---

title: 什么类型的语言是机器语言（即，结构化，面向对象等）？
date: 2022-01-23T22:08:06+08:00

---




## 什么类型的语言是机器语言（即，结构化，面向对象等）？  
### 回答 1
这不是那些。已经开发出所有后续语言类型，以避免机器语言编程的难度。  
首先，机器语言几乎没有被人类写成，因为它只是数字。  
例如，在旧ZX频谱上，基于Z80微处理器，该程序将打印一个空间：  
62,32,215,201。  
并不意味着太多了吗？  
在这里它是汇编语言 - 这只是一种使用助记符而不是数字写作机器语言的简写方式：  
LD A，20  
RST 10.  
托  
汇编语言（且机器语言）没有变量。它只是记忆和r  
这不是那些。已经开发出所有后续语言类型，以避免机器语言编程的难度。  
首先，机器语言几乎没有被人类写成，因为它只是数字。  
例如，在旧ZX频谱上，基于Z80微处理器，该程序将打印一个空间：  
62,32,215,201。  
并不意味着太多了吗？  
在这里它是汇编语言 - 这只是一种使用助记符而不是数字写作机器语言的简写方式：  
LD A，20  
RST 10.  
托  
汇编语言（且机器语言）没有变量。它只是具有内存和寄存器（CPU本身内的快速位存储器）。它没有参数的函数，而是必须设置寄存器并跳转到函数地址，推动您在堆栈上的位置，以便您可以返回到那里（幸运的是，机器有呼叫/ RET指令）。  
这既是非常简单的语言，也是一个非常坚硬的语言，因为它非常简单。  
因此，如果您在理解它时进行编程，并带走类似程序，函数，局部变量，对象，结构的东西......然后您最终有点像汇编语言。带走指令和注册的有用的英语名称，并用数字替换它们，并最终使用机器语言。  
### 回答 2
机器语言都不是这些。它只是表示CPU指令的字节序列。没有一个高级语言编程范例应用于机器语言。在此级别，没有变量，控制结构，数据结构，对象，类，方法/函数等。所有这些概念都由高级语言提供，但最终将机器语言转换为内存位置，条件和无条件的跳跃指令，呼叫/ retu ...  
