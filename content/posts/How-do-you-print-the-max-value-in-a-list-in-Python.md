---

title: 如何在Python列表中打印最大值？
date: 2022-01-23T22:08:09+08:00

---




## 如何在Python列表中打印最大值？  
### 回答 1
使用max（）函数  
例子  
<ol> list1 = [2,4,6,11,1,45]打印（max（list1））</ ol>  
<li>列表1 = [2,4,6,11,1,45] </ li>  
<li>打印（max（list1））</ li>  
### 回答 2
您可以使用max（）函数：  
<ol>列表= [1,2,3,4,5]打印（max（list））</ ol>  
<li>列表= [1,2,3,4,5] </ li>  
<li>打印（max（list））</ li>  
输出：  
<OL> 5 </ OL>  
<li> 5 </ li>  
或者您可以使用A for循环并比较每个数字并跟踪找到的最大数字：  
<ol>列表= [1,2,3,4,5] max = list [0]列表中的num：如果num> max：max = num print（max）</ ol>  
<li>列表= [1,2,3,4,5] </ li>  
<li> max = list [0] </ li>  
<li>为num列表：</ li>  
<li>如果num> max：</ li>  
<li> max = num </ li>  
<li>打印（max）</ li>  
输出：  
<OL> 5 </ OL>  
<li> 5 </ li>  
### 回答 3
定义： - 定义： -   
Python编程语言中有四种集合数据类型，其中列表是Python中最常见的数据结构之一。  
<ol> <class list> </ ol>  
<li> <class list> </ li>  
声明：-declaration： -   
宣布列表有三种方法：  
<ol>这个列表= [0，苹果，真，一个好孩子，真实，[1，香蕉，假]] </ ol>  
<li>这个列表= [0，苹果，真，一个好孩子，真实，[1，香蕉，假]] </ li>  
定义： - 定义： -   
Python编程语言中有四种集合数据类型，其中列表是Python中最常见的数据结构之一。  
<ol> <class list> </ ol>  
<li> <class list> </ li>  
声明：-declaration： -   
宣布列表有三种方法：  
<ol>这个列表= [0，苹果，真，一个好孩子，真实，[1，香蕉，假]] </ ol>  
<li>这个列表= [0，苹果，真，一个好孩子，真实，[1，香蕉，假]] </ li>  
<ol> thislist = list（（0，Apple，True，一个好孩子，真实，[1，香蕉，假]））</ OL>  
<li>这个列表= list（（0，Apple，True，一个好孩子，真实，[1，香蕉，假]））</ li>  
<ol> newlist = [oldlist中的元素的表达式（元素）如果条件，则newlist = [x-1在范围（n）中（n），如果x> 2] newlist = [0] * n newlist = [0在范围内（n）] j在范围（行）] </ ol>中，newlist = [[0在范围（cols）]] </ ol>  
<li> newlist = [旧列表中的元素的表达式（元素）如果条件] </ li>  
<li> newlist = [x-1，I如果x> 2，则在范围内（n）] </ li>  
<li> newlist = [0] * n </ li>  
<li> newlist = [0在范围内（n）] </ li>  
<li> newlist = [[0在范围（cols）中]的j范围（行）] </ li>  
特点： - 特点： -   
列表有三个主要功能：  
用途：--uses： -   
列表有两个主要用法：  
### 回答 4
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
### 回答 5
您可以使用任何这些来查找最大值 -   
<ol> l = [2,5,8,1,9,2]打印（max（l））输出-9 </ OL>  
<li>打印（max（l））</ li>  
<OL> L = [2,5,8,1,9,2]打印（排序（L，Reverse = True）[0]）输出-9 </ OL>  
<li>打印（排序（l，reverse = true）[0]）</ li>  
<li>输出-9 </ li>  
<ol> l = [2,5,8,1,9,2]在范围内（len（l）-1）：如果l [i]> l [i + 1]：l [i]，l[I + 1] = L [I + 1]，L [I]打印（L [-1]）输出-9 </ OL>  
<Li> L = [2,5,8,1,9,2] </ li>  
<li> i在范围内（len（l）-1）：</ li>  
<li>如果l [i]> l [i + 1]：</ li>  
<li> l [i]，l [i + 1] = l [i + 1]，l [i] </ li>  
<li>打印（l [-1]）</ li>  
<li>输出-9 </ li>  
### 回答 6
如果你的意思是如何添加字符串的每个单词，那么拆分（）应该是您的样子所在：  
<ol >>>> string = hello world >>> string.split（）[hello，world] </ ol>  
<li >>>> string = hello world </ li>  
<li >>>> string.split（）</ li>  
<li> [你好，世界] </ li>  
要将其用于用户输入的整数，可以使用：  
<ol >>>> user_input =输入（键入您的号码\ n）键入您的数字1 2 3 >>> [in for user_input.split（）] [1,2,3] </ ol>的x  
<li >>>> user_input =输入（键入您的号码\ n）</ li>  
<li>键入您的号码</ li>  
<li> 1 2 3 </ li>  
<li >>>> [int（x）在user_input.split（）中的x] </ li>  
<li> [1,2,3] </ li>  
请注意，拆分（）将空格作为默认分隔符，但这可能是任何东西。例如：  
<ol >>>> user_input =输入（键入您的号码\ n）键入您的数字1,2,3 >>> [in for user_input.split（，）] [1,2,3] < / ol>  
<li >>>> user_input =输入（键入您的号码\ n）</ li>  
<li>键入您的号码</ li>  
<li> 1,2,3 </ li>  
<li >>>> [int（x）在user_input.split（，）] </ li>中  
<li> [1,2,3] </ li>  
### 回答 7
str（）是用于将数据转换为字符串数据类型的Python内置函数。写入str（1）时，返回的值将是字符串类型1而不是整数类型。与INT（1）上的数学操作相比，STR（1）的数学操作给出了不同的值。下面我解释了一些情景  
<ol> i = int（2）打印（i * 3）#gives输出6 IE 2 * 3 = 6 s = str（2）打印（s * 3）#gives输出222 IE 2 * 3 = 222打印（s +3）＃自Int和String无法连接以来抛出错误。打印（S + STR（3））#gives输出23.打印（S + STR（3）+ A）#gives输出23a打印（S / 3）#Throws误差。由于字符串CA </ OL>  
<li> i = int（2）</ li>  
<li>打印（i * 3）#gives输出6 i.e 2 * 3 = 6 </ li>  
<li> s = str（2）</ li>  
<li>打印（s * 3）#gives输出222 i.e 2 * 3 = 222 </ li>  
<li>打印（s + 3）＃自Int和string无法连接以来抛出错误。 </ Li>  
<li>打印（S + str（3））#gives输出23. </ li>  
<li>打印（S + str（3）+ a）#gives输出23a </ li>  
<li> </ li>  
<li>打印（s / 3）#throws一个错误。由于字符串Ca </ li>  
str（）是用于将数据转换为字符串数据类型的Python内置函数。写入str（1）时，返回的值将是字符串类型1而不是整数类型。与INT（1）上的数学操作相比，STR（1）的数学操作给出了不同的值。下面我解释了一些情景  
<ol> i = int（2）打印（i * 3）#gives输出6 IE 2 * 3 = 6 s = str（2）打印（s * 3）#gives输出222 IE 2 * 3 = 222打印（s +3）＃自Int和String无法连接以来抛出错误。打印（S + STR（3））#gives输出23.打印（S + STR（3）+ A）#gives输出23a打印（S / 3）#Throws误差。由于弦不能分开。 </ OL>  
<li> i = int（2）</ li>  
<li>打印（i * 3）#gives输出6 i.e 2 * 3 = 6 </ li>  
<li> s = str（2）</ li>  
<li>打印（s * 3）#gives输出222 i.e 2 * 3 = 222 </ li>  
<li>打印（s + 3）＃自Int和string无法连接以来抛出错误。 </ Li>  
<li>打印（S + str（3））#gives输出23. </ li>  
<li>打印（S + str（3）+ a）#gives输出23a </ li>  
<li> </ li>  
<li>打印（s / 3）#throws一个错误。由于弦不能分开。 </ Li>  
请注意，STR（2），2和“2”所有被视为琴弦。  
### 回答 8
A2A。  
基于附加的链接以及问题。试图调整它。所以，你得到了预期的结果。您希望代码的输出为547欧姆而不是547.在我给你解决方案之前。  
在这里，以一般方式回答问题。这显示了将列表转换为字符串的一种可能方法。  
<ol> l = [5,4,7] s = .join（l）打印（s）</ ol>  
<li> l = [5,4,7] </ li>  
<li> s = .join（l）</ li>  
<li>打印（s）</ li>  
这将打印列表中的元素作为字符串。而且，你会得到类似的东西  
<OL> 547 </ OL>  
<li> 547 </ li>  
一旦你有一些东西。您可以轻松地添加字符串字符。就像是。  
<OL>打印（S +欧姆）</ OL>  
<li>打印（s +欧姆）</ li>  
并获得所需的输出lik  
A2A。  
基于附加的链接以及问题。试图调整它。所以，你得到了预期的结果。您希望代码的输出为547欧姆而不是547.在我给你解决方案之前。  
在这里，以一般方式回答问题。这显示了将列表转换为字符串的一种可能方法。  
<ol> l = [5,4,7] s = .join（l）打印（s）</ ol>  
<li> l = [5,4,7] </ li>  
<li> s = .join（l）</ li>  
<li>打印（s）</ li>  
这将打印列表中的元素作为字符串。而且，你会得到类似的东西  
<OL> 547 </ OL>  
<li> 547 </ li>  
一旦你有一些东西。您可以轻松地添加字符串字符。就像是。  
<OL>打印（S +欧姆）</ OL>  
<li>打印（s +欧姆）</ li>  
并获得所需的输出  
<OL> 547Ohms </ OL>  
<li> 547 ohms </ li>  
注意：加入是字符串的方法。它希望列表中存在的元素必须是字符串。如果他们不是。您会收到错误的错误，如TypeError：Sequence Item 0：Intipe Item 0：INT。这意味着它是期待一个字符串但是得到了整数。  
如果您的列表包含整数。您必须将整数转换为字符串。就像是  
<ol> l = [1,2,3] s = .join（L]中元素的[str（元素）]打印（s）</ ol>  
<li> l = [1,2,3] </ li>  
<li> s = .join（l]中元素的[str（元素））</ li>  
<li>打印（s）</ li>  
回到代码。您已明确提及以运行输入0,1,3的代码。  
您的代码的最后两行可以用我尝试在上面解释的东西替换。  
<ol>在范围内的项目（0，len（a））：打印（a [项目]，end =）</ ol>  
<li>为范围内的项目（0，Len（A））：</ Li>  
<li>打印（a [项目]，end =）</ li>  
相反，你可以做一些类似的事情  
<ol> s = .join（a的元素[str（元素）]）+欧姆打印（s）</ ol>  
<li> s = .join（a中元素的[str（元素）]）+欧姆</ li>  
<li>打印（s）</ li>  
您可以查看以下链接中的完整代码。  
在这里Quora怀疑。 :)  
希望能帮助到你。并给出您想要的输出。  
任何疑虑仍然存在。评论，我很乐意提供帮助。  
### 回答 9
有几种方法可以这样做。  
最简单的（但也没有保证）的方式是刚刚通过空格拆分输入。  
<ol> some_list = [n在输入（）中的n。拆分（）] </ ol>  
<li> yem_list = [n for n在输入（）中。拆分（）] </ li>  
这可以通过用户迅速滥用，因为它们可以轻松输入更多或小于六个值。  
另一种方法是为循环执行一个循环并将输入附加到列表。  
<ol> some_list = []在范围内（6）：some_list.append（输入（））</ ol>  
<li> some_list = [] </ li>  
<li>为I系列（6）：</ li>  
<li> some_list.append（输入（））</ li>  
最粘散的方式是通过组合前两种方法在一步中完成这一点。  
<ol> some_list = [IN输入（）在范围内（6）] </ ol>  
<li> you_list = [Input（）在范围（6）] </ li>  
### 回答 10
有三种不同的数字类型：整数，浮点数和复数。此外，Booleans是整数的子类型。整数具有无限的精度。浮点数通常使用双倍实现。  
Sys.Flaot.Info提供了有关您程序运行的计算机的浮点号的精度和内部表示的信息。复数有一个真实和虚部，每个浮点数。  
从复杂的数字Z中提取这些部件，使用Z.real和Z.imag。 （标准库包括额外的数字类型，属性的分数，并按住具有用户可定义精度的浮点数的小数。）  
### 回答 11
<ol> a = [1,2,3] a = a + [4,5,6]＃甚至a + = [4,5,6]＃保留相同的引用，以便分享它a.extend（[4,5,6]）</ OL>  
<li> a = [1,2,3] </ li>  
<li> a = a + [4,5,6] </ li>  
<li>＃甚至</ li>  
<li> a + = [4,5,6] </ li>  
<li>＃保留相同的引用，以便您可以分享它</ li>  
<li> a.extend（[4,5,6]）</ li>  
