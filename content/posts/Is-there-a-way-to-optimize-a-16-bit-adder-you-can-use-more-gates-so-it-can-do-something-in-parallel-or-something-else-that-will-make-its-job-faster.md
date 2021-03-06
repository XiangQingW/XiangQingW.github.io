---

title: 有没有办法优化16位加法器（你可以使用更多的盖茨），所以它可以并行地做点什么或者其他东西将使其工作更快？
date: 2022-01-23T22:08:03+08:00

---




## 有没有办法优化16位加法器（你可以使用更多的盖茨），所以它可以并行地做点什么或者其他东西将使其工作更快？  
### 回答 1
有许多技术，包括携带潜行和携带选择方法。如果您正在进行大量的添加，您可能会考虑冗余编码，以推迟带有Carry-Save Adder。  
很多，许多方法都在那里。  
这个博客帖子有一个很好的调查：  
### 回答 2
加法器是ALU（算术和逻辑单元）的核心。使用适当的逻辑，即使对于乘法或划分，也可以使用它进行比较。  
鉴于在成像中，大多数像素是8位，您可以在并行地添加电路以在两组8位数字上运行。  
### 回答 3
是的。使用携带看法发生器（CLA）。大多数ALU产品都有一个伴侣CLA。  
### 回答 4
是的，我们的设计将以光速传播携带;不仅仅快，而且以光速为字面。  
除了一个小细节外，这将是一种伟大的发明：我们正在使用继电器逻辑 - 大型机电继电器。  
我们使用的继电器具有十分之一秒的切换时间。因此，涟漪加法器将显着慢 - 超过一秒钟传播携带。我们不想等待那久。  
所以我的朋友重新设计了电路，使其作为携带和连接在阶段之间的携带和连接的功能，产生输出。随着电流可以去的速度，携带通过封闭的触点 - 光速。  
结果是一个加法器，可以在恒定的一个门延迟中添加任何两个数量的多个比特。  
当然，一个门延迟比任何合理的逻辑门更长的数量级数量多。如果可能有可能使用FET或某物使用相同的技术，但是您可以添加电容等，因此它不会像速率一样快（相对于栅极延迟）。  
### 回答 5
基本上实现了一个完整的加法器，需要两个4：1 mux。  
让我们从头开始。  
要实现完整加法器，首先需要了解总和和携带的表达式。  
这是表达式  
现在需要将SUM的表达和携带在MUX树内。  
对于Mux树计算，允许我们考虑Mux的以下参数。  
I（0）到I（3）是所需的输入。  
从上面的计算中，B和C被视为选择线（从上述完整加法器的真相表中取出）。  
和T...  
### 回答 6
首先让我们看到半加法器。  
在哪里  
s =a⊕bs=a⊕b  
c = abc = ab  
现在FA增加了三位A，B和之前的携带孔。  
这里，  
s =a⊕bəcins=a⊕bəcin  
cout = ab + bc + cacout = ab + bc + ca  
现在FA可以使用两个如下实现。  
在图中，p = a，q = b  
这里，  
cout1 = ab，s1 =a⊕bcout1= ab，s1 =a⊕b  
s2 =a⊕bəcins2=a⊕bəcin  
cout =（ab）+（cin.s1）cout =（ab）+（cin.s1）  
= ab + cin（a'b + ab'）= ab + cin（a'b + ab'）  
= ab + cina'b + cinab'= ab + cina'b + cinab'  
= ab + ab + cina'b + cinab'（∵x+ x = x）= ab + ab + cina'b + cinab'（∵x+ x = x）  
= A（b + b'cin）+ b（a + a'cin）= a（b + b'cin）+ b（a + a'cin）  
= a（b + cin）+ b（a + cin）（∵x+ x'y = x + y）= a（b + cin）+ b（a + cin）（∵x+ x'y = x + y）  
= ab + bcin + cina = ab + bcin + cina  
证明x + x'y = x + yx + x'y = x + y  
我们知道，a + bc =（a + b）（a + c）a + bc =（a + b）（a + c）  
⟹⟹lhs = x + x'y =（x + x'）（x + y）lhs = x + x'y =（x + x'）（x + y）  
=（1）（x + y）=（1）（x + y）  
= x + y = RHS■= x + y =RHS◼  
首先让我们看到半加法器。  
在哪里  
s =a⊕bs=a⊕b  
c = abc = ab  
现在FA增加了三位A，B和之前的携带孔。  
这里，  
s =a⊕bəcins=a⊕bəcin  
cout = ab + bc + cacout = ab + bc + ca  
现在FA可以使用两个如下实现。  
在图中，p = a，q = b  
这里，  
cout1 = ab，s1 =a⊕bcout1= ab，s1 =a⊕b  
s2 =a⊕bəcins2=a⊕bəcin  
cout =（ab）+（cin.s1）cout =（ab）+（cin.s1）  
= ab + cin（a'b + ab'）= ab + cin（a'b + ab'）  
= ab + cina'b + cinab'= ab + cina'b + cinab'  
= ab + ab + cina'b + cinab'（∵x+ x = x）= ab + ab + cina'b + cinab'（∵x+ x = x）  
= A（b + b'cin）+ b（a + a'cin）= a（b + b'cin）+ b（a + a'cin）  
= a（b + cin）+ b（a + cin）（∵x+ x'y = x + y）= a（b + cin）+ b（a + cin）（∵x+ x'y = x + y）  
= ab + bcin + cina = ab + bcin + cina  
证明x + x'y = x + yx + x'y = x + y  
我们知道，a + bc =（a + b）（a + c）a + bc =（a + b）（a + c）  
⟹⟹lhs = x + x'y =（x + x'）（x + y）lhs = x + x'y =（x + x'）（x + y）  
=（1）（x + y）=（1）（x + y）  
= x + y = RHS■= x + y =RHS◼  
### 回答 7
真值表是输入的基本表示对任何逻辑设计或电路的输出。  
两位完整加法器 - 让我们单独描述该电路的输入和输出。  
考虑到上述输入和输出，可以表示真相表 - （注意：这是一个部分TT，以了解电路以及它的工作原理）  
### 回答 8
NAND盖茨做了两件事，只有一个东西。  
NAND门是AND门，然后是不是门。这是“额外”的反演（实际上它在大多数电路实现中免费提供）使其比平原和更容易。您可以使用NAND制作所有其他逻辑功能，因为Demorgan的定理，所以在实践中，这就是您所需要的。  
### 回答 9
您不太可能找到4位加法器电路的完整真理表。如果您非常需要它，您必须生成它。但我必须警告你会很大，因为有很多输入的输入可以拥有4位加法器。  
对于生成真理表，您必须放置所有输入，然后找出输出位。或者您可以使用计算机程序简化您的任务。  
在这里，我使用Excel生成了真实表的简单版本。  
如果您希望您可以使用Excel文件并查找其他组合。4-bitaddertruthtable.xlsx.  
### 回答 10
你不。  
当您将最不显着的芯片的随身携带和最小重要的芯片的随身携带到逻辑0时，两个4位加法器芯片（74283系列）工作正常。  
但是要从使用2的补充中减去B，您必须通过更改最小显着的芯片的携带到逻辑1来补充所有八位B并添加1。补充B的方式是XOR与减去控制的所有八个输入信号，然后将八个XOR结果连接到两个加法器的B输入。还将最不重要的加法器芯片的随比减去更换最小的加法器芯片。当您希望A-B（减去= 1）并在需要时添加0时，将添加1（减去= 0）。  
所以你需要两个7486级筹码。  
### 回答 11
添加剂是数字逻辑设备，可在一起添加或总和。虽然您可能会发现它们自己使用的一些应用程序，但您将更常见地发现它们用作算术逻辑单元（ALU）中的组件，它们本身是中央处理单元（CPU）中的组件。结果，您可以考虑的任何电子设备都有一个微控制器或其中的CPU使用加法器。一般来说，大多数家用电子设备可能会使用8位微控制器或32/64位CPU。因此，如果您有4位加法器，很可能与第二个4位加法器一起使用以形成8位加法器。  
示例包括：智能恒温器，带有数字读出的洗衣机或干洗机等设备，数字闹钟，数码手表，数字卫生间秤，游戏机，网络设备，如路由器或WiFi接入点，ECT ...  
以下是在通过计算系统的元素工作时创建的ALU：从NOAM Nisan和Shimon Schocken的第一个原则构建现代计算机。此示例中的加法器是16位加法器。关于添加剂的一个很好的部分是您可以将它们链接以创建应用程序中的应用程序。但是，您确实需要了解现实世界应用程序中的携带位的传播延迟，并确保您不会比加法器更快地将应用程序提高。滞后越多。  
这是一个4位加法器的事实意味着它需要4位输入。在二进制中，一位是1或0，并且大数字表示为一系列1S和0。 4位加法器可以将零的零的值与1111表示的零表示。如果结果不能存储在4位中，通常存在携带比特。例如，15 + 15 = 30，其在二进制中由11110表示。第五次携带位用于存储最有效位。 （最左边的比特）。  
0 = 0000.  
1 = 0001.  
2 = 0010  
3 = 0011  
4 = 0100.  
5 = 0101  
6 = 0110  
7 = 0111  
8 = 1000  
9 = 1001  
10 = 1010  
11 = 1011.  
12 = 1100.  
13 = 1101.  
14 = 1110.  
15 = 1111.  
它是并行加法器的事实是指同时读取所有4位。这需要提供4个完整的加法器来处理所有4位，并且需要更多的电线来加载所有位。不需要时钟。输出自动更新，因为输入的变化只是轻微的传播延迟。相比之下，串行加法器一次加载1位。由于这仅是一个完整的加法器，而不是并行加法器所需的4个完整加法器。您还需要更少的电线加载输入并读取数据。但是，由于您在一次需要时钟和通常操作时加载数据1bit，操作将慢。  
### 回答 12
完整的加法器（FA）是一个反对半加法器（HA）的名称。  
FA总和两个输入位（a，b）加上携带位（cin）并输出一个结果位和一个携带输出（下面的cout，图片，忽略输出处的0值）。  
HA SUMS两个输入位（A，B，无输入携带）并输出一个结果位（和）和一个携带输出（携带）。 （下图，再次忽略输出的0值）。  
请注意，可以使用两个半加法器和A或Gate构建完整的加法器。  
要使用一定数量的位链，以及相同数量的完整加法器，但第一个加法器中的一个正整数  
完整的加法器（FA）是一个反对半加法器（HA）的名称。  
FA总和两个输入位（a，b）加上携带位（cin）并输出一个结果位和一个携带输出（下面的cout，图片，忽略输出处的0值）。  
HA SUMS两个输入位（A，B，无输入携带）并输出一个结果位（和）和一个携带输出（携带）。 （下图，再次忽略输出的0值）。  
请注意，可以使用两个半加法器和A或Gate构建完整的加法器。  
要使用一定数量的位数，将正整数与您链的一定数量的完整添加剂一起链，但链条中的第一个加法器（LSB）的第一个加法器可以是公顷，因为初始携带输入是0.这一加法器链被调用波纹携带加法器，因为携带从LSB到MSBS的链的输出的变化。我认为这是您在问题中询问的串行加法器（加法者链是街区的串行排列）。下面是图片。  
这些添加剂的很好的财产是它们是完全模块化的，即，如果需要使用更多位的单词，我们只需为链添加更多fas。  
有许多变形的涟漪携带加法器，如携带展示前瞻加法器，携带跳过加法器和曼彻斯特链条加法器（见http://users.encs.concordia.ca/~asim/coen_6501/lecture_notes/l2_notes。 PDF。）。这些变化的目标是加速沿着加法器​​链的携带的涟漪，因为终端的总延迟限制了加法器的速度。  
最后，并行加法器通常是指具有n位输入的加法器，因此当它被视为块时，它被认为是并行的两个n位词的加法器，并输出（n + 1）位字。加法器的内部实现可以是已经提到的任何一个或其他人。  
图片从半加法器和完整的加法器电路中获取，包括对FA和HA的工作的更深解释。  
