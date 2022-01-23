---

title: 如何在使用C ++程序中编写DO-WISH循环以将字母从Z显示到A.
date: 2022-01-23T22:08:15+08:00

---




## 如何在使用C ++程序中编写DO-WISH循环以将字母从Z显示到A.  
### 回答 1
请记住，某些字符集不会将字母放在良好的连续块中。例如，还有一些EBCDIC系统。  
所以，我提供了一个便携式代码：  
<ol> #include <iostream> int main（）{do;while（！std ::运算符<<（std :: cout，zyxwvutsrqponmlkjihgfedcba \ n）））;} </ OL>  
<li> #include <iostream> </ li>  
<li> </ li>  
<li> int main（）{</ li>  
<li>做;</ Li>  
<li> while（！</ li>  
<li> std ::运算符<<（std :: cout，</ li>  
<li> zyxwvutsrqponmlkjihgfedcba \ n）</ li>  
<li>）;</ Li>  
<li>} </ li>  
### 回答 2
这将是写这样的代码的合理方式。  
使用命名空间std <ol> #include <iostream>int main（）{char x = a;do {cout << x ++ <<端口;}而（x <= z）;} </ OL>  
<li> #include <iostream> </ li>  
使用命名空间std;</ Li>  
<li> </ li>  
<li> int main（）{</ li>  
<li> char x = a;</ Li>  
<li> do {</ li>  
<li> cout << x ++ << endl;</ Li>  
<li> </ li>  
<li>} while（x <= z）;</ Li>  
<li>} </ li>  
### 回答 3
#include <stdio.h> int main（）{int num，i，ceface = 1; printf（输入号码\ n）; scanf（％d，＆num）; i = numwhille（i> = 1）{事实=事实* i; i  - ;} printf（给定的数字％d的阶乘为％d \ n，num，事实）;返回0;}  
### 回答 4
<ol> #include <stdio.h> #include <stdlib.h> int main（）{float celsius，华氏温度;Printf（\ inter温度在摄氏度：）;scanf（％f，＆celsius）;Fahrenheit =（1.8）*摄氏+ 32;printf（\ n％f deg celsius是％f fahrenheit \ n，摄氏，华氏素）;返回0;} </ OL>  
<li> #include <stdio.h> </ li>  
<li> #include <stdlib.h> </ li>  
<li> int main（）</ li>  
<li> {</ li>  
<li>浮子摄氏，华氏温度;</ Li>  
<Li> Printf（Celsius的脑温度：）;</ Li>  
<li> scanf（％f，celsius）;</ Li>  
<Li> Fahrenheit =（1.8）*摄氏+ 32;</ Li>  
<li> printf（\ n％f deg celsius是％f fahrenheit \ n，摄氏度，华氏体）;</ Li>  
<li>返回0;</ Li>  
<li>} </ li>  
### 回答 5
<ol> #include <stdio.h> int main（）{char temp = a;printf（来自a  -  z的字母是：\ n）;而（temp <= z）{printf（％c \ n，temp）;temp ++;返回0;} </ OL>  
<li> #include <stdio.h> </ li>  
<li> </ li>  
<li> int main（）</ li>  
<li> char temp = a;</ Li>  
<li> printf（来自a  -  z的字母是：\ n）;</ Li>  
<li> while（temp <= z）</ li>  
<li> {</ li>  
<li> printf（％c \ n，temp）;</ Li>  
<li> temp ++;</ Li>  
<li>返回0;</ Li>  
<li>} </ li>  
### 回答 6
然而，有可能是非常缺乏的。  
考虑循环：  
<OL> for（int i = 0; i <endvalue; i ++）{// stuff} </ ol>  
<li> for（int i = 0; i <endvalue; i ++）{</ li>  
<li> // stuff </ li>  
<li>} </ li>  
尽管在那里有几个编程语言存在，但没有相应的汇编语言。因此，上面的代码被翻译成伪组装：  
<OL> MOV 0，EAX MOV EndValue，EBX LOOP：// Stem Icome EAX // IS ++ MOV EBX，EBC子ECX，EAX JGZ环路</ OL>  
<li> mov 0，eax </ li>  
<Li> Mov EndValue，EBX </ Li>  
<li>循环：</ li>  
<li> // stuff </ li>  
<li> in eax // i ++ </ li>  
<li> movebx，ebc </ li>  
<li>子ECX，EAX </ LI>  
<li> JGZ环</ Li>  
总之，上面的组装（假设EndValue是阳性的）：  
然而，有可能是非常缺乏的。  
考虑循环：  
<OL> for（int i = 0; i <endvalue; i ++）{// stuff} </ ol>  
<li> for（int i = 0; i <endvalue; i ++）{</ li>  
<li> // stuff </ li>  
<li>} </ li>  
尽管在那里有几个编程语言存在，但没有相应的汇编语言。因此，上面的代码被翻译成伪组装：  
<OL> MOV 0，EAX MOV EndValue，EBX LOOP：// Stem Icome EAX // IS ++ MOV EBX，EBC子ECX，EAX JGZ环路</ OL>  
<li> mov 0，eax </ li>  
<Li> Mov EndValue，EBX </ Li>  
<li>循环：</ li>  
<li> // stuff </ li>  
<li> in eax // i ++ </ li>  
<li> movebx，ebc </ li>  
<li>子ECX，EAX </ LI>  
<li> JGZ环</ Li>  
总之，上面的组装（假设EndValue是阳性的）：  
我们可以（再次 - 非常强烈建议不要这样）复制C：  
<ol> int i = 0;循环：//做填充if（i ++ <endvalue）goto循环; </ OL>  
<li> int i = 0; </ Li>  
<li>循环：</ li>  
<li> // do stuff </ li>  
<li> if（i ++ <endvalue）</ li>  
<li> goto循环; </ Li>  
转到从一个地方到另一个地方的无条件跳跃，因为跳进错误的地方而导致程序中的无数错误并打破堆叠。  
与使用GOTO语句几乎与之一样糟糕的替代方案是使用递归。  
<ol> void循环（int i，int结束）{if（i <结束）{//填充循环（i + 1，结束）; }} </ OL>  
<li> void循环（int i，int结束）{</ li>  
<li> if（i <结束）{</ li>  
<li> // stuff </ li>  
<li>循环（i + 1，端）; </ Li>  
<li>} </ li>  
然而，这也产生问题，因为调用函数也很高。当函数称为行（或相当指令号码）从调用的位置放在堆栈中，需要在另一个函数之前读取它可以读取其参数（然后在函数结束之前放回到那里）。该解决方案将导致高端值的过度内存使用。  
### 回答 7
<ol> #include <bits / stdc ++。h>使用命名空间std;int main（）{int i，j;我= 2;do {cout << i <<：\ n;for（j = 1; j <= 10; j ++）cout << i << * << j << = <<（i * j）<< \ n;cout << \ n;I ++;} whiled（i <= 10）;} </ OL>  
<li> #include <bits / stdc ++。h> </ li>  
使用命名空间std;</ Li>  
<li> </ li>  
<li> int main（）</ li>  
<li> {</ li>  
<li> int i，j;</ Li>  
<li> i = 2;</ Li>  
<li> do </ li>  
<li> {</ li>  
<< i <<的表格<< i <<：\ n;</ Li>  
<li> for（j = 1; j <= 10; j ++）</ li>  
<li> cout << i << * << j << = <<（i * j）<< \ n;</ Li>  
<li> cout << \ n;</ Li>  
<li> i ++;</ Li>  
<li> </ li>  
<li>}（我<= 10）;</ Li>  
<li>} </ li>  
以上提出了一种简单的解决方案。评论如果你什么都不理解。如果必要的更改循环，似乎可以使用do-while，以循环进行必要的问题。  
### 回答 8
虽然（1）{  
做{  
for（int j = 0; j <= 50; j + = 2）  
cout << J << ENDL;  
}}虽然（0）;  
休息;  
}  
### 回答 9
这将是一个过于简单的，但对这个问题的非语言特定答案：  
### 回答 10
问题陈述有点模糊，但我猜测该程序中的关键元素是程序员不知道要输入的方形矩阵的尺寸，因此程序必须能够调整到任意数量的输入元素只要该数字是整数平方（1,4,9,16,25等）。问题陈述也没有说明组装矩阵的内容;假设元素是数字IEDoubles.Dale Keener的（DK）建议您将二维矩阵视为一维元素组，其中行连接端到端（1-D ），而是超过另一个（2-D），应该在这里派上友好。在这里，在其他单词中，虽然您的程序的用户可能会想到它们的2×2阵列，如此二 -  D布局：  
<li> 0 1 </ li>  
<li> 2 3 </ li>  
您还可以在1-D布局中认为它是这样的：  
<OL> 0 1 2 3 </ OL>  
<li> 0 1 2 3 </ li>  
如果您还具有单行长度为两个元素的信息，则可以从1-D表示到2-D表示。我们在此完成的是将矩阵的2-D性质降低到a 1-d可以表示任何行长度的方形矩阵的公共元素类型的1-d数据对象.That 1-d对象现在适合于问题陈述的循环的输入，其中一组常量的操作将重复，只要重复一些条件是满足的。条件可能是只要读取/查找/解析另一个数字;我们将其留给您来确定如何表达该条件（它取决于您选择的输入方法），但只要它评估为True（非零），循环将解析的输入元素放入1- D对象，然后循环回尝试解析下一个输入元素。我们所做的其他事情是推迟确定行长度，直到所有矩阵元素输入都完成，大多是因为，除非您要求用户指定行长度以前矩阵元素输入，程序无法知道行长度，直到它知道1-D对象中有多少元素。这需要程序来跟踪，或者确定矩阵元素输入完成后，元素的数量在1-D对象中.ONCE没有更多有效输入，可以从1-D对象中的元素数确定行长度：25个元素意味着行长度为5; 9个元素意味着行长度为3; Again，我们将其留给您，以确定如何从矩阵元素的数量到行长度.NOTA Bene：输入导致的行长度是可能的，EG11元素不能排列成完整的方形矩阵，因此您需要决定如何检测和将这些案例视为错误.NBALSO矩阵将为Square的初始规范是允许您隐含地从Inputs.so中隐含地确定行长度的结果对于2-D平方矩阵的一些数字，nsquared的输入元素，将它们存储到1-d对象中，退出[while]循环，我们已经确定了一行的长度，现在我们需要使用[do ... while ... while]循环在2-d中显示矩阵，即使它存储在1-d optook中.A 2-D显示将包含n个元素的n个元素。如果您只需输出一个元素在他们现有的序列中的一段时间后跟一条线终结者，我怀疑你已经知道怎么办，你会哈哈一行的一排扁豆;我将它留给您如何将1-by-nsquared输出更改为n-by-n output.i写了一个程序来执行此操作，以确保我给出的任何建议都是有道理的，但我同意戴尔·佩雷纳代码不应该在这里分享或者锻炼对您没有价值;典型的输出如下：前两个输入元件的无效计数（零和两个）;最后三个案例分别有9,4和1个元素，分别为3,2和1的行长。我建议您尝试使用到目前为止提供的建议进行编码;如果您有任何疑问或任何问题不清楚，我怀疑Dale Keener或者我愿意进一步提出建议。  
### 回答 11
void main（）  
{  
 int n，f，f1 = -1，f2 = 1;  
 cout <<输入条款数：  
 CIN >> n;  
 cout <<斐波纳契系列是：;  
 做  
 {  
 f = f1 + f2;  
 F1 = F2;  
 F2 = F;  
 cout << f <<;  
 n--;  
 } while（n> 0）;  
}  
