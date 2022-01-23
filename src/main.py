# -*- coding: utf-8 -*-
# __main__.py
import subprocess
import sqlite3

QUORA_DB = "out\quora.db"

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


def gen_doc():
    subprocess.run(['hugo', '-h'], shell=True)
    id2answers = get_all_cn_answers()
    for question_id, answers in id2answers.items():
        print(question_id)
        print(len(answers))
        break;


def main():
    gen_doc()


if __name__ == '__main__':
    main()
