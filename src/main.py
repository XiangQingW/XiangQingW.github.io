# -*- coding: utf-8 -*-
# __main__.py
import subprocess
import sqlite3
import os.path


QUORA_DB = "out\quora.db"
GENED_QUESTION_IDS_FILE = "out\gened_question_ids.txt"

class CnAnswerRow:
    def __init__(self, question_id, title, content):
        self.question_id = question_id
        self.title = title
        self.content = content


def get_all_cn_answers():
    conn = sqlite3.connect(QUORA_DB)
    c = conn.cursor()

    data = c.execute('SELECT question_id, question_title, content from answer_cn')
    id2answer = {}

    for row in data:
        (question_id, title, content) = row
        answer = CnAnswerRow(question_id, title, content)
        if question_id not in id2answer:
            id2answer[question_id] = [answer]
        else:
            id2answer[question_id].append(answer)

    conn.commit()
    conn.close()

    return id2answer


def get_all_gened_question_ids():
    if not os.path.isfile(GENED_QUESTION_IDS_FILE):
        return set()

    f = open(GENED_QUESTION_IDS_FILE, 'r', encoding='utf-8')
    gened_ids = set()

    for line in f:
        gened_ids.add(line.rstrip('\r\n'))

    f.close()
    return gened_ids


def read_post_header(path):
    f = open(path, 'r', encoding='utf-8')

    lines = []
    for line in f:
        if 'draft' in line:
            continue
        lines.append(line)

    f.close()
    return lines


def write_post(path, contents):
    f = open(path, 'w', encoding='utf-8')

    for line in contents:
        f.write(line)

    f.close()


def write_gened_question_id(id):
    f = open(GENED_QUESTION_IDS_FILE, 'a+', encoding='utf-8')
    f.write(id + '\n')
    f.close()


def gen_docs():
    id2answers = get_all_cn_answers()
    all_gened_question_ids = get_all_gened_question_ids()

    cur_post_count = 0
    total_post_count = len(id2answers)

    for question_id, answers in id2answers.items():
        cur_post_count += 1
        print('start to gen post: {}/{}'.format(cur_post_count, total_post_count))
        if question_id in all_gened_question_ids:
            print('Question has already gened: id= ', question_id)
            continue

        if not answers:
            print('Questoin doesnt have answer: ', question_id)
            continue

        title = answers[0].title
        path = 'posts/' + title[:50] + '.md'

        subprocess.run(['hugo', 'new', path], shell=True)

        path = 'content/' + path

        post_content = read_post_header(path)
        post_content.append('\n')
        post_content.append('## ' + title + '  ')

        post_content.append('\n')
        for idx, answer in enumerate(answers):
            post_content.append('### ' + '答案 ' + str(idx + 1) + '\n')
            for line in answer.content.splitlines():
                post_content.append(line + '  ' + '\n')

        write_post(path, post_content)

        print('gen post suc: {}/{}'.format(cur_post_count, total_post_count))

        all_gened_question_ids.add(question_id)
        write_gened_question_id(question_id)
        break


def main():
    gen_docs()


if __name__ == '__main__':
    main()