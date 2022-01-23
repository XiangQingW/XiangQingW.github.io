---

title: 在c ++中使用printf是一个不好的做法？
date: 2022-01-23T22:08:05+08:00

---




## 在c ++中使用printf是一个不好的做法？  
### 回答 1
我们在这件事上有两种思想。  
好的  
打印f的一些非常严重的优势。其中一个最明显的是它可以允许比iostreams和机械手更紧凑的格式化。例如，让我们考虑这样的代码：  
<ol> printf（％＃ -  2.2x \ n，foo）; </ OL>  
<li> printf（％＃ -  2.2x \ n，foo）; </ Li>  
使用iostreams操纵器的操作根本并不琐碎。即使是最简单的模仿也是如此：  
<ol> std :: cout << std :: setfill（0）<< std :: hex; std :: cout << std :: setw（4）<< std :: setPrecision（4）<< std :: left << std :: hex << std :: showbase << foo; std :: cout << st </ ol>  
<li> std :: cout << std :: setw（4）</ li>  
<li> << std :: setPrecision（4）</ li>  
<li> << std :: left </ li>  
<li> << std :: hex </ li>  
<li> << std :: showbase </ li>  
<li> << foo; </ Li>  
<li> std :: cout << st </ li>  
我们在这件事上有两种思想。  
好的  
打印f的一些非常严重的优势。其中一个最明显的是它可以允许比iostreams和机械手更紧凑的格式化。例如，让我们考虑这样的代码：  
<ol> printf（％＃ -  2.2x \ n，foo）; </ OL>  
<li> printf（％＃ -  2.2x \ n，foo）; </ Li>  
使用iostreams操纵器的操作根本并不琐碎。即使是最简单的模仿也是如此：  
<ol> std :: cout << std :: setfill（0）<< std :: hex; std :: cout << std :: setw（4）<< std :: setPrecision（4）<< std :: left << std :: hex << std :: showbase << foo; std :: cout << std :: setfill（）<< std :: dec << \ n; </ OL>  
<li> std :: cout << std :: setw（4）</ li>  
<li> << std :: setPrecision（4）</ li>  
<li> << std :: left </ li>  
<li> << std :: hex </ li>  
<li> << std :: showbase </ li>  
<li> << foo; </ Li>  
<li> std :: cout << std :: setfill（）<< std :: dec << \ n; </ Li>  
耶！一个8字符的格式字符串已变成8行代码（它对参数打开，即它仍然无法真正正确）。  
Printf还允许您从外部文本文件加载格式字符串，支持标签和格式的更改，而无需在某些情况下重新编译。  
坏人  
PRINTF通常相对较慢，因为它通常会在运行时解释格式字符串。它包括一个格式字符串解析器，一次浏览格式字符串中的字符，并计算出某些东西是否是打印出的字符字符，或者（一部分）转换规范。相比之下，通过iOStreams，格式化在编译时都是已知的，因此没有运行时解释，以解决格式字符串装置的方式。  
在支持不成部分基本语言的任何类型方面，Printf也会失败。如果您有一个结构，它不会提供打印出整个结构的任何简单支持 - 您必须单独指定每个元素（并且通常最终也有很多重复的代码来执行此操作）。  
丑陋  
另一方面，随着其他人指出，Printf以多种方式非常不安全。获得未定义的行为非常容易。更糟糕的是，相当多的未定义行为案例通常会产生无害的寻找结果，因此在某人在展示错误所必需的情况下在某些人测试之前存在多年的错误是相当常见的。  
### 回答 2
不必要。这取决于你正在做的什么样的格式。如果您做了很多花哨的格式，Printf的格式字符就可以比使用Cout的格式系统更容易：  
<ol> printf（宽度=％5.2f cm \ n，w）; printf（长度=％5.2f cm \ n，l）; Printf（直径=％5.2F cm \ n，d）; printf（圆周=％5.2f cm \ n，c）; </ OL>  
<li> printf（宽度=％5.2f cm \ n，w）; </ Li>  
<li> printf（长度=％5.2f cm \ n，l）; </ Li>  
<li> printf（直径=％5.2f cm \ n，d）; </ Li>  
<li> printf（圆周=％5.2f cm \ n，c）; </ Li>  
但是，如果你只是做简单的打印并且不需要做重型格式，那么就可以说些什么：  
<ol> cout <<长度是<< l << cm << endl; </ OL>  
<li> cout << length是<< l << cm << endl; </ Li>  
只需记住使用c style io时#include <stdio.h> #include <iostream>  
不必要。这取决于你正在做的什么样的格式。如果您做了很多花哨的格式，Printf的格式字符就可以比使用Cout的格式系统更容易：  
<ol> printf（宽度=％5.2f cm \ n，w）; printf（长度=％5.2f cm \ n，l）; Printf（直径=％5.2F cm \ n，d）; printf（圆周=％5.2f cm \ n，c）; </ OL>  
<li> printf（宽度=％5.2f cm \ n，w）; </ Li>  
<li> printf（长度=％5.2f cm \ n，l）; </ Li>  
<li> printf（直径=％5.2f cm \ n，d）; </ Li>  
<li> printf（圆周=％5.2f cm \ n，c）; </ Li>  
但是，如果你只是做简单的打印并且不需要做重型格式，那么就可以说些什么：  
<ol> cout <<长度是<< l << cm << endl; </ OL>  
<li> cout << length是<< l << cm << endl; </ Li>  
使用C ++样式IO时，请记住#include <stdio.h> #include <iostream> #include <iostream>。  
### 回答 3
不，但它不安全，看看这个代码：  
<ol> printf（hello％s \ n）;</ OL>  
<li> printf（hello％s \ n）;</ Li>  
％s意味着将从printf的第二个参数中检索字符串，不存在的参数，因此，printf将读取一些内存地址，可能会崩溃计算机，或者您将具有不确定的行为。  
STD :: COUT <<远更好，效果安全，虽然不像Printf一样多才多艺。  
对它们两个非常好的替代品是FMTLIB：  
FMTLIB / FMT.  
### 回答 4
我想加入Jerry Coffin非常好的答案，通过现代的C ++可以获得STD :: Printf [1]的良好，而没有糟糕的和丑陋，使用已引入的C ++ 11。< a> [1] </a>  
改进的Printf实现的一个示例是{fmt}库[2]，它提供与编译时类型安全的Printf样和Python语法，扩展到自定义类型。<a> [2] </a>  
以下是从{fmt}图书馆github的页面中取出的一些示例：  
打印你好，世界！到stdout：  
<ol> fmt ::打印（Hello，{}！，世界）; // python样格式字符串语法fmt :: printf（hello，％s！，world </ ol>  
<li> fmt ::打印（hello，{}！，世界）; // python样格式字符串语法</ li>  
<li> fmt :: printf（hello，％s！，世界</ li>  
脚注  
我想加入Jerry Coffin非常好的答案，通过现代的C ++可以获得STD :: Printf [1]的良好，而没有糟糕的和丑陋，使用已引入的C ++ 11。< a> [1] </a>  
改进的Printf实现的一个示例是{fmt}库[2]，它提供与编译时类型安全的Printf样和Python语法，扩展到自定义类型。<a> [2] </a>  
以下是从{fmt}图书馆github的页面中取出的一些示例：  
打印你好，世界！到stdout：  
<ol> fmt ::打印（Hello，{}！，世界）; // python格式的格式字符串语法fmt :: printf（hello，％s！，世界）; // printf格式字符串语法</ ol>  
<li> fmt ::打印（hello，{}！，世界）; // python样格式字符串语法</ li>  
<li> fmt :: printf（hello，％s！，世界）; // printf格式字符串语法</ li>  
格式化字符串并使用位置参数：  
<ol> std :: string s = fmt :: format（ID而不是{1}而不是{0}。，右，开心）; // s == id而不是右边的快乐。</ ol>  
<li> std :: string s = fmt :: format（ID而不是{1}而不是{0}。，右，开心）; </ Li>  
<li> // s == id而不是右边的快乐。  
### 回答 5
我还可以添加其他图书馆可以更安全，并且在某些情况下，比Printf及其亲属更快，至少比Ostream互动更具表现力和紧凑  
杰瑞有一个非常好的答案，涵盖了标准图书馆的所有领土，虽然我对iostreams的经验是，在测量时，大多数实现的性能都比printf更糟糕。  
尽管如此，我会说它是使用Printf的最不好的做法，或者对于那么重要，C的变量函数的大多数应用。  
我还会添加其他图书馆可用，更安全，并且在某些情况下，比Printf及其亲属更快，至少比Ostream界面更为富有表现力和紧凑，并且通常比Ostream更有表现。  
Boost格式库 - 优点：型安全性，大多数Printf格式，支持比其他人更广泛采用。  
缺点：运行时解析格式说明符字符串，同时有用兼容性方面，具有性能影响;不支持特定于语言环境的数字格式（单引号'）和输入精度（星号*）  
{FMT}：概述 -  FMT 5.2.0文档 - 优点：真正快速（FMTLIB / FMT）;对于包含的低开销，可以在编译时解析最新的constexpr支持，熟悉python用户的熟悉语法。  
缺点：我相信一些表达式仍然是已解析的，语法没有用printf映射1-1，无法在编译时构建单通机分配。  
谷歌的ABSEIL / ABSL :: Strforvat（） - 优点：真的很快;适度的开销纳入;仔细映射到Printf格式选项  
缺点：Wonky Google习语，稍微奇怪的语法，假设STD :: String目标。  
### 回答 6
使用printf是一个很好的做法。使用iostreams是一个糟糕的做法。它们是一个非常不成功的实验，失败了，并且永远不应该使用。  
