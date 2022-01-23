---

title: 如何编写一个程序以输入10个数字，并查找其总和？
date: 2022-01-23T22:08:22+08:00

---




## 如何编写一个程序以输入10个数字，并查找其总和？  
### 回答 1
由于您没有指定语言，我绝对确定您希望在J.作为奖励中对此问题的解决方案，它实际上将在一系列任意长度上工作，只要您通过空格拆分所有条目！  
<ol> + / @ :(。; ._ 2＆:(，＆）＆:( 1！：1）＆1 :) </ ol>  
<li> + / @ :(。; ._ 2＆:(，＆）＆:( 1！：1）＆1 :) </ li>  
我希望这有帮助！否则，在苗条的机会上，您正在使用一些无聊的语言为您的作业，考虑阅读教科书中的相关材料并使用它提出解决方案。我相当确定循环和数组索引彻底覆盖。  
P.S.如果您真的坚持为10个数字，并且不再或更少，您将需要在函数中管道，这将在长度不匹配时抛出错误：  
<ol> [：^ :( 10＆：〜：＆：＃）nb。 [： - 抛出错误NB。 ^： - 如果nb。 10  -  10 NB。 〜： - 不等于NB。 ＃ - 数组长度</ ol>  
<li> [：^ :( 10＆：〜：＆：＃）</ li>  
<li> Nb。 [： - 抛出错误</ li>  
<li> Nb。 ^： - 如果</ li>  
<li> Nb。 10  - 十分</ li>  
<li> Nb。 〜： - 不等于</ li>  
<li> Nb。 ＃ - 数组长度</ li>  
这将产生最终功能  
<ol> + / @：（[：^ :( 10＆〜：＆：＃））@ :(。; 2＆：（，＆）＆:( 1！：1）＆1 :) ^^这里是^ ^ </ ol>  
<li> + / @：（[：^ :( 10＆〜：＆：＃））@ :(。; 2＆：（，＆）＆:( 1！：1）＆1 :) </ li>  
<li> ^^在这里它是^^ </ li>  
P.P.S.我用了一个无聊的语言，但我忘了使用阵列:(  
<OL>公共静态void main（String ... args）{最终扫描仪扫描仪=新扫描仪（System.in）; system.out.println（intstream.generate（扫描仪:: nextint）.limit（10）.sum（））; } </ OL>  
<li>公共静态void main（String ... args）{</ li>  
<li>最终扫描仪扫描仪=新扫描仪（System.in）; </ Li>  
<li> system.out.println（</ li>  
<li> intstream.generate（扫描仪:: nextint）.limit（10）.sum（）</ li>  
<li>）; </ Li>  
<li>} </ li>  
### 回答 2
在C.  
<ol> #include <stdio.h> int main（）{int i，arr [10]，sum = 0; printf（输入10个元素:); for（i = 0; i <10; ++ i）scanf（％d，＆arr [i]）; for（i = 0; i <10; ++ i）sum = sum + arr [i]; Printf（数字总和是：％d，sum）;返回0; } </ OL>  
<li> #include <stdio.h> </ li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int i，arr [10]，sum = 0; </ Li>  
<li> printf（输入10个元素:); </ Li>  
<li> scanf（％d，＆arr [i]）; </ Li>  
<li>（i = 0; i <10; ++ i）</ li>  
<li> sum = sum + arr [i]; </ Li>  
<li> printf（数字总和是：％d，sum）; </ Li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
在C ++中  
使用命名空间std <ol> #include <iostream> int main（）{int i，arr [10]，sum = 0; cout <<输入10个元素： for（i = 0; i <10; ++ i）CIN >> ARR [I]; for（i = 0; i <10; ++ i）sum = sum + arr [i]; cout <<数字的总和：<<总和;返回0; } </ OL>  
<li> #include <iostream> </ li>  
使用命名空间std; </ Li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int i，arr [10]，sum = 0; </ Li>  
<li> cout <<输入10个元素： </ Li>  
<li> cin >> arr [i]; </ Li>  
<li>（i = 0; i <10; ++ i）</ li>  
<li> sum = sum + arr [i]; </ Li>  
<li> cout <<数字总和：<<总和; </ Li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
在Java.  
<ol>导入java.util.scanner;公共类示例12 {公共静态void main（String [] args）{int </ ol>  
<li>导入java.util.scanner; </ Li>  
<li>公共类示例12 {</ li>  
<li>公共静态void main（String [] args）{</ li>  
<li> </ li>  
<li> int </ li>  
在C.  
<ol> #include <stdio.h> int main（）{int i，arr [10]，sum = 0; printf（输入10个元素:); for（i = 0; i <10; ++ i）scanf（％d，＆arr [i]）; for（i = 0; i <10; ++ i）sum = sum + arr [i]; Printf（数字总和是：％d，sum）;返回0; } </ OL>  
<li> #include <stdio.h> </ li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int i，arr [10]，sum = 0; </ Li>  
<li> printf（输入10个元素:); </ Li>  
<li> scanf（％d，＆arr [i]）; </ Li>  
<li>（i = 0; i <10; ++ i）</ li>  
<li> sum = sum + arr [i]; </ Li>  
<li> printf（数字总和是：％d，sum）; </ Li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
在C ++中  
使用命名空间std <ol> #include <iostream> int main（）{int i，arr [10]，sum = 0; cout <<输入10个元素： for（i = 0; i <10; ++ i）CIN >> ARR [I]; for（i = 0; i <10; ++ i）sum = sum + arr [i]; cout <<数字的总和：<<总和;返回0; } </ OL>  
<li> #include <iostream> </ li>  
使用命名空间std; </ Li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int i，arr [10]，sum = 0; </ Li>  
<li> cout <<输入10个元素： </ Li>  
<li> cin >> arr [i]; </ Li>  
<li>（i = 0; i <10; ++ i）</ li>  
<li> sum = sum + arr [i]; </ Li>  
<li> cout <<数字总和：<<总和; </ Li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
在Java.  
<ol>导入java.util.scanner;公共类示例12 {公共静态void main（String [] args）{int i，sum = 0; int arr [] =新int [10]; system.out.println（输入10个数字）; Scanner SC = New Scanner（System.in）; for（i = 0; i <10; ++ i）arr [i] = sc.nextint（）; for（i = 0; i <10; ++ i）sum = sum + arr [i]; system.out.println（数字总和是：+和）; }} </ OL>  
<li>导入java.util.scanner; </ Li>  
<li>公共类示例12 {</ li>  
<li>公共静态void main（String [] args）{</ li>  
<li> int i，sum = 0; </ Li>  
<li> int arr [] = new int [10]; </ Li>  
<li> system.out.println（输入10个数字）; </ Li>  
<li> scanner sc = new scanner（system.in）; </ Li>  
<li> arr [i] = sc.nextint（）; </ Li>  
<li>（i = 0; i <10; ++ i）</ li>  
<li> sum = sum + arr [i]; </ Li>  
<li> system.out.println（数字总和是：+和）; </ Li>  
<li> </ li>  
<li>} </ li>  
在这里，我使用两个循环，一个读取和其他用于查找和。  
您可以将读数和求和与相同的循环相结合  
<OL> for（i = 0; i <10; ++ i）{scanf（％d，＆arr [i]）; SUM = SUM + ARR [I]; } </ OL>  
<li>（i = 0; i <10; ++ i）</ li>  
<li> {</ li>  
<li> scanf（％d，＆arr [i]）; </ Li>  
<li> </ li>  
<li> sum = sum + arr [i]; </ Li>  
<li>} </ li>  
### 回答 3
//示例程序  
#include <iostream>  
#include <string>  
使用命名空间std;  
int main（）  
int arr [10];  
int art_sum = 0;  
for（int i = 0; i <10; i ++）  
{  
cout <<输入元素：<< I + 1 << ENDL;  
CIN >> ARR [I];  
arr_sum + = arr [i];  
cout <<数组元素的总和：<< ARR_SUM << ENDL;  
}  
输出快照  
### 回答 4
在C编程 -   
<ol> #include <stdio.h> main（）{int a [10]，i，sum = 0;printf（输入array \ n）;for（i = 0; i <10; i ++）{scanf（％d，＆a [i]）;总和= sum + a [i];printf（数组和数组=％d，sum）;} </ OL>  
<li> #include <stdio.h> </ li>  
<li> main（）</ li>  
<li> int a [10]，i，sum = 0;</ Li>  
<li> printf（输入array \ n）;</ Li>  
<li> for（i = 0; i <10; i ++）</ li>  
<li> {</ li>  
<li> scanf（％d，＆a [i]）;</ Li>  
<li> sum = sum + a [i];</ Li>  
<li> printf（阵列=％d，sum）;</ Li>  
<li>} </ li>  
### 回答 5
这个问题没有指定哪种编程语言。甚至一些像Python和Java这样的常用语言也可以用几行进行。  
Python：  
<ol> num_list = [1,2,3,4,5,6,7,8,9,10] sum_value = sum（num_list）打印（sum_value）</ ol>  
<li> num_list = [1,2,3,4,5,6,7,8,9,10] </ li>  
<li> sum_value = sum（num_list）</ li>  
<li>打印（sum_value）</ li>  
Java：  
<ol> //包含java.util。*列表<整数> numlist = arrays.aslist（1,2,3,4,5,6,7,8,9,10）;Integer sumvalue = numlist.stream（）。maptoint（整数:: intvalue）.sum（）;system.out.println（sumvalue）;</ OL>  
<li> //包括java.util。* </ li>  
<li>列表<整数> numlist = arrays.aslist（1,2,3,4,5,6,7,8,9,10）;</ Li>  
<li>整数sumvalue = numlist.stream（）。MapToint（Integer :: Intvalue）.sum（）;</ Li>  
<li> system.out.println（sumvalue）;</ Li>  
### 回答 6
您没有在此处指定语言在这里是perl6。  
<OL>说总和提示（）XX 10; </ OL>  
<li>说总和提示（）xx 10; </ Li>  
老实说，我会使它成为它接受任何数量的输入行。  
<ol>说行。 </ OL>  
<li>说线路。 </ Li>  
如果一行中有多个号码，那么这两个都会失败，所以这里是拆分空白的代码。  
<ol>说单词.sum; </ OL>  
<li>说单词.sum; </ Li>  
也许你想检查所有这些在找到总和之前是数字，而且它们的恰好有10个。哦，这是第一个实际使用数组的人。  
<ol> catch {默认{注意'输入必须是10个数字';退出1; ＃11最小的数字大于10.＃（防止它更多内存</ ol>  
<li> catch {默认{</ li>  
<li>注意'输入必须是10个数字'; </ Li>  
<li>退出1; </ Li>  
<li>}} </ li>  
<Li>＃11是大于10的最小数字。</ li>  
<li>＃（防止它使用更多内存</ li>  
您没有在此处指定语言在这里是perl6。  
<OL>说总和提示（）XX 10; </ OL>  
<li>说总和提示（）xx 10; </ Li>  
老实说，我会使它成为它接受任何数量的输入行。  
<ol>说行。 </ OL>  
<li>说线路。 </ Li>  
如果一行中有多个号码，那么这两个都会失败，所以这里是拆分空白的代码。  
<ol>说单词.sum; </ OL>  
<li>说单词.sum; </ Li>  
也许你想检查所有这些在找到总和之前是数字，而且它们的恰好有10个。哦，这是第一个实际使用数组的人。  
<ol> catch {默认{注意'输入必须是10个数字';退出1; ＃11是大于10的最小数字。＃（防止它更多的内存小于必要的＃如果有超过10个数字。）我的数字@numbers = words.head（11）»。数字;数字;数字;数字;数字;数字;如果@numbers≠10; ＃9≠10和11≠10说@ numbers.sum; </ OL>  
<li> catch {默认{</ li>  
<li>注意'输入必须是10个数字'; </ Li>  
<li>退出1; </ Li>  
<li>}} </ li>  
<Li>＃11是大于10的最小数字。</ li>  
<li>＃（防止它使用比必要的更多内存</ li>  
<li>＃如果有超过10个数字。）</ li>  
<li>我的数字@ nnumbers = words.head（11）»。数字; </ Li>  
<li>如果@numbers≠10死亡; ＃9≠10和11≠10</ li>  
<li>说@ numbers.sum; </ Li>  
### 回答 7
使用for-epour循环而不是指向索引以快速执行执行  
公共类拉姆{  
公共静态void main（String [] args）{  
int sum = 0;  
int ar [] =新int [10];  
system.out.println（输入数据:);  
Scanner SC = New Scanner（System.in）;  
for（int i = 0; i <10; ++ i）  
AR [i] = sc.nextint（）;  
for（int i：ar）  
总和= sum + i;  
system.out.println（Sum）;  
}  
### 回答 8
对不起，Quora没有做作业......  
### 回答 9
这个问题似乎是自己的答案。该程序只缺少名称。  
这只是许多程序员不会在数组中存储输入数字，因为维护总和并计数足以计算平均值。  
### 回答 10
在这里，您是因素：  
<OL> 0 10 [READLN String> Number +]时间。 </ OL>  
<li> 0 10 [readln String> number +]时间。 </ Li>  
虽然这不存储数组中的数字。这样做有点愚蠢，因为你不需要做到这一款，它浪费了内存，所以如果这是你已经设置的一个例子，你可以考虑你的老师被我勾选。  
但如果您必须将其存储在数组中：  
<OL> 10 [READLN String> Number]复制总和。 </ OL>  
<li> 10 [readln String> number]复制总和。 </ Li>  
但更严重的是，我希望你的意思是C ++。在这种情况下，答案显然  
<OL>使用命名空间std; int main（int argc，char * argv []）{vector <int>测试（10）;生成（test.begin（），test.end（），[]（）{int </ ol>  
使用命名空间std; </ Li>  
<li> </ li>  
<li> int main（int argc，char * argv []）{</ li>  
<li>矢量<int>测试（10）; </ Li>  
<li>生成（test.begin（），test.end（），</ li>  
<li> []（）{int </ li>  
在这里，您是因素：  
<OL> 0 10 [READLN String> Number +]时间。 </ OL>  
<li> 0 10 [readln String> number +]时间。 </ Li>  
虽然这不存储数组中的数字。这样做有点愚蠢，因为你不需要做到这一款，它浪费了内存，所以如果这是你已经设置的一个例子，你可以考虑你的老师被我勾选。  
但如果您必须将其存储在数组中：  
<OL> 10 [READLN String> Number]复制总和。 </ OL>  
<li> 10 [readln String> number]复制总和。 </ Li>  
但更严重的是，我希望你的意思是C ++。在这种情况下，答案显然  
<OL>使用命名空间std; int main（int argc，char * argv []）{vector <int>测试（10）;生成（test.begin（），test.end（），[]（）{int a; cin >> a;返回一个;}）; cout <<累积（test.begin（），test.end（），0）; } </ OL>  
使用命名空间std; </ Li>  
<li> </ li>  
<li> int main（int argc，char * argv []）{</ li>  
<li>矢量<int>测试（10）; </ Li>  
<li>生成（test.begin（），test.end（），</ li>  
<li> []（）{int a; CIN >> a;返回一个;}）; </ Li>  
<li> cout <<累积（test.begin（），test.end（），0）; </ Li>  
<li>} </ li>  
编辑。哦，让我们不要忘记python：  
<OL>打印（SUM（[int（输入（输入（输入（输入（输入（输入（输入（输入（输入（输入））（10）]））））</ ol>  
<li>打印（sum（[int（输入（输入（输入（输入（输入（输入（输入（输入（输入（输入））（10）]）））））</ li>  
和Java。  
<ol>公共课堂夏季{公共静态void main（String [] args）{scanner s = new scanner（system.in）; system.out.println（Intstream.generate（s :: nextint）.limit（10）.sum（））; }} </ OL>  
<li>公共班级夏天{</ li>  
<li>公共静态void main（String [] args）{</ li>  
<li>扫描仪s =新扫描仪（system.in）; </ Li>  
<li> system.out.println（Intstream.generate（s :: nextint）</ li>  
<li> .limit（10）.sum（））; </ Li>  
<li>} </ li>  
### 回答 11
您可以使用“for”或'foreach'循环来加入数组中的所有元素并找到它们的总和。这是Java中的一个例子。  
<ol>公共静态int findsum（int [] array）{int temp = 0;for（int x = 0; x <array.length; x ++）{temp + = array [x];} return temp;} </ OL>  
<li>公共静态int findsum（int [] array）{</ li>  
<li> int temp = 0;</ Li>  
<li> for（int x = 0; x <array.length; x ++）{</ li>  
<li> temp + = array [x];</ Li>  
<li>返回温度;</ Li>  
<li>} </ li>  
### 回答 12
您应该指定了您希望答案的语言.Anyways这是C中的代码。  
#include <stdio.h>  
void main（）  
int a [10]，i，sum = 0;  
scanf（％d，＆a [i]）;  
for（i = 0; i <10; i ++）  
{  
总和+ = [i];  
printf（％d，sum）;  
}  
### 回答 13
/ *假设你想要C * /中的答案  
#include <stdio.h>  
#include <stdlib.h>  
int arraysum（int myArray []，int size）  
{int sum = 0;  
for（int i = 0; i <size; i ++）  
{sum = sum + myArray [i];} / *可以写入sum + = myArray [i] * /  
退货;  
}  
int main（）  
int mynumberarray [10] =;  
for（i = 0; i <10; i ++）  
{scanf（％d，＆mynumberarray [i]）;}  
int sum_array = arraysum（mynumberarray，6）;  
printf（总和是％d \ n，sum_array）;}  
返回0;  
}  
/ *您必须想知道为什么我担任函数。对。实际上采用功能简化了主要的代码* /  
### 回答 14
#include <stdio.h>  
漂浮普通（浮子元素[]）;  
浮法添加（浮子元素[]）;  
int main（）  
{  
int sum;  
Float AVG，元素[] = {23,55,22,3,4,18,23,45,56,67};  
avg =平均（元素）;//只有数组的名称被传递为参数  
总和=加法（元素）;  
printf（sum元素=％d \ n，sum）;  
printf（平均元素=％f，avg）;  
返回0;  
}  
浮法平均值（浮动元素[]）  
{  
INT I;  
浮动AVG，SUM = 0.0;  
for（i = 0; i <10; ++ i）{  
sum + =元素[i];  
AVG =（SUM / 10）;  
返回avg;  
}  
浮法添加（浮动元素[]）  
{  
int sum = 0，i;  
for（i = 0; i <10; i ++）  
sum = sum +元素[i];  
退货;  
}  
### 回答 15
主要的（）  
int x [10];  
INT I，SUM = 0;  
for（i = 0; i <= 9; i ++）  
{  
printf（输入否）;  
scanf（％d，＆a [i]）;  
总和= sum + a [i];  
printf（％d，sum）;  
}  
### 回答 16
<ol>＃python a_list，q = []，0，而q <10：try：a_number = float（输入（写一个数字:)）a_list.append（a_number）q + = 1除ValueError之外：print（f {a_number不是一个数字。\再试一次！）打印（fsum是{sum（a_list）}）</ ol>  
<li>＃python </ li>  
<li> a_list，q = []，0 </ li>  
<li> q <10：</ li>  
<li>尝试：</ li>  
<li> a_number = float（输入（写一个数字:)）</ li>  
<li> a_list.append（a_number）</ li>  
<li> q + = 1 </ li>  
<li>除ValueError之外：</ li>  
<li>打印（f {a_number}不是数字。\再试一次！）</ li>  
<li>打印（fsum是{sum（a_list）}）</ li>  
### 回答 17
你坐在电脑上，打开选择的编辑，开始打字。你又怎么写一个计划？  
但是你可能会要求一个例子。在C ++中，  
<ol>模板<class chart，class elem，std :: size_t n> std :: basic_istream <chart>＆operator >>（std :: basic_istream <chart>＆is，std :: array <elem，n>＆a）{for （汽车和elem：a）是>> elem;返回是; } int main（）{std :: array <int，10> a; std :: cin >> a;自动= std ::累积（a.begin（），a.end（），0）; } </ OL>  
<li>模板<class chart，class elem，std :: size_t n> </ li>  
<li> std :: basic_istream <chart>＆operator >>（std :: basic_istream <chart>＆is，</ li>  
<li> std :: array <Elem，n>＆a）{</ li>  
<li>（auto＆Elem：a）是>> elem; </ Li>  
<li>返回是; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> int main（）{</ li>  
<li> std :: Array <int，10> a; </ Li>  
<li> std :: cin >> a; </ Li>  
<li>自动um = std ::累积（a.begin（），a.end（），0）; </ Li>  
<li>} </ li>  
### 回答 18
在C.  
<ol> #include <stdio.h> #include <stdlib.h> #include <time.h> #define rep（x，v）for（size_t x = 0; x <sizeof（v）/ sizeof（v [ 0]）; ++ x）int main（void）{srand（时间（null））; int a [10]; rep（i，a）a [i] =（rand（）＆0xf）+1;长= 0; rep（i，a）sum + = a [i]; rep（i，a）printf（a [％zu] =％d，，i，a [i]）; printf（\ nsum =％ld \ n，sum）; } </ OL>  
<li> #include <stdio.h> </ li>  
<li> #include <stdlib.h> </ li>  
<li> #include <time.h> </ li>  
<li> #define rep（x，v）for（size_t x = 0; x <sizeof（v）/ sizeof（v [0]）; ++ x）</ li>  
<li> int main（void）{</ li>  
<li> srand（时间（null））; </ Li>  
<li> int a [10]; </ Li>  
<li> rep（i，a）a [i] =（rand（）＆0xf）+1; </ Li>  
<li> long sum = 0; </ Li>  
<li> rep（i，a）sum + = a [i]; </ Li>  
<li> </ li>  
<li> rep（i，a）printf（a [％zu] =％d，，i，a [i]）; </ Li>  
<li> printf（\ nsum =％ld \ n，sum）; </ Li>  
<li>} </ li>  
编译和运行：  
<ol >> cc -o3 -funroll-all-loops -march = native -o sum10 sum10.c> ./sum10 a [0] = 6，a [1] = 15，a [2] = 6，a [ 3] = 8，a [4] = 14，a [5] = 4，a [6] = 9，a [7] = 11，a [8] = 5，a [9] = 3，sum = 81 </ OL>  
<li >> cc -o3 -funroll-all-loops -march = native -o sum10 sum10.c </ li>  
<li >> ./sum10 </ li>  
<Li> A [0] = 6，A [1] = 15，[2] = 6，a [3] = 8，a [4] = 14，a [5] = 4，a [6] =参照图9，a [7] = 11，a [8] = 5，a [9] = 3，</ li>  
<li> sum = 81 </ li>  
在Lua，由Metables  
<ol>＃！/ usr / bin / env luajit math.randomseed（os.clock（）* os.time（））local a = setometable（{}，{__index = function </ ol>  
<li>＃！/ usr / bin / env luajit </ li>  
<li> math.randomseed（os.clock（）* os.time（））</ li>  
<li>本地a = ettometable（{}，</ li>  
<li> {__Index =函数</ li>  
在C.  
<ol> #include <stdio.h> #include <stdlib.h> #include <time.h> #define rep（x，v）for（size_t x = 0; x <sizeof（v）/ sizeof（v [ 0]）; ++ x）int main（void）{srand（时间（null））; int a [10]; rep（i，a）a [i] =（rand（）＆0xf）+1;长= 0; rep（i，a）sum + = a [i]; rep（i，a）printf（a [％zu] =％d，，i，a [i]）; printf（\ nsum =％ld \ n，sum）; } </ OL>  
<li> #include <stdio.h> </ li>  
<li> #include <stdlib.h> </ li>  
<li> #include <time.h> </ li>  
<li> #define rep（x，v）for（size_t x = 0; x <sizeof（v）/ sizeof（v [0]）; ++ x）</ li>  
<li> int main（void）{</ li>  
<li> srand（时间（null））; </ Li>  
<li> int a [10]; </ Li>  
<li> rep（i，a）a [i] =（rand（）＆0xf）+1; </ Li>  
<li> long sum = 0; </ Li>  
<li> rep（i，a）sum + = a [i]; </ Li>  
<li> </ li>  
<li> rep（i，a）printf（a [％zu] =％d，，i，a [i]）; </ Li>  
<li> printf（\ nsum =％ld \ n，sum）; </ Li>  
<li>} </ li>  
编译和运行：  
<ol >> cc -o3 -funroll-all-loops -march = native -o sum10 sum10.c> ./sum10 a [0] = 6，a [1] = 15，a [2] = 6，a [ 3] = 8，a [4] = 14，a [5] = 4，a [6] = 9，a [7] = 11，a [8] = 5，a [9] = 3，sum = 81 </ OL>  
<li >> cc -o3 -funroll-all-loops -march = native -o sum10 sum10.c </ li>  
<li >> ./sum10 </ li>  
<Li> A [0] = 6，A [1] = 15，[2] = 6，a [3] = 8，a [4] = 14，a [5] = 4，a [6] =参照图9，a [7] = 11，a [8] = 5，a [9] = 3，</ li>  
<li> sum = 81 </ li>  
在Lua，由Metables  
<ol>＃！/ usr / bin / env luajit math.randomseed（os.clock（）* os.time（））本地a = ettometable（{}，{__index =函数（t，i）返回getmetapable（t） [i]结束，sum =函数（t）本地SUM = 0对于i = 1，＃t do sum = sum + t [i]结束返回和结束，out =函数（t）return {..table.concat（ t ,,）。 TONUMBER（arg [1]）或10）打印（a：out（））io.write（sum =，a：sum（），\ n）</ ol>  
<li>＃！/ usr / bin / env luajit </ li>  
<li> math.randomseed（os.clock（）* os.time（））</ li>  
<li>本地a = ettometable（{}，</ li>  
<li> {__Index =函数（t，i）返回getmetapable（t）[i]结束，</ li>  
<li> sum =函数（t）本地SUM = 0对于i = 1，＃t do sum = sum + t [i]结束返回和结束，</ li>  
<li> out =函数（t）return {.. .. table.concat（t，）。}结束，</ li>  
<li> init = for i = 1的函数（t，n），n do t [i] = math.random（10）结束返回t结束</ li>  
<li>}）</ li>  
<Li> A：init（arg [1]和tonumber（arg [1]）或10）</ li>  
<li>打印（A：Out（））</ li>  
<li> io.write（sum =，a：sum（），\ n）</ li>  
执行  
<OL >> CHMOD + X SUM10.LUA>。/ SUM10.LUA 10 {5,4,7,3,9,5,8,6,2,19,5,8,6,2,1} SUM = 50 </ OL>  
<li >> chmod + x sum10.lua </ li>  
<li >> ./sum10.lua 10 </ li>  
<Li> {5,4,7,3,9,5,8,6,2,1} </ li>  
<li> sum = 50 </ li>  
### 回答 19
如何编写一个程序以输入10个数字，并查找其总和？  
我打开一个文本编辑器，我键入：  
<ol> n = 9打印（sum（list（范围（n + 1）））==（如果n <0 else（n // 2）*（n + 1），如果n％2 == 0 ever n*（（n + 1）// 2）））</ OL>  
<li> n = 9 </ li>  
<li>打印（sum（list（范围（n + 1）））==（如果n <0 else（n // 2）*（n + 1），如果n％2 == 0 else n *（（n + 1）// 2）））</ li>  
并将其安全为trueprinter.py  
最后，我在这个文件的文件夹中打开一个终端：  
<ol> python trueprinter.py </ ol>  
<li> python trueprinter.py </ li>  
这将是真的  
我确信这个计划满足了次要人。我生成长度10的数组（[0,1，...，9]）并计算其总和。  
### 回答 20
以下代码可以帮助您编写上述程序：  
它的产出是：  
### 回答 21
您可以在Python中如下所示：  
<ol> a = 1结果= 0对于范围（10）：y = int（输入（请输入号码{0}：.format（a）））结果+ = y a + = 1打印（结果输入的10个数字是：，结果）</ ol>  
<li> a = 1 </ li>  
<li>结果= 0 </ li>  
<li>在范围内（10）：</ li>  
<li> y = int（输入（请输入号码{0}：.format（a）））</ li>  
<li>结果+ = y </ li>  
<li> a + = 1 </ li>  
<li>打印（输入的10个号码的结果是：，结果）</ li>  
### 回答 22
％MATLAB代码，用于数组的总和  
凭借全能的恩典，此代码为所有数组提供了正确的答案。  
arr =输入（请输入array）  
asize =尺寸（arr）  
总和= 0;  
对于i = 1：asize（2）  
SUM = SUM + ARR（i）;  
坚定  
printf（总和是:);  
DISP（总和）  
### 回答 23
<ol> #include <stdio.h>你main（）{intarray [10];你总和= 0，我;for（i = 0; i <10; i ++）{printf（输入号码:);scanf（％d，＆intarray [s]）;总和+ = intarray [i];printf（总计％d \ n，sum）;返回0;} </ OL>  
<li> #include <stdio.h> </ li>  
<li>你是main（）{</ li>  
<那个>你的intarray [10];</ Li>  
<li>你总和= 0，i;</ Li>  
<li> </ li>  
<li> for（i = 0; i <10; i ++）{</ li>  
<li> printf（输入号码:);</ Li>  
<li> scanf（％d，＆intarray [s]）;</ Li>  
<li> sum + = intarray [i];</ Li>  
<li>} </ li>  
<li> printf（总计％d \ n，sum）;</ Li>  
<li> </ li>  
<li>返回0;</ Li>  
<li>} </ li>  
### 回答 24
int main（无效）  
int arr [10]，我，sum = 0;  
scanf（％d，＆arr [i]）  
for（i = 0; i <10; i ++）  
{  
sum + = arr [i];  
printf（％d，sum）  
返回0;  
}  
### 回答 25
这是我用C语言编写的一个例子......您可以使用任何语言中的算法  
int sum = 0，i，arr [9];  
for（i = 0; i <10; i ++）{  
扫描（％d，＆arr [i]）;  
sum + = arr [i];  
}  
### 回答 26
由于您可能正在使用Python，这是Python版本：此外，下次指定语言。^^  
总和= 0.  
对于I系列（0,10）：  
num =输入（输入数字:)  
SUM + = num  
打印（总和是+ str（和）  
### 回答 27
这是用c中写的例子。它使用一些明显命名的函数来使其容易遵循代码的情况而不使用大量注释。  
<ol> #include <stdio.h> #include <stdlib.h> #define max_len 10 void promptorfornumbers（int a []，int len）{int index; for（index = 0; index <max_len; index ++）{printf（输入整数％d％d的％d：，（索引+ 1），max_len）; scanf（％d，＆a [index]）; } int getsum（int a []，int len）{int runningsum = 0; int索引; for（index = 0; index <len; index ++）{runningsum + = a [index];返回runningsum;浮动getav </ ol>  
<li> #include <stdio.h> </ li>  
<li> #include <stdlib.h> </ li>  
<li> #define max_len 10 </ li>  
<li> </ li>  
<li> void promptorfornumbers（int a []，int len）</ li>  
<li> {</ li>  
<li> int索引; </ Li>  
<li> for（index = 0; index <max_len; index ++）{</ li>  
<li> printf（输入整数％d％d：，（索引+ 1），max_len）; </ Li>  
<li> scanf（％d，＆a [index]）; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> int getsum（int a []，int len）</ li>  
<li> {</ li>  
<li> int runningsum = 0; </ Li>  
<li> int索引; </ Li>  
<li> for（index = 0; index <len; index ++）{</ li>  
<li> runningsum + = a [index]; </ Li>  
<li>返回runningsum; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> float getav </ li>  
这是用c中写的例子。它使用一些明显命名的函数来使其容易遵循代码的情况而不使用大量注释。  
<ol> #include <stdio.h> #include <stdlib.h> #define max_len 10 void promptorfornumbers（int a []，int len）{int index; for（index = 0; index <max_len; index ++）{printf（输入整数％d％d的％d：，（索引+ 1），max_len）; scanf（％d，＆a [index]）; } int getsum（int a []，int len）{int runningsum = 0; int索引; for（index = 0; index <len; index ++）{runningsum + = a [index];返回runningsum; float getaverage（int a []，int len）{return getsum（a，len）* 1.0f / len; } int main（）{int numbers [max_len];提示棘手（数字，max_len）; printf（平均：％f，sum：％d \ n，getaverage（numbers，max_len），getsum（数字，max_len））;返回0; } </ OL>  
<li> #include <stdio.h> </ li>  
<li> #include <stdlib.h> </ li>  
<li> #define max_len 10 </ li>  
<li> </ li>  
<li> void promptorfornumbers（int a []，int len）</ li>  
<li> {</ li>  
<li> int索引; </ Li>  
<li> for（index = 0; index <max_len; index ++）{</ li>  
<li> printf（输入整数％d％d：，（索引+ 1），max_len）; </ Li>  
<li> scanf（％d，＆a [index]）; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> int getsum（int a []，int len）</ li>  
<li> {</ li>  
<li> int runningsum = 0; </ Li>  
<li> int索引; </ Li>  
<li> for（index = 0; index <len; index ++）{</ li>  
<li> runningsum + = a [index]; </ Li>  
<li>返回runningsum; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> float getaverage（int a []，int len）</ li>  
<li> {</ li>  
<li>返回getsum（a，len）* 1.0f / len; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int数字[max_len]; </ Li>  
<li> promptorfornumbers（数字，max_len）; </ Li>  
<li> printf（平均：％f，sum：％d \ n，getaverage（numbers，max_len），getsum（数字，max_len））; </ Li>  
<li>返回0; </ Li>  
<li>} </ li>  
如果问题没有要求阵列，则我不会使用一个，因为可以计算总和作为用户输入数字，并且平均值只是SUM / LENGLE。没有阵列，程序使用的内存将是恒定的而不是线性相对于数字的数量。  
有许多其他方法可以编写程序：  
### 回答 28
这是两种方式 -   
<ol> main（）{int sum = 0; int n = 10;而（n--）{int x; scanf（％d，＆x）; sum = sum + x; printf（％d，sum）; } </ OL>  
<li> main（）</ li>  
<li> int sum = 0; </ Li>  
<li> int n = 10; </ Li>  
<li> while（n--）</ li>  
<li> {</ li>  
<li> int x; </ Li>  
<li> scanf（％d，＆x）; </ Li>  
<li> sum = sum + x; </ Li>  
<li> printf（％d，sum）; </ Li>  
<li>} </ li>  
这里，循环已被使用而不是使用阵列。  
循环执行10次以进行输入。  
2.使用goto命令  
<ol> main（）{int i = 1，sum = 0;输入：int x; scanf（％d，＆x）; I ++; sum = sum + x;如果（i <= 10）转到输入; printf（％d，sum）; } </ OL>  
<li> main（）</ li>  
<li> {</ li>  
<li> int i = 1，sum = 0; </ Li>  
<li>输入：</ li>  
<li> int x; </ Li>  
<li> scanf（％d，＆x）; </ Li>  
<li> i ++; </ Li>  
<li> sum = sum + x; </ Li>  
<li> if（i <= 10）</ li>  
<li> goto输入; </ Li>  
<li> printf（％d，sum）; </ Li>  
<li>} </ li>  
### 回答 29
您的意思是输入10个数字，然后打印总和。让我们去编码......：  
<ol>导入java.util.scanner;公共类主{公共静态void main（String args []）{扫描仪输入=新扫描仪（System.in）; int sum = 0; for（int i = 0; i <10; i + = 1）{sum + = input.nextint（）; system.out.println（总和是：+和）; }} </ OL>  
<li>导入java.util.scanner; </ Li>  
<li>公共类主要{</ li>  
<li>公共静态void main（String args []）{</ li>  
<li>扫描仪输入=新扫描仪（System.in）; </ Li>  
<li> int sum = 0; </ Li>  
<li> for（int i = 0; i <10; i + = 1）{</ li>  
<li> sum + = input.nextint（）; </ Li>  
<li> system.out.println（总和是：+和）; </ Li>  
<li>} </ li>  
第一行，导入输入扫描仪：慢慢拍摄输入但简单。第二和第三行，类和主要方法描述。第四行，创建扫描仪的实例（准备拍摄输入）。第五行，将变量初始化为零，所以我们可以  
您的意思是输入10个数字，然后打印总和。让我们去编码......：  
<ol>导入java.util.scanner;公共类主{公共静态void main（String args []）{扫描仪输入=新扫描仪（System.in）; int sum = 0; for（int i = 0; i <10; i + = 1）{sum + = input.nextint（）; system.out.println（总和是：+和）; }} </ OL>  
<li>导入java.util.scanner; </ Li>  
<li>公共类主要{</ li>  
<li>公共静态void main（String args []）{</ li>  
<li>扫描仪输入=新扫描仪（System.in）; </ Li>  
<li> int sum = 0; </ Li>  
<li> for（int i = 0; i <10; i + = 1）{</ li>  
<li> sum + = input.nextint（）; </ Li>  
<li> system.out.println（总和是：+和）; </ Li>  
<li>} </ li>  
第一行，导入输入扫描仪：慢慢拍摄输入但简单。第二和第三行，类和主要方法描述。第四行，创建扫描仪的实例（准备拍摄输入）。第五行，将变量初始化为零，以便我们可以将所有即将到来的整数汇总到此变量中。第六行，运行十次。第七行，取消并将其添加到和变量。第九行最后打印到控制台。  
你完成了！ :)  
### 回答 30
我可以 …  
在C ++中，写入此类程序的代码如下：  
#include <iostream>  
#include <iomanip>  
使用命名空间std;  
int main（）  
int arr [5];  
for（int i = 0; i <5; i ++）  
{  
CIN >> ARR [I];  
}  
COUT <<您输入的号码是：<< endl;  
for（int i = 0; i <5; i ++）  
{  
cout << arr [i] << endl;  
}  
### 回答 31
Python代码：  
<ol> user_input = [输入（输入值:)范围（10）] </ ol>  
<li> user_input = [输入（输入值:)为范围（10）] </ li>  
示例输出：  
C代码：  
#include <stdio.h>  
int main（）  
{  
int a [10]; INT I; int bylest;  
printf（输入十个值:);  
//在数组中存储10个数字  
for（i = 0; i <10; i ++）{  
scanf（％d，＆a [i]）;  
}  
示例输出：  
输入十个值：1 2 3 4 5 6 7 8 9 10  
C＃尖锐代码：  
<OL>使用系统;公共类练习4 {公共静态void main（）{int i，n，sum = 0;双平均值; console.write（输入10号：\ n）; for（i = 1; i <= 10; i ++）{console.write（numbers- {0}：，i）; n = convert.toint32（console.readline（））; }}} </ ol>  
使用系统<li> </ Li>  
<li>公共阶级练习4 </ li>  
<li>公共静态void main（）</ li>  
<li> {</ li>  
<li> int i，n，sum = 0; </ Li>  
<li>双重平均值; </ Li>  
<li> console.write（输入10个数字：\ n）; </ Li>  
<li>（i = 1; i <= 10; i ++）</ li>  
<li> {</ li>  
<li> console.write（numbers- {0}：，i）; </ Li>  
<li> n = convert.toint32（console.readline（））; </ Li>  
<li>} </ li>  
样本  
Python代码：  
<ol> user_input = [输入（输入值:)范围（10）] </ ol>  
<li> user_input = [输入（输入值:)为范围（10）] </ li>  
示例输出：  
C代码：  
#include <stdio.h>  
int main（）  
{  
int a [10]; INT I; int bylest;  
printf（输入十个值:);  
//在数组中存储10个数字  
for（i = 0; i <10; i ++）{  
scanf（％d，＆a [i]）;  
}  
示例输出：  
输入十个值：1 2 3 4 5 6 7 8 9 10  
C＃尖锐代码：  
<OL>使用系统;公共类练习4 {公共静态void main（）{int i，n，sum = 0;双平均值; console.write（输入10号：\ n）; for（i = 1; i <= 10; i ++）{console.write（numbers- {0}：，i）; n = convert.toint32（console.readline（））; }}} </ ol>  
使用系统<li> </ Li>  
<li>公共阶级练习4 </ li>  
<li>公共静态void main（）</ li>  
<li> {</ li>  
<li> int i，n，sum = 0; </ Li>  
<li>双重平均值; </ Li>  
<li> console.write（输入10个数字：\ n）; </ Li>  
<li>（i = 1; i <= 10; i ++）</ li>  
<li> {</ li>  
<li> console.write（numbers- {0}：，i）; </ Li>  
<li> n = convert.toint32（console.readline（））; </ Li>  
<li>} </ li>  
示例输出：  
<OL>输入10个数字：数字-1：2号2：4号 -  3：6号 -  4：8号-5：10号 -  6：12号-7：14号码-8：16 Number-9：18号 -  10：20 </ OL>  
<li>输入10个数字：</ li>  
<li>数字-1：2 </ li>  
<li>数字-2：4 </ li>  
<li>数字-3：6 </ li>  
<li>数字-4：8 </ li>  
<li>数字-5：10 </ li>  
<li>数字-6：12 </ li>  
<li>数字-7：14 </ li>  
<li>号码-8：16 </ li>  
<li>数字-9：18 </ li>  
<li>数字-10：20 </ li>  
### 回答 32
你好，  
要将输入到数组中，您需要具有有关循环的知识。您也可以在不使用循环的情况下取出输入。假设您需要将3个整数作为输入。只需查看以下代码。 （我正在使用c ++语言。）  
使用命名空间std <ol> #include <iostream> int main（）{int ara [10]; // IVE声明了一个大小10 cin >> ARA [0]; //拍摄输入第一整数CIN >> ARA [1]; //拍摄输入第二个整数CIN >> ARA [2]; ////拍摄输入第三整数返回0; } </ OL>  
<li> #include <iostream> </ li>  
使用命名空间std; </ Li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int ara [10]; // IVE声明了大小10 </ li>的数组  
<li> cin >> ARA [0]; //拍摄了第一个整数</ li>  
<Li> Cin >> ARA [1]; //拍摄了第二个整数</ li>  
<li> cin >> ARA [2]; ////拍摄了第三个整数</ li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
现在，如果你想拿10个整数，你可以写入10行Cin >>。但如果你需要更多地需要更多的tha怎么办  
你好，  
要将输入到数组中，您需要具有有关循环的知识。您也可以在不使用循环的情况下取出输入。假设您需要将3个整数作为输入。只需查看以下代码。 （我正在使用c ++语言。）  
使用命名空间std <ol> #include <iostream> int main（）{int ara [10]; // IVE声明了一个大小10 cin >> ARA [0]; //拍摄输入第一整数CIN >> ARA [1]; //拍摄输入第二个整数CIN >> ARA [2]; ////拍摄输入第三整数返回0; } </ OL>  
<li> #include <iostream> </ li>  
使用命名空间std; </ Li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int ara [10]; // IVE声明了大小10 </ li>的数组  
<li> cin >> ARA [0]; //拍摄了第一个整数</ li>  
<Li> Cin >> ARA [1]; //拍摄了第二个整数</ li>  
<li> cin >> ARA [2]; ////拍摄了第三个整数</ li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
现在，如果你想拿10个整数，你可以写入10行Cin >>。但是，如果您需要超过10 ^ 6或更多的整数，那么怎么样。如果你愿意，你可以写入10 ^ 6行CIN >>，但你可能很容易假设它会非常痛苦。  
因此，这是我们需要使用循环的原因之一，以将输入划入阵列。  
现在，问题是循环。根据Whatis.com的定义，  
在计算机编程中，循环是一系列指令，该指令在达到某个条件之前不断重复。  
查看以下代码。  
使用命名空间std <ol> #include <iostream> int main（）{int ara [10]; for（int i = 0; i <10; i ++）{CIN >> ARA [I];返回0; } </ OL>  
<li> #include <iostream> </ li>  
使用命名空间std; </ Li>  
<li> int main（）</ li>  
<li> int ara [10]; </ Li>  
<li> </ li>  
<li> for（int i = 0; i <10; i ++）</ li>  
<li> {</ li>  
<li> cin >> ARA [i]; </ Li>  
<li> </ li>  
<li>返回0; </ Li>  
<li>} </ li>  
在第8行，我正在使用c ++语言的循环。我想你已经注意到了循环中有三个部分。 I变量用于更改阵列ARA的索引。  
摘要是，此循环将从值I = 0开始。然后它会检查条件（i <10）。由于0 <10所以，它将占据ARA [I]的输入，这意味着ARA [0]。  
然后，我的新值是i = i + 1，即i = 1 + 1 = 2。然后它会检查条件（i <10）。由于，2 <10所以，它将取得一个输入ARA [I]，这意味着ARA [2]。  
然后，我的新值将是i = i + 1，即i = 2 + 1 = 3。然后它会检查条件（i <10）。由于3 <10所以，它将取得一个进入ARA [I]，这意味着ARA [3]。  
它会继续......然后在i = 9之后，我的新值将是i = i + 1，即i = 9 + 1 = 10。然后它会检查条件（i <10）。由于10不小于10.因此，它会破坏循环。  
现在，如果您想显示阵列ARA的输出只需复制整个循环和粘贴并替换CIN >> ARA [I]与COUT << ARA [i]（别忘了键入分号）完成工作！ ：D.  
我希望你能理解。要知道有关循环的详细信息，请谷歌它。在那里，您将找到许多关于使用循环的参考。  
谢谢！祝你今天过得愉快！ :)  
### 回答 33
<ol> java.util导入。*;公共类解决方案{公共静态void main（String [] args）{scanner sc = new scanner（system.in）你是史塔[] =新你[10];for（你= 0; i <10; i ++）Intar [i] = sc.nextint（）;for（你= 0; i <10; i ++）system.out.println（Intar [i]）;}} </ OL>  
<li>导入java.util。*;</ Li>  
<li>公共类解决方案{</ li>  
<li> </ li>  
<lik>公共静态void main（String [] args）{</ li>  
<li> scanner sc = new scanner（system.in）;</ Li>  
<那个>你是Intharmed [] =新你[10];</ Li>  
<li> intarar [s] = sc.nextint（）;</ Li>  
<li>（你是= 0; i <10; i ++）</ li>  
<li> system.aut.println（Intar [S]）;</ Li>  
<li>} </ li>  
### 回答 34
您在C / C ++主题区域输入了此问题时，我将假设您需要C / C ++中的答案。  
我强烈建议您了解每一行的基础知识而不是复制以下代码。  
int main（）{  
//创建一个10个整数数组  
int a [10];  
// initialise一个int变量以从用户暂时存储数字  
int num;  
//遍历10次使用for循环要求用户输入数字  
for（int i = 0; i <10; i ++）{  
//从标准IO获取输入并将其存储在num的位置  
scanf（％d，num）;  
[i] = num;  
}  
//现在再次使用循环穿过阵列并分配  
您在C / C ++主题区域输入了此问题时，我将假设您需要C / C ++中的答案。  
我强烈建议您了解每一行的基础知识而不是复制以下代码。  
int main（）{  
//创建一个10个整数数组  
int a [10];  
// initialise一个int变量以从用户暂时存储数字  
int num;  
//遍历10次使用for循环要求用户输入数字  
for（int i = 0; i <10; i ++）{  
//从标准IO获取输入并将其存储在num的位置  
scanf（％d，num）;  
[i] = num;  
}  
//现在再次使用For循环遍历阵列并显示元素的数量和地址  
for（int i = 0; i <10; i ++）{  
printf（索引％d的元素为：％d \ n，i，a [i]）;  
printf（索引％d的元素地址为：％p \ n，i和a [i]）;  
//结尾  
}  
这是一个非常原始但是基本解决方案，可以通过更好地使用指针来优化它。  
请记住，需要大量概念来完全理解在代码中发生的情况。  
### 回答 35
首先，用英语定义问题（或无论您的自然语语言发生什么）。特别注意任何可能制作的不那么言名的假设。  
拿10个数字 - 我们谈论一个人被提示为单个号码，连续十次？我们是否希望接受作为单个输入的数字列表？当我们只获得9个数字时会发生什么？当我们得到11时会发生什么？  
来自用户 - 我们是否必须在提示时谈论用户？从文本文件或电子表格中拍摄数字呢？那么使用系统中其他地方派生的数字呢？  
展示他们的总和 - 我们只回到总数吗？我们应该打印收到的数字，然后是他们的总数？  
一旦您完全定义了问题，您应该有一些看起来像伪代码的东西。这是最基本的解释可能是什么样子：  
`重复这十次:(提示用户输入数字，然后存储给定的数字）。计算十个存储的数字的总和。打印计算结果.`  
从那里，你的工作现在是*将*转换为您选择的编程语言。这是Ruby中的一个例子：  
<ol> number_set = [] 10. itfimes dope输入数字number_set << gets.to_f结束总计：puts number_set.inject（＆：+）</ ol>  
<li> number_set = [] </ li>  
<li> 10.Times do </ li>  
<li>放入输入一个数字</ li>  
<li> number_set << gets.to_f </ li>  
<li>结束</ li>  
<li>投入总：</ li>  
<li> puts number_set.inject（＆：+）</ li>  
有办法做到这一点更可读/有效/整洁/好，但这是我们对我们的解决方案的刻录方式相当忠实的翻译。这效果很好，但我们也可以在此方面构建，直到我们的解决方案感觉正确。 （练习和同行评审感觉到的感觉是正确的感觉）。  
奖金：这是一个代码高尔夫解决方案：  
<ol> puts（10.times.map {p输入数字; gets.to_f} .sum）</ ol>  
<li> puts（10.times.map {p输入一个数字; gets.to_f} .sum）</ li>  
### 回答 36
这里是基本的Java程序，如果输入的数字是，例如输入：21,12,14,30,15,10,45,9,6,55：  
导入java.util.scanner;  
公共类inputintegernumaddup {  
公共静态void main（String [] args）{  
扫描仪扫描=新扫描仪（System.in）  
system.out.println（输入号码:);  
int num1 = scan.nextint（）;  
int num2 = scan.nextint（）;  
int num3 = scan.nextint（）;  
int num4 = scan.nextint（）;  
int num5 = scan.nextint（）;  
int num6 = scan.nextint（）;  
int num7 = scan.nextint（）;  
int num8 = scan.nextint（）;  
int num9 = scan.nextint（）;  
int num10 = scan.nextint（）;  
scan.close（）;  
INT = NUM​​1 + NUM2 + NUM3 + NUM4 + NUM5  
+ num6 + num7 + num8 + nu  
这里是基本的Java程序，如果输入的数字是，例如输入：21,12,14,30,15,10,45,9,6,55：  
导入java.util.scanner;  
公共类inputintegernumaddup {  
公共静态void main（String [] args）{  
扫描仪扫描=新扫描仪（System.in）  
system.out.println（输入号码:);  
int num1 = scan.nextint（）;  
int num2 = scan.nextint（）;  
int num3 = scan.nextint（）;  
int num4 = scan.nextint（）;  
int num5 = scan.nextint（）;  
int num6 = scan.nextint（）;  
int num7 = scan.nextint（）;  
int num8 = scan.nextint（）;  
int num9 = scan.nextint（）;  
int num10 = scan.nextint（）;  
scan.close（）;  
INT = NUM​​1 + NUM2 + NUM3 + NUM4 + NUM5  
+ NUM6 + NUM7 + NUM8 + NUM9 + NUM10）;  
//返回num1的总和至num10。  
system.out.println（所有数字的总和是= + +和）;  
}  
/ **  
* 输出：  
*所有数字的总和是= 217  
* /  
或者，您将阵列变量设置为阵列变量，并通过它添加阵列中的所有数字和阵列的打印和。我希望这有帮助。  
### 回答 37
如果您知道数组是什么，还有一个for循环，以及一个if语句，那么你可以轻松完成这个作业问题。在...上下功夫。  
