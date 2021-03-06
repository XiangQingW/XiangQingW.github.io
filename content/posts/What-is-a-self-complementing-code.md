---

title: 什么是自我补充的代码？
date: 2022-01-23T22:08:19+08:00

---




## 什么是自我补充的代码？  
### 回答 1
自补充代码是具有9个十进制NO补充的属性的代码。通过在图案中的每个比特互补1s，通过替换1s和0s直接获得。  
示例 - 所示的图片中  
### 回答 2
如何识别自我补充代码？  
回答这个。  
### 回答 3
在我的脑海里，它是偶尔打印输出的代码，即向申请者说，谢谢你释放我帅哥！或者谢谢你给我吃晚餐的意大利面条代码！:)  
### 回答 4
谢谢你的A2A。  
加权代码： - 加权码是遵守位置加权原理的码，这使得每个数字的位置表示特定权重。在这些代码中，每个十进制数字由一组四位表示。  
 在加权代码中，每个数字根据其位置分配特定权重。例如，在8421 / BCD码中，1001的重量为1,1,0,1，（从左到右）分别为8,4,2和1。  
有数百万加权代码是最常见的代码是8421 / BCD代码。  
示例：8421,2421,84-2-1是所有加权代码。  
非加权代码：t  
谢谢你的A2A。  
加权代码： - 加权码是遵守位置加权原理的码，这使得每个数字的位置表示特定权重。在这些代码中，每个十进制数字由一组四位表示。  
 在加权代码中，每个数字根据其位置分配特定权重。例如，在8421 / BCD码中，1001的重量为1,1,0,1，（从左到右）分别为8,4,2和1。  
有数百万加权代码是最常见的代码是8421 / BCD代码。  
示例：8421,2421,84-2-1是所有加权代码。  
非加权代码：非加权码在位置加权。换句话说，未分配给每个数字位置的任何权重的代码。  
示例：超级3（XS-3）和灰度代码。  
有关更好理解的链接：  
二进制代码  
BCD代码  
非加权代码  
### 回答 5
超出3个代码是基本10代码的示例。当评估它时，相对于其他十进制代码评估它是有用的，如二进制编码的十进制（BCD）或2421代码。它不用比比较十进制代码与二进制文件.Binary对计算机来说远更好，特别是现在计算是便宜的。指数在早期的计算机历史中更有用，人们不想将二进制文件转换为Decimal.excess-3代码，由表示的4位码字组成数字值0到9如下：  
有几个有趣的3个代码的属性：  
与此线程中的其他答案不同，我发现第一个属性比第二个属性更有趣。事实上，其他答案似乎是无知的超出3个代码的真正力量。我可以告诉我，超出3个代码有用的真正原因是，超过3个加法和减法比其他十进制代码更直接，尤其是BCD。（注意：重要的是要注意，超出3算术并不多与二元相比，直截了当的）.excess-3添加  
让我们来看看过度的3加法。请说我有一个值A.ITS超出3版本是一个+ 3.likeWise，数字B的超出版本B将是B + 3.let在没有携带的简单情况下。如果我添加一个+ 3到b + 3，我将获得（a + b）+ 6.in以将最终总和纠正到有效的超额3值，我需要减去3，这将给我一个正确的值（a + b）+ 3.let看一个example.let表示我想做3 + 4.3  - > 0110  
4  - > 0111  
0110 + 0111 = 1101（不是有效的超额3个值。减去3）  
1101  -  011 = 1010（超过3值7，这是正确的总和）  
您可以清楚地看到该算法添加2个超出3位数的时间，当数字不续位时，让我们转到第二种情况下，在那里携带携带。阐明后面的推理有点难以正式化，所以让我们更先看看一个榜样。如果我们想做6 + 7，我们将执行以下操作：  
6  - > 1001  
7  - > 1010  
1001 + 1010 = 10011  
最重要的1位实际上是携带，所以我们留下了：  
0011  
我们现在可以看到，要获得正确的超出3个值，我们需要添加3所以我们可以获得0110.这项工作的原因在下面的段落中解释。（注意，它可能很难阅读，而且这是一个有点手摇。你可以跳过它并抓住我的话，如果你愿意）。如果我们增加了3个+ 3和B + 3的3个值，我们的总和将是（A + B）+6。但是，如果生成携带，我们正在寻找的特定数字将需要由16：（a + b）+6 mod 16.now，此添加的某个属性是（a + b） +6将始终小于32.因为这一点，我们实际上可以说（a + b）+6 mod 16 =（a + b）+ 6-16 =（a + b）-10。然而，这种情况当A + B的总和产生携带的常规基础-10的总和的常规基础10和的数字。对于示例，6 + 5 = 11，并且最低有效数字为11-10 = 1.sh，我们的过度3加入的输出是携带的常规总和的最低数量，因为输出是正常的总和，我们需要通过添加来将其纠正到其超额3版本3.所以，添加2个超出3位数的规则如下：  
使用借款定期减法是类似的。如果您了解添加规则的证明，则减去规则将非常简单地证明。还可以通过执行10的补充减法来减少减法方法.Since超出了3码自我补充，您可以简单地翻转比特并添加1以获得10年代的子系统补充，并且您可以将其添加到您的Minuend以获得差异。例如，让我们说我想做49  -  22.49的减法 - > 0111 1100（Minuend）  
22  - > 0101 0101（Subtrahend）  
10的22份补充将是：  
然后，我们可以做出补充：  
如上所述，超级3的益处是添加和减法比其他十进制代码更容易，尤其是BCD .BCD代码如下：  
在BCD中添加的规则沿着以下行（如果我错了，请纠正我）：  
逻辑的逻辑比超出-3附加的逻辑更复杂。如果您想要处理减法，逻辑将更加复杂。我可以想象，当十进制代码很受欢迎时，返回超出3在实施方面对BCD的巨大效益。  
### 回答 6
超出3个码字是自我补充的，因为它们是特别选择的。  
要了解他们为什么是自我补充的，让我们首先枚举所有4位二进制数。  
如果您介绍这一点，您可以观察到，如果两个数字A和B加入到最多15个，则A和B的二进制表示将彼此补充，这意味着您可以通过翻转比特来获得另一个。  
证明这是非常简单的。通过连续四个1获得二进制值15。在任何数字处，您可以具有1作为总和的唯一方法是：  
然而，案例2是不可能的，因为对于最低有效数字没有携带。这意味着不可能在没有总和的数字之一的情况下生成携带，因此，通过必要性，每个数字必须遵循规则1，这将根据定义需要两个概述彼此的补充。  
现在让我们考虑十进制代码。十进制代码是4次数字代码字，代表十进制值。最直观的代码是二进制代码十进制（BCD），看起来像这样。  
您可以看到使用可能的16个二进制代码中的10个，并且6是未使用的。这里，6个未使用的码字是最后的。  
但是，我们可以重新分配10位数字以使其使未使用的码字均可在开头和结尾处分布。  
这是3个码。  
因为这种转变，我们有对称性。这种对称意味着，当两个码字的十进制值增加到9时，两个码字的二进制总和将是15.这意味着代码是自互补的。  
因此，最终，因为我们选择了超额3代码来具有对称性并具有对称码字的十进制值，最多添加15，代码是自互补的。  
### 回答 7
考虑到你知道二进制数字的基础知识。  
84-2-1（8,4，4，-2，-1）是加权代码以及自补充代码，因为代码是自互补的代码的必要条件是其所有重量的总和必须是相等的到9即84-2-1（8 + 4-2-1 = 9）。  
例如，让我们参加84-2-1系统。  
十进制0 = 0000（在84-2-1系统中）＆（9s补码为0 = 9），那么9（84-2-1）应该具有1111.因此，0及其9S补码IE 9保持自我补充关系。  
让我们拿另一个例子：  
十进制1 = 0111（在84-2-1系统中）＆（9s补充1 = 8），其意同（84-2-1）  
考虑到你知道二进制数字的基础知识。  
84-2-1（8,4，4，-2，-1）是加权代码以及自补充代码，因为代码是自互补的代码的必要条件是其所有重量的总和必须是相等的到9即84-2-1（8 + 4-2-1 = 9）。  
例如，让我们参加84-2-1系统。  
十进制0 = 0000（在84-2-1系统中）＆（9s补码为0 = 9），那么9（84-2-1）应该具有1111.因此，0及其9S补码IE 9保持自我补充关系。  
让我们拿另一个例子：  
十进制1 = 0111（在84-2-1系统中）＆（9s补码为1 = 8），其意味着（84-2-1）等同于8的8，应该是1000，因此又称数量及其补充保留了他们的自我互补关系。  
来源：自补充代码（超额3,84-2-1,2 * 421）  
### 回答 8
通过自补充代码，在谈到时，硬件的设计更容易，9S补充减法。它是一种减法方法，负数被转换为9S补码。自我补充代码简单出路。假设您必须通过Say，3（0011）减去一个数字，其十进制9S补充代码为1100分配给第6号。类似地，如果0（0000），则为9（1111）。该对具有额定的位，易于在硬件中实现，增加了操作速度。  
### 回答 9
8-4-2-1是字典的，用于数量的数字抑制。这被称为BCD，这意味着二进制编码十进制。这是在这种计算机上使用的IBM 1620和IBM 1401.在IBM 360系列上，有在BCD数据上操作的指令。  
### 回答 10
这是指在通信信道上编码，如网络。不是编程语言。  
如果您要通过无线电网络发送代码1 0 0 1 1 0，您可以想象一些干扰意味着收到的是乱码的。例如，它可以接收为1 0 0 0 1 0。  
显然，您无法判断其中一个位已更改，这意味着您的数据或命令将是错误的。  
存在错误检测代码，例如奇偶校验位，汉明代码，循环冗余校验等。所有这些都添加额外的位，帮助您检测错误。  
奇偶校验是最简单的exp  
这是指在通信信道上编码，如网络。不是编程语言。  
如果您要通过无线电网络发送代码1 0 0 1 1 0，您可以想象一些干扰意味着收到的是乱码的。例如，它可以接收为1 0 0 0 1 0。  
显然，您无法判断其中一个位已更改，这意味着您的数据或命令将是错误的。  
存在错误检测代码，例如奇偶校验位，汉明代码，循环冗余校验等。所有这些都添加额外的位，帮助您检测错误。  
奇偶校验是最容易解释的。  
让我们用一个额外的额外重新发送我们的原始代码。我们将使用“偶数奇偶校验”系统，这意味着我们添加到末尾的新位将使“1”比特的总数变为偶数。  
在我们的情况下，原始代码有3位设置为1.最接近的偶数是四个，因此我们的“偶数奇偶校验”位必须为“1”。  
我们将代码重新发送为1 0 0 1 1 0 1  - 您可以在末尾看到额外的位。  
根据我们的示例，假设接收器具有相同的位损坏，所以我们收到了1 0 0 0 1 0 1  
在这里，奇偶校验位通过了。所以当我们检查 - 我们发现奇偶校验位与规则不匹配。当我们实际收到的数据的正确价值为零时，这是'1'。  
所以我们现在知道代码已损坏。  
但我们不知道如何解决它。我们只知道它不正确。  
纠错代码的类别与实际代码一起发送更多的交叉检查信息。这些检测错误不仅可以检测到错误，它们都可以检测到哪些特定位出错。当您只能有两个值的位 -  0和1  - 如果您知道这是错误的，则会自动知道合适的值是什么。  
通过在接收器结束时用正确的位置替换错误的值，您已成为自我纠正的代码。  
非常方便的是NASA这样的工作，其中一个微小的空间探头，带有微小的电源，而且一颗微小的天线试图告诉我们太阳系的边缘就像是什么样的。我们得到一个非常微弱，非常损坏的信号。  
而自我纠正的代码是我们根本听到它的唯一原因。  
### 回答 11
为什么这种转换完成可以被视为超额3代码的重要性，或者是什么是应用程序  
超出3的应用  
由于添加了许多缺点，还提供了BCD代码，使用过量的3个代码，并且在飞机的轴位置使用灰色码。  
这些代码精确地用于电光开关和电化学信号。  
灰色代码在许多现实生活中出现。一开始，代码的主要使用与我们现在称为从模数到数字格式的转换相关的。基本目标是转换电压值  
为什么这种转换完成可以被视为超额3代码的重要性，或者是什么是应用程序  
超出3的应用  
由于添加了许多缺点，还提供了BCD代码，使用过量的3个代码，并且在飞机的轴位置使用灰色码。  
这些代码精确地用于电光开关和电化学信号。  
灰色代码在许多现实生活中出现。一开始，代码的主要使用与我们现在称为从模数到数字格式的转换相关的。基本目标是转换先前在模数到相应系列脉冲中的电压值，这将表示数字形式的相同值。该技术是通过垂直移动电压来转换电压，电子束水平地穿过阴极射线管的屏幕横扫。在其上具有掩蔽印记的屏幕仅允许梁在某些位置的通道，并且产生电流直至梁通过掩模。光束的通过产生一系列“开”和“关闭”条件，其通过它通过的孔的图案。  
最常见的灰色码使用是定位用于轴I的旋转位置，该轴I表示灰色码的图案印刷在盘上，或在轴上印刷，并且通过电气或光学检测器感测该图案。  
灰色代码用于一些旧计算机，依赖于预先指定的数字N作为偏置值。  
超出3个代码是表示具有正数和负数余额的数字的技术。当这些超出3个数字中的两个的总和超过9时，加法器的携带位将设置为高。当您添加两个超出3个数字时，结果不会是过量的3号，示例：添加1到3，答案似乎是7，但实际答案应该是4，所以这个问题的补救措施是减去3 （二进制011）如果结果小于十进制10并且如果数字等于或大于10，则添加3。  
由于我们添加两个数字时，需要完成这一点，但总和的六个结果的超值值超值。但是，我们现在，0到15的值是四位整数，并且对于这意味着总和将溢出。  
希望这可以帮助。为什么代码转换取决于它的应用程序  
谢谢你的询问  
### 回答 12
哇......我认为我第一次看到了几十年来任何地方的3个。有一个时间是一个适度流行的BCD号码表示。接下来你知道，人们会询问RAD50。  
如果将位中的BCD数字翻转到过多的3位，结果是九个中的3个BCD补充 - 无论如何，无论如何，我猜这在硬件较高的那一天的那天保存了硬件。这是代码的几个潜在优势之一，尽管似乎没有挽救它。  
