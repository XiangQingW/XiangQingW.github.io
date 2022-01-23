---

title: 如何在Python中搜索一个字符串？
date: 2022-01-23T22:08:22+08:00

---




## 如何在Python中搜索一个字符串？  
### 回答 1
您需要查看以下方法  
[代码]  
打开（）  
file.close（）  
用open（）如  
file.read（）  
file.readlines（）  
file.write（）  
[/代码]  
一旦您获得了打开和关闭和读取文件的挂起，那么您就在对象类型搜索中执行普通字符串  
### 回答 2
这是一个可能导致Python编程的基础知识，进入一些基本算法分析，并包括Python中的上下文管理器的主题。  
虽然你可能只是想要答案，但你会发现它和无数的其他实际编程相关的答案，在stackoverflow上。快乐编码！  
### 回答 3
打印（你是什么？  
您可以使用RAW_INPUT（）或输入（）命令在Python中取出。  
打印Hello消息的程序：  
打印（你的名字是什么？）  
name = input（）  
打印（你好％s！你好吗？％名称）  
打印数字平方的程序：  
num = int（输入（输入数字））  
打印（数字的平方是：，num ** 2）  
### 回答 4
嘿！  
因此，有两种方式可以在其中反转用户输入的字符串。  
<ol> str =输入（）打印（str [::  -  1]）</ ol>  
<li>打印（str [::  -  1]）</ li>  
2.使用内置的字符串反向功能：  
<ol> str =输入（）打印（反向（str））</ ol>  
<li> str =输入（）</ li>  
<li>打印（反向（str））</ li>  
希望这有助于帮助！  
### 回答 5
Python列表可轻松转换为字符串。在这里，我介绍了您可以获得的不同方式。  
在这里，我们的示例列表是 -   
a_list = [我，我，20年，旧]  
需要转换为像这样的字符串 -   
我20岁了  
。  
使用循环  
<ol> a_list = [i，am，20，岁，旧]结果=对于a_list中的元素：结果+ = str（元素）+打印（结果）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果= </ li>  
<li>在a_list中的元素：</ li>  
<li>结果+ = str（元素）+ </ li>  
<li> </ li>  
<li>打印（结果）</ li>  
。  
使用加入  
<ol> a_list = [i，AM，20，岁，旧]结果= .join（str（i）在a_list中）打印（结果）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果= .join（str（i）在a_list中）</ li>  
<li>打印（结果）</ li>  
。  
使用地图+加入  
<OL> A_LIST = [i，AM，20，岁，旧]结果= .join（map（str，a_list））打印（结果）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果= .join（地图（str，a_list））</ li>  
<li>打印（结果）</ li>  
。  
使用reduc  
Python列表可轻松转换为字符串。在这里，我介绍了您可以获得的不同方式。  
在这里，我们的示例列表是 -   
a_list = [我，我，20年，旧]  
需要转换为像这样的字符串 -   
我20岁了  
。  
使用循环  
<ol> a_list = [i，am，20，岁，旧]结果=对于a_list中的元素：结果+ = str（元素）+打印（结果）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果= </ li>  
<li>在a_list中的元素：</ li>  
<li>结果+ = str（元素）+ </ li>  
<li> </ li>  
<li>打印（结果）</ li>  
。  
使用加入  
<ol> a_list = [i，AM，20，岁，旧]结果= .join（str（i）在a_list中）打印（结果）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果= .join（str（i）在a_list中）</ li>  
<li>打印（结果）</ li>  
。  
使用地图+加入  
<OL> A_LIST = [i，AM，20，岁，旧]结果= .join（map（str，a_list））打印（结果）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果= .join（地图（str，a_list））</ li>  
<li>打印（结果）</ li>  
。  
使用Really + Lambda函数  
<OL>从Functools导入减少A_List = [i，AM，20，旧]结果=减少（lambda i，j：f {i} {j}，a_list）打印（结果）</ ol>  
<li>从Functools导入减少</ li>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>结果=减少（lambda i，j：f {i} {j}，a_list）</ li>  
<li>打印（结果）</ li>  
。  
使用SEP参数  
如果您只需要将列表打印到字符串中，那么您可以使用此功能。  
<ol> a_list = [i，我，20，年，旧]打印（* a_list，sep =）</ ol>  
<li> a_list = [我，我，20年，旧] </ li>  
<li>打印（* a_list，sep =）</ li>  
### 回答 6
声明一个变量：  
<OL> x = AMR </ OL>  
<li> x = amr </ li>  
您可以访问这样的字符：  
<OL>打印（x）＃输出：AMR PRINT（X [0]）＃输出：打印（X [1]）＃输出：B打印（X [2]）＃输出：C打印（x [：] ）＃输出：AMR PRINT（X [::  -  1]）＃输出：RMA PRINT（x [：2]）＃输出：AM </ OL>  
<li>打印（x）＃输出：amr </ li>  
<li>打印（x [0]）＃输出：a </ li>  
<li>打印（x [1]）＃输出：b </ li>  
<li>打印（x [2]）＃输出：c </ li>  
<li> </ li>  
<li>打印（x [：]）＃输出：AMR </ Li>  
<li>打印（x [::  -  1]）＃输出：RMA </ LI>  
<li>打印（x [：2]）＃输出：Am </ Li>  
但是当你尝试编辑这样的角色时：  
<ol> x [0] = b＃error tyouperror：str对象不支持项目分配</ ol>  
<li> x [0] = b＃error </ li>  
<li> typeerror：str对象不支持项目分配</ li>  
<li> </ li>  
它不接受更改，因为字符串是不可变的对象，您无法编辑一旦创建的字符串变量。这有很多关于互联网的答案。谷歌这个问题并阅读了关于字符串可变性的一些答案。  
这  
声明一个变量：  
<OL> x = AMR </ OL>  
<li> x = amr </ li>  
您可以访问这样的字符：  
<OL>打印（x）＃输出：AMR PRINT（X [0]）＃输出：打印（X [1]）＃输出：B打印（X [2]）＃输出：C打印（x [：] ）＃输出：AMR PRINT（X [::  -  1]）＃输出：RMA PRINT（x [：2]）＃输出：AM </ OL>  
<li>打印（x）＃输出：amr </ li>  
<li>打印（x [0]）＃输出：a </ li>  
<li>打印（x [1]）＃输出：b </ li>  
<li>打印（x [2]）＃输出：c </ li>  
<li> </ li>  
<li>打印（x [：]）＃输出：AMR </ Li>  
<li>打印（x [::  -  1]）＃输出：RMA </ LI>  
<li>打印（x [：2]）＃输出：Am </ Li>  
但是当你尝试编辑这样的角色时：  
<ol> x [0] = b＃error tyouperror：str对象不支持项目分配</ ol>  
<li> x [0] = b＃error </ li>  
<li> typeerror：str对象不支持项目分配</ li>  
<li> </ li>  
它不接受更改，因为字符串是不可变的对象，您无法编辑一旦创建的字符串变量。这有很多关于互联网的答案。谷歌这个问题并阅读了关于字符串可变性的一些答案。  
解决方案：  
您可以将字符串转换为列表，使用其索引更改字符并将列表转换回字符串：  
<ol> x = amr x = list（x）＃将字符串转换为列表打印（x）＃输出：[a，m，r] x [0] = b#使用其索引打印（x）更改字符＃输出：[b，m，r] x = .join（x）＃通过使用zling方法将列表更改为返回字符串。 （Google IT）打印（x）＃输出：BMR </ OL>  
<li> x = amr </ li>  
<li> x = list（x）＃将字符串转换为列表</ li>  
<li>打印（x）＃输出：[a，m，r] </ li>  
<li> x [0] = b＃使用其索引更改字符</ li>  
<li>打印（x）＃输出：[b，m，r] </ li>  
<li> x = .join（x）＃通过使用串的连接方法将列表更改为返回字符串。 （谷歌它）</ li>  
<li> </ li>  
<li>打印（x）＃输出：bmr </ li>  
您可以通过另一种方法（字符串切片）执行此操作：  
<ol> x = amr x = b + x [1：]＃输出：bmr x = amr x = x [：1] + b + x [2：]＃输出：abr </ ol>  
<li> x = b + x [1：]＃输出：bmr </ li>  
<li> </ li>  
<li> x = amr </ li>  
<li> x = x [：1] + b + x [2：]＃输出：abr </ li>  
只是玩这种方法，直到你理解它很好。  
我希望这可以帮到你。  
### 回答 7
这是一个已经回答了，但我们可以添加一些更多的Python语法糖来得到期望的结果。  
<01 >>>> >>>你好K =列表（k）的[H，E，L，L，O] >>> [I为i的k]的[H，E，L，L，O]> [升用于升上述（i对于i在K）] [H，E，L，L，O] >>> [I对于i在k.split（）[0] [H，E，1,1- [O] >>> Z = [] >>>为i的范围（LEN（K））：... z.append（K [切片（I，I + 1）]）... >>> Z [小时， E，L，L，O] >>>打印（[* K]）[H，E，L，L，O] </醇>  
<锂K = >>>>你好</ LI>  
<锂>>>>列表（k）的</ LI>  
<锂>>>> [I为i的k]的</ LI>  
<锂>>>> </ LI [第（i为i的k）的升用于升]>  
<锂>>>> [I对于i在k.split（）[0] </ LI>  
<LI>并[h，E，L，L，O] </ LI>  
<LI> </ LI>  
<锂>>>> Z = [] </ LI>  
<锂>>>>对于i在范围（LEN（K））。</ LI>  
<LI> ... z.append（K [切片（I，I + 1）]）</ LI>  
<LI> ... </ li>  
<锂>>>>ž</ LI>  
<LI> </ LI>  
<锂>>>>打印（[* K]）</ LI>  
<LI>并[h，E，L，L，O] </ LI>  
然而，另一个问题：  
<01 >>>> >>> DEF你好ķmake_list（*参数）：...返回[I对于i在args] ... >>> make_list（k）的[H，E，L，L，O] </醇>  
<锂>>>>ķ</ LI>  
<LI>你好</ LI>  
<锂>>>> DEF make_list（*参数）：</ LI>  
<LI> ...返回[I对于i在args] </ LI>  
<LI> ... </ li>  
<锂>>>> make_list（k）的</ LI>  
<LI>并[h，E，L，L，O] </ LI>  
### 回答 8
您可以使用Python中的设置操作进行。  
<ol> string1 = sathua string2 = hat s1 = set（string1）s2 = set（String2）common_char = s1和s2中的s1和s2＃字母在s1和s2 </ ol>中  
<li> string1 = sathua </ li>  
<li> string2 = hat </ li>  
<li> s1 = set（string1）</ li>  
<li> s2 = set（string2）</ li>  
<li> common_char = s1和s2中的s1和s2＃字母</ li>  
输出：{'t'，'a'，'h'}  
享受编码...... :-)  
### 回答 9
你可以至少两种方式做到这一点。第一个是将字符串拆分为单词列表，抛出第一个单词，然后用空格加入剩下的返回。  
<ol> string =这是一个字符串split_string = string.split（）new_string_list = split_string [1：] new_string = .join（new_string_list）print（new_string）</ ol>  
<li> string =这是一个字符串</ li>  
<li> split_string = string.split（）</ li>  
<li> new_string_list = split_string [1：] </ li>  
<li> new_string = .join（new_string_list）</ li>  
<li>打印（new_string）</ li>  
第二个是找到字符串中第一个空间的索引，然后只需在空间前面夹出一切。  
<ol> string =这是一个字符串space_index = string.find（）new_string = string [space_index：] print（new_string）</ ol>  
<li> string =这是一个字符串</ li>  
<li> space_index = string.find（）</ li>  
<li> new_string = string [space_index：] </ li>  
<li>打印（new_string）</ li>  
第一种方法允许您操纵另一个单词  
你可以至少两种方式做到这一点。第一个是将字符串拆分为单词列表，抛出第一个单词，然后用空格加入剩下的返回。  
<ol> string =这是一个字符串split_string = string.split（）new_string_list = split_string [1：] new_string = .join（new_string_list）print（new_string）</ ol>  
<li> string =这是一个字符串</ li>  
<li> split_string = string.split（）</ li>  
<li> new_string_list = split_string [1：] </ li>  
<li> new_string = .join（new_string_list）</ li>  
<li>打印（new_string）</ li>  
第二个是找到字符串中第一个空间的索引，然后只需在空间前面夹出一切。  
<ol> string =这是一个字符串space_index = string.find（）new_string = string [space_index：] print（new_string）</ ol>  
<li> string =这是一个字符串</ li>  
<li> space_index = string.find（）</ li>  
<li> new_string = string [space_index：] </ li>  
<li>打印（new_string）</ li>  
第一个方法允许您操作字符串中的其他单词。第二种方法更简单。  
### 回答 10
您可以通过多种方式执行此操作。您可以检查字符串的长度并将其与0进行比较，如  
说明：ln（）函数是函数的构建，它给出了字符串的长度  
如果您的字符串为空，则在该案例光标将是真的条件  
进入IF语句，它将打印空字符串（因为在打印中的按摩是空字符串）  
另一种方法是  
假设一个s =  
这里是一个空字符串，现在通过比较它来检查所需的字符串  
### 回答 11
您可以遵循Ahad Raheman的解决方案，因为它很容易理解。我会告诉你这个词被发现的索引。在文本文件中搜索单词就像在文件中执行线性搜索。这是你将如何做到： -   
<ol> s =输入（在文件中输入要搜索的单词 - >）fp = file.txt // fp变量将把filepath存储到文件f =打开（fp）// f变量将用作文件访问器标志= index = 0 for f：line.strip（）。拆分（\ n）索引+ = 1如果s in line：flag = 1 break如果标志== 0：print（fsorry无法找到{s}） ：打印</ ol>  
<li> s =输入（在文件中输入要搜索的单词 - >）</ li>  
<li> fp = file.txt // fp变量将文件属于文件</ li>  
<li> f =打开（fp）// f变量将用作文件访问器</ li>  
<li>标志= index = 0 </ li>  
<li> </ li>  
<li>在f：</ li>中线  
<li> line.strip（）。拆分（\ n）</ li>  
<li>索引+ = 1 </ li>  
<li>如果是s：</ li>  
<li>标志= 1 </ li>  
<li>打破</ li>  
<li> </ li>  
<li>如果标志== 0：</ Li>  
<li>打印（fsorry无法找到{s}）</ li>  
<li> else：</ li>  
<li>打印</ li>  
您可以遵循Ahad Raheman的解决方案，因为它很容易理解。我会告诉你这个词被发现的索引。在文本文件中搜索单词就像在文件中执行线性搜索。这是你将如何做到： -   
<ol> s =输入（在文件中输入要搜索的单词 - >）fp = file.txt // fp变量将把filepath存储到文件f =打开（fp）// f变量将用作文件访问器标志= index = 0 for f：line.strip（）。拆分（\ n）索引+ = 1如果s in line：flag = 1 break如果标志== 0：print（fsorry无法找到{s}） ：打印（Ffound {s}中{index}）f.close（）</ ol>  
<li> s =输入（在文件中输入要搜索的单词 - >）</ li>  
<li> fp = file.txt // fp变量将文件属于文件</ li>  
<li> f =打开（fp）// f变量将用作文件访问器</ li>  
<li>标志= index = 0 </ li>  
<li> </ li>  
<li>在f：</ li>中线  
<li> line.strip（）。拆分（\ n）</ li>  
<li>索引+ = 1 </ li>  
<li>如果是s：</ li>  
<li>标志= 1 </ li>  
<li>打破</ li>  
<li> </ li>  
<li>如果标志== 0：</ Li>  
<li>打印（fsorry无法找到{s}）</ li>  
<li> else：</ li>  
<li>打印（在线{index}中的ffound {s}）</ li>  
<li> </ li>  
<li> f.close（）</ li>  
