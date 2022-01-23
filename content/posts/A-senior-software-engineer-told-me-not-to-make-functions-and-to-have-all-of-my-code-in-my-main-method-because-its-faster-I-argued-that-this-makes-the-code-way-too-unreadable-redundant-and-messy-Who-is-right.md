---

title: 高级软件工程师告诉我不要使函数并拥有我的主要方法，因为它更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？
date: 2022-01-23T22:08:11+08:00

---




## 高级软件工程师告诉我不要使函数并拥有我的主要方法，因为它更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？  
### 回答 1
这两个观点都有一些真相，但对于非琐碎，现实世界的开发项目，您比其他软件工程师更正确。  
考虑唐纳德Knuth，计算机编程系列艺术作者的以下声明：  
>程序员浪费了大量时间思考，或担心他们的计划的非关键部分的速度，并且这些尝试在调试和维护时实际上具有强烈的负面影响......  
### 回答 2
高级软件工程师告诉我不要使函数并拥有我的主要方法，因为它更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？  
代码比让我们说30行代码*是短的吗？然后他可能是对的。否则他几乎肯定不是。在99.99％的情况下，您赢得这种方式的性能可以忽略不计。在99.99％的情况下，您失去的代码质量并不可忽略不计。所以在99.99％的情况下，你是对的。  
而且，坦率地说，那个人不值得标签工程师，更不用说高级。  
*当方法变得超过10行时，我个人开始重构。我的大多数方法都长五行。  
### 回答 3
当代码完成后，可以p  
通过编写代码保存运行时间内联的是一个是便士和笨拙的例子。  
确实，函数调用每个成本一分钟的额外时间，如果代码全部均为行。这种差异吗？它是1％，还是0.001％？通常是后者。  
但是发展得更快？一块软件分成逻辑函数，或者是一个单一的墙壁代码文件，没有明显的开始或停止？这种微小的速度降低通常会为您提出一大批易于发展。这是一个有价值的贸易。  
完成代码后，您可以配置它，如果一个函数调用太多次数，则可以在内联函数。通常有一个或两个功能，可占据可观的时间，其余的别是没有。所以在最后优化的是更有效的。  
### 回答 4
当然是一个主要的  
高级软件工程师告诉我不要使函数并拥有我的主要方法，因为它更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？  
遗憾的是在它中，在许多其他人的生活中，你遇到了没有被宣传超越他们的能力的博泽斯，通常是凭借谈论一个良好的谈话。  
除非您的主要值非常短（例如，10到20行），那么将代码分解为更简单的单位，将帮助可辨据和可接受性与接近对性能的无限影响。  
当然，一个主要由每次函数组成的主要函数是两行长度，但除了这种极端情况之外，你是对的，他/她不仅错了，而且没有能力抓住他们的职称。  
### 回答 5
你是。不得不做堆栈的性能是如此小，你可能也不令人费不知它作为增益。但是，可读性的丧失是真正阻碍了您未来的编程团队实际解决任何内容的能力。  
如果在一个环境中的函数调用太多的环境中为您做过，您根本不应该使用高级语言。  
### 回答 6
当您想要展开一切以获得绝对性能时，存在罕见的情况。编程FPGA的人有时会进入这一点。但即使在那里也非常罕见。也许40年前，功能呼叫开销足够重要，以至于人们有时担心它。但是通过现代机器，功能呼叫开销非常小，如果它成为一个问题，则通过引用调用通常会减少它。并且在编程语言中设计用于问题的问题，通常存在内联指令，告诉编译器为您展开它。此外，优化器非常擅长自动完成此内容。  
易变是问题的一个方面。整体问题是验证性和验证。您如何测试您正在构建并验证他们符合其规范的部分。实时编程可能存在特殊情况，其中最高优先级的东西需要在少于x的时钟周期中进行。这是一个特殊的情况，其中定时是正确性规范的一部分，并且在某些角落的情况下，如果它展开，则可以更容易证明代码符合规范的时间部分。实时系统开发人员将更好地对此进行评论。  
### 回答 7
哇，1989年的一个问题，我不知道Quora回来了！  
（认真色：在他们的正确思想中没有人想到2021年的方法调度的开销。好的，除了0.001％的软件工程师外，没有人在超低级内循环非常性能敏感的东西中进行的0.001％  
### 回答 8
我敢肯定的是，在过去几年比几行再此高级软件工程师不写任何程序。  
内联一切速度的提升是negliable，它是由编译器如果可能的话做了。  
如果你的老板告诉你写在一个单一的主功能的一切，你显然必须这样做，但是这将是一个维护的噩梦，也是它使测试相当困难。  
### 回答 9
你说的对。他们不是一名高级。  
除非这是一个巨魔问题。它感觉就像一个，因为它如此完全不可能为我们在我们的行业持续到200条线路或更少的代码的工程。更少促进了。  
这实际上是难以置信的。  
更新：自写这一点以来，我实际上经历过这一点。  
### 回答 10
这是事实，没有通话功能是非常，非常稍快;毕竟CPU具有存储寄存器的状态，更新调用堆栈，调用该方法，然后再次更新调用堆栈和恢复寄存器。这需要的不仅仅是跟随直线路径时更大一些量。然而，有一些参与这一并发症。  
首先，一旦你过去一定规模是不维护;我们的大脑根本就没有这样的。我们有这样的功能，我们可以采取真正的大任务，把它们分解成更小的任务。如果我们真正想要的额外性能，我们可以选择内联函数，其交易少函数调用（快）编译的代码大小（大）。一些编译器自动执行此操作时，它是有道理的，尤其是如果我们杀青的优化级别（长编译时间，更快的执行时间）。  
其次，许多语言中的编译代码条款强加最大功能尺寸。虽然现代系统应该不会有这个问题，这是不是很久以前，一个功能必须适应32KB或64KB内存中。一些有限的存储器装置今日（如嵌入式系统），并设计为便携式的语言，仍可能有类似的限制。要编写可移植的代码，我们应该更喜欢功能。  
三，功能允许我们重用代码。这意味着更少的打字，更小的源代码的大小，且再次，可维护性。如果您发现有一些逻辑，这是复制粘贴100次的错误，你现在必须解决它的100倍。但是，如果你有这样的功能，你修复一次，所有代码受灾地区固定为一次。这是在大型项目中节省大量的时间。  
第四，CPU有一个缓存。在一条直线上写一串代码可能会导致更多的高速缓存未命中，造成比不调用函数相关的获得更多的性能损失。使用功能可减少程序的大小在内存中，使之更容易适应在缓存中。这可以通过50倍或更多字面上加快程序。  
没有高级开发人员会永远这样说严重。如果他们这样做了写代码，他们应该为不称职被解雇。这是一个非常新手犯的错误。功能让我们的生活更容易，并且由于现代计算机的速度不够快，调用的函数是不区分。实际上，CPU可以甚至预见一个函数调用预先，和沿该路径优化代码。  
### 回答 11
这取决于您是否正在进行应用程序开发。由于您提到了主要方法，这听起来是这种情况。对于高级，应用程序开发，您是正确的，可读性非常重要。但是对于低水平固件开发或驱动程序开发，性能（速度，存储占用空间，内存足迹......）可能更多的是驱动力。  
### 回答 12
问：一位高级软件工程师告诉我不要使函数并在我的主要方法中拥有所有代码，因为它更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？  
答：2019年的旧问题，  
在等待谜团展开的谜团，< - 内部笑话。  
我来啦，  
唔…..  
我应该拒绝< - 这是一个笑话，我的大量主要方法为10,000线吗？  
问：一位高级软件工程师告诉我不要使函数并在我的主要方法中拥有所有代码，因为它更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？  
答：2019年的旧问题，  
在等待谜团展开的谜团，< - 内部笑话。  
我来啦，  
唔…..  
我应该拒绝< - 这是一个笑话，我的大量主要方法为10,000线吗？  
现在，回到家里，我可以大声尖叫，我的老板是假装的。  
有趣的事实：  
这是一个假装的问题。  
看，上面，它取决于，哈哈。 （我有一个页面，1级，一个C＃UWP应用程序，哈哈哈哈哈哈哈哈。  
收到消息/笑话.........需要我说更多？ ......  
来自当地语法警察 - >查克掌舵  
一个自我吸收的绅士，  
尽管如此，谢谢你非常笨拙（Hehehe），来自  
我是不是错了。  
### 回答 13
我确实想添加一些东西，因为我认为其他答案缺少了这一点和fa  
我怀疑这是拖必的，因为我不确定任何人都会是这么公平的愚蠢，还有一份工作。  
如果程序非常简单，这可能是更简单的唯一的时间，这实际上是线性操作的简短列表。如果是这种情况，并且性能是关键，那么OS或调度程序中的初始化成本将远远超过运行程序的成本。因此，从根本上讲，申请结构是错误的，开销过度，这可能不是一个优化的解决方案。  
我确实想要添加一些东西，因为我认为其他答案失踪了这一点，并落入了同样的思想陷阱，就像这个'高级'一样。这实际上不太可能更快地运行。功能不仅仅是代码组织，它们表示可以在需要时执行的可调用堆栈的操作。如果您将所有逻辑放在主要方法中，则您实际上是在应用程序中强制迫使应用程序中的所有可能的操作添加到呼叫堆栈中。虽然这大部分可能最终展开，但这仍然需要一些处理器时间。在大多数典型成功运行中的大多数应用程序中，大量操作将永远不会在呼叫堆栈上进行特征。您还使用您不需要的缓存内存，扩展当地人的寿命，处理器时间不是唯一的重要资源。  
这为我们带来了现代世界的另一个问题。资源管理。您可能有一个操作系统和处理器，能够运行多个线程（并不总是如此知道的情况，所以这有点态度，虽然是99％的时间）。如果没有函数调用，您无法利用并行性，并且与大量堆栈框架相似的内容切换将沉重。您正在难以在OS级别优化OS级别，并且在等待访问慢速资源时可能只是阻止。通过卡在进入点方法中，您限制了最佳执行操作的系统能力。现代处理器充满优化，您将有效地阻止其中许多单片代码。  
这就是为什么绕过对目标硬件如何运行的低水平了解经常导致一些愚蠢的误解，这在实践中难以困扰。绝大多数开发人员没有CONT编译器的另一面的线索。这是危险的，我们喜欢相信它并不重要，但它确实如此。我也同意所有其他人，除非您正在编写在天空领域运行的代码，那么维护您的单片代码的成本将绝对削弱额外的0.1％的硬件配置的成本，您需要使这是一个非问题。这个“高级”应该被解雇，没有希望能够在他们认为这是合理的。我实际上遇到了这个顽固的人，他们逼真地花了那些雇用这么多痛苦和痛苦的公司。  
### 回答 14
A2A。  
两个都。  
如果你需要绝对速度，内联函数可以节省几微秒。之前我40+年前加入这个行业时的CPU运行在为0.5MHz，这是必要的。今天我就不会认为这是在大多数情况下，有利我们的处理器，运行速度快5000倍。这就是所谓的骨干或脊柱结构，并着手结构化设计。  
也许一个（老化）的Arduino具有在8MHz不同的要求。但即使在那里，人们可以很容易地在时钟频率72MHz以上以较低的成本进行交易，以ARM处理器。所以，就没有真正需要做到这一点。  
因此，第一个解决方案，尽管它correctne  
A2A。  
两个都。  
如果你需要绝对速度，内联函数可以节省几微秒。之前我40+年前加入这个行业时的CPU运行在为0.5MHz，这是必要的。今天我就不会认为这是在大多数情况下，有利我们的处理器，运行速度快5000倍。这就是所谓的骨干或脊柱结构，并着手结构化设计。  
也许一个（老化）的Arduino具有在8MHz不同的要求。但即使在那里，人们可以很容易地在时钟频率72MHz以上以较低的成本进行交易，以ARM处理器。所以，就没有真正需要做到这一点。  
因此，第一个解决方案，尽管它的正确性是过时的，而且在大多数情况下，已经过时了。  
第二，现在更有意义的是硬件成本下降，因为我们更感兴趣的是管理开发时间比在大多数情况下，优化的执行时间几纳秒。  
在这种情况下，速度是一个问题，内联是有用的，但我会利用宏观部件的汇编，或inline关键字在C完成同样的事情，但保持较好的组织和可读的代码。  
如果“它的速度更快”车手是关键，那么你就需要在编译器使用的优化器。这些作为，理查德Godivala指出了他的评论是现在，他们击败了所有，但最好的程序员的水平，甚至他们有问题跟上硬件和软件的新技巧，优化编译器利用透明。  
装配解决方案是不可能的了今天，在10000的代码20年前也许，但即使如此，通常只有几行也很少主程序甚至40年前。  
我遇到了一个这样的野兽，然后，它是100页，花了18个月编写和充满错误和有限的功能。我在COBOL（是的！）在2天（*？）重新写，这是更快（是的是的！），无bug（万岁！），并附加功能的用户本来想多年（耶！）。我的经理恨我吧 - 他是原作者:-(我没做什么特别的。  
当需要内联在中断服务程序剃几个指令和优化编译器不可用我仍然会碰到的情况。  
我放弃了组装25年前比，当我在不具有现有技术优化的状态FORTH写的ISR等。我宁愿选择一个更快的处理器，并利用来回拿到手，然后重写（并行）在C ++中。它有时快让我在所述的微处理器发挥是由于它的互动性。 $ 2.00为更快的处理器是值得我的时间只有几分钟。  
### 回答 15
他还送你去找左手螺丝刀吗？  
抛弃幽默，我觉得很难相信他是高级软件工程师。我的意思是，也许他的老板，谁也是他的叔叔，给了他这个头衔。但他绝对不是技能的高级软件工程师。  
### 回答 16
这两个观点都有一些真相，但对于非琐碎，现实世界的开发项目，您比其他软件工程师更正确。  
考虑唐纳德Knuth，计算机编程系列艺术作者的以下声明：  
程序员浪费了大量时间思考，或担心他们的计划的非关键部分的速度，并且这些尝试在考虑调试和维护时实际上具有强烈的负面影响。我们应该忘记小的效率，比如约97％的时间：过早优化是万恶之源。然而，我们不应该在那个关键的3％中传递我们的机会。  
 -  Donald Knuth，1974年[重点添加]  
任何非琐碎的现实世界软件开发项目中的默认方法应该是开发高度可读，可维护的代码。然后，只有这样，测量性能并寻找性能热点，保持性能要求（您的项目有那些，对右边？）始终想到。专注于优化那些热点。然后，重复测量/优化周期，直到您达到或刚超过您的性能要求。然后停止优化，除非拧紧性能要求。  
当然，通过呼叫和从函数返回来产生一些开销。呼叫约定是否在堆栈或寄存器中传递了东西并不重要......将涉及到开销。如果您的编译器支持它，并且如果您的函数很小，并且足够简单，则可以通过使用内联功能来解决这些问题。 [注意：#define宏也可用于避免函数调用开销，但我不建议使用该方法。如果你不知道你在做什么（即使你知道你在做什么），那里有太多的陷阱。]  
从纯粹的性能角度来看，函数调用通常是速度和内存足迹之间的权衡。显然，在三个不同的地方调用一个函数比放置在每个呼叫站点上的代码副本略微慢，但这样做也将使用更多内存。如果足迹更大，这可以减慢性能，因为它可以影响地区，缓存，分页等。事实是，您只是不知道在实际测量之前的性能问题。  
完全放弃源代码的可维护性，始终将所有内容放入一个单片功能不是一个很好的默认方法。这对非常小的，琐碎的程序来说只有良好的。现在，一些小型嵌入式系统使用非常少量的软件来完成作业（例如，读取单个传感器并更新显示的值），因此在某些情况下，一切都可以舒适地放入单个单片功能而不损害可维护性。这将被视为一个琐碎的软件项目。但今天绝大多数软件和固件都比这更复杂。  
维护阶段在其使用寿命期间占软件的80％或更多。如果您不编写高度可读，可维护的代码，则将巨额成本负担推入维护阶段，这意味着您的软件的整体成本上升了80％或更多。  
一般来说，没有任何邪恶的优化。但是以牺牲可维护性为代价而过早优化，与非琐碎，现实世界的软件项目的良好（又名邪恶）相反。开发可读，可维护的代码。然后测量并优化问题区域，针对您的项目的实际性能要求。  
### 回答 17
两者都是正确的，但你比你的高级软件工程师更正确。我会告诉你为什么？  
当您从主代码调用函数时，执行将当前上下文（地址和寄存器）推向堆栈，程序计数器已加载功能地址以呼叫功能。从函数返回时，从堆栈中弹出上下文，以继续在主代码中执行。这增加了一些额外的推动，流行周期，因此增加了一些基于您的PR ...  
### 回答 18
第一个问题是，可以只用一个主要方法写入所有程序吗？  
我不这么认为，这里有一些笔记：  
我相信高级开发商正在与你一起笑话！或者你正在制作这样的故事来拥有这个问题。  
### 回答 19
这种思维可能在20世纪60年代恢复了一些价值，在计算机大型器上运行。  
如今，最重要的速度因子是处理器通过其预测管道运行代码的能力，并从内部缓存访问代码。  
如果您在单片片中编写整个程序，则无法在现代计算机上飞行。  
它甚至会变得更慢，因为CPU将在RAM，缓存和REGI之间不断地铲起小位，因为  
### 回答 20
在我的专业领域，它不会有意义。但是，我可以想象速度在可维护性方面超过一个优势的区域。  
采用例如纳米波特或信号处理。如果您的软件是瓶颈，您可以通过装箱以主要方法包装所有逻辑来提高性能或吞吐量20％，为什么不呢？  
它真的取决于应用程序。您应该首先要求高级软件工程师更具体，并更好地解释决定背后的原因是什么。  
### 回答 21
除非您正在编写在非常有限的硬件资源上运行的嵌入式代码......我认为写入可维护性的，可读代码更重要地编写超高效代码。一方面，这取决于所使用的语言。如果您使用的是编译的语言，编译器和链接器将为您提供一些优化。除此之外，您每次运行所述代码的时间可能会在现代硬件上忽略不计。  
对我来说听起来像你的高级被你吓倒，只是想告诉你要做什么才能对自己感觉更好。  
### 回答 22
有可能是合法的情况下，你的高级会是正确的，但是...  
在时间至少99％，你会不会在这些案件之一。我需要更多详细的项目给出更明确的答案，但有机会，你可能是正确的。  
首先，不可读的代码是一般越野车和未优化。的确有函数调用的性能损失，但如果你不能确定为O（n ^ 2）算法被用来在你的代码的地方，可以通过一个被O（N *的log（n））的算法，函数调用量将真正成为至少你的性能问题。这同样适用于识别重要的I / O瓶颈，潜在螺纹锁固网站等设计更好的协调代码线程实际上是不可能的。所有这些都已经没有去整体非常困难。  
和修复bug肯定会意味着你必须到处都是函数内联应用相同的修复。不同之处在于没有办法知道这些地方会是这样，甚至与你最大的努力，一个重要的情况下可能会被错过，导致错误做更大的危害，或变得更加难以追踪。而且错误也可能导致的性能损失，数据丢失或严重故障。再次，从函数调用的性能损失会相比，这是出奇地低。  
其次，函数调用可以通过底层语言进行优化。如果您使用的编译语言，编译器可以决定自动内联一些功能无论如何，这甚至有可能暗示它内联您所选择的选择功能。  
在另一方面，如果你使用的是解释或混合语言，从函数调用的性能损失会比从解释的处罚，首先是微不足道的。即使如此，功能给出解释或VM跟踪执行热点进行JIT编译一个很好的提示。否则，它只能跟踪环路，这可能会在重要的优化机会的丢失。  
第三，在现代编程语言，任何不是一个函数是不是你可以独立调用。这将使测试软件是站不住脚的。如果代码有4个分支的功能，一旦你确认它们正常范围内的功能参数来工作，一切都很好。你只需要确保该函数正确调用，并远离这些案件抽象的最大多数其他测试。一种单片代码必须次测试这些4个分支的可能的代码路径中的所有其他分支。如果不是这样，很多重要的情况下，肯定会被错过。要么，你回去使用goto语句，这仍然是非常糟糕的。  
我怀疑，如果性能是至关重要的应用程序，他会愿意不进行函数调用，他就不能没有测试每个代码路径的性能瓶颈。测试是否是手动的出了问题，写自动化测试的许多代码路径很可能是它自己的噩梦。他最好是愿意支付一个更大的开发团队，以及一个非常大的服务器场得到合理的时间内运行这些测试。  
我能想到的一些合理的情况是：  
### 回答 23
在50年前，我们不得不计算时钟周期并写入封闭机器代码，最大限度地使用寄存器来使东西完全运行，这是一个慢的加工器和小/慢记忆的小/慢记忆。但是，现代优化编译器会照顾大量转换功能，以加入内联代码和展开循环，因此程序员可以自由地编写人类可读代码，而不是担心函数调用开销。有很多其他最佳实践可以减少不必要的......  
### 回答 24
你说的对。在简单的投他们可能会产生类似的机器代码。更糟的是，你是资深的提议实际上是慢的代码变得更加复杂。  
现代编译器是聪明的，我说的是真的聪明。但是，计算机具有的内存数量有限速度有限。利用良好的封装和整洁的代码将限制工作集，编译器需要工作，这将是能够执行扎痛的优化，这将产生更快的代码。  
在简单情况下，编译器将能够在网上所有的代码，并会产生相同的代码无论哪种方式，但你的代码会更容易理解。  
### 回答 25
我认为，这使得代码太不可读的，多余的，而凌乱不是唯一的问题。  
相对于分析师，开发人员，设计师等称号软件工程师并没有透露太多有关情况。有时缺乏工人不能因其他问题被终止，唯一的解决办法是推动到一个位置，他/她至少可以做的损害，或做一个横向转移。也有对平台和语言使用的信息。这是关于商业计算机商业应用程序，或者这是关于应用程序正在为拥有有限的资源和最低的功率要求的嵌入式系统开发，如家电或家庭恒温器。  
根据您的环境，一个子程序调用（或函数或方法或模块）可能只是涉及跳转到某个地方，保存几寄存器，做的东西，恢复寄存器，东回跳。开销应该是最小的。如果你是一个有点傲慢与参数/参数类型匹配，也可能涉及到一些的thunk。多一点的开销。如果你的整个应用程序不适合到内存一次，那么功能使用可能意味着成千上万的额外的指令来调用交换/分页以及磁盘活动和等待时间，直到函数开始。但是，可以在不函数调用仍会发生。您可能仍然必须处理交换/分页当你的整个可执行文件，不装入内存。那随时都可能发生你的程序达到交换大小页面的结束和下一个instrution尚未在内存中。  
使用子程序可以减少应用程序的整体规模，减少应用程序的大小可能意味着更少的交换。如果你设计你的功能，系统就不会换出个你最常用的功能经常。  
嵌入式系统可以在内存中（鼓励子程序使用）相对较低，也可能需要实时响应的是排除了额外的代码执行时间（鼓励内置），特别是如果该软件包含中断处理程序可以非常时间敏感的。在另一方面，CPU可以是非常快的这些天，内存很便宜，但他们也将有更大的动力需求。  
### 回答 26
该工程师不是老年人而是老年人。如果您以编译语言编程，则现代编译器将在线内联。如果您无法使用编译的语言工作，您显然不在乎运行时速度。  
通过避免函数调用节省时间的想法可能在某些情况下在30年前的某些情况下具有相关，但即便如此，在几乎所有情况下都不值得降低可读性和可维护性。  
### 回答 27
一些好的回复在这里，但在性能优化工作后，我倾向于一般信任的编译器。编译器是令人难以置信的复杂，而且往往这些天，编译器可以使程序更快地商讨如何一个特定的代码块运行更多的上下文信息。即使在线keyworda被忽略这些天，编译器始终基于优化的标准是速度，还是速度和快速地（与forceinline压倒一切，如果你确实需要）作出的节拍判断。  
你很快就会发现，随机微优化的作品很少，在多数情况下与差异仅仅归结为随机变化。要真正使代码运行速度更快，功能是否使用与否在很大程度上是无关紧要的后编译。你需要了解什么是在低级别发生的，并且这些代码如何被瓶颈。  
改进高速缓存利用率，分组的指令，使得超标量体系结构可以并行执行非相关的指令，减少资源争用，避免copys等;所有有更多的好处。  
这是从来没有值得尝试欺骗编译器和牺牲可维护性或可读性，优化应该永远是明智决策的过程。确定一段代码，这是慢，理解为什么它是缓慢的（内存问题，吞吐量，缺乏硬件饱和度/占用等;）然后再考虑解决方法的影响，最重要的衡量你的结果。  
如果你不衡量，你不知道。我建议实际上剖析代码下一次和比较数字，如果有的话，只是证据证明该工程师错误。 - 正如你正确的建议，你不想牺牲可维护性。 - 它永远只能是值得的，如果涨幅可测量显著。同样，一个代码库的大部分地区都不值得花时间去手动优化，将会有更为低挂水果从优化的代码重量级部分，比潜在削去0.01％关闭所有的你买回来60％的性能。  
这是完全有可能在某些编程语言/环境，这些东西仍然相关，但我怀疑这是这里的情况。  
### 回答 28
这对Web开发中的CSS甚至是JavaScript的长时间参数，但我从未听说过Java，PHP，C ++等。他正在看着码比，好像他将成为唯一改变或更新代码的工程师。实际上，您根据其功能将代码分解为类，并在需要时扩展/导入它们。  
这位工程师是否具有计算机科学的正式学位？我会认为如果他这样做，那么他会知道有时你需要牺牲速度的速度。  
### 回答 29
您是对的，任何促进一个迷信的公司，就像高级工程师一样，您应该尽快逃避。  
### 回答 30
他想读主要，从头到看结果  
很高兴能够知道程序的绝对程序序列。您知道第100行发生在第110行发生的情况下发生了什么。  
一些程序可以这样工作。玩具程序，单个工具程序，充当数据变换功能的程序输入→变换→输出。  
有时可以击中妥协：该程序具有功能，但在再次使用之前，所有结果返回主要。函数可以调用其他函数，但任何用户数据结果在任何其他处理之前都会回到主要。  
他想读到主要，从头到尾看结果。他并不意味着你应该创造一个巨大的主要功能，并跳到gotos。  
他希望确保他能以主要追溯该计划，而且不必去调试某些其他文件，该计划做了一堆工作和退出。  
他可能会强迫你作为一项练习来编写一些紧凑型逻辑紧张的代码。可能有担心以前的编码人员对他的生活困难的代码依赖关系，他想避免这种情况。  
取决于用例，他可能会离开他的脑袋。你能得到第二个意见吗？  
更快，更快地陷入灾难  
真的，它不是更快的不符合职能调用。在纳秒中测量计算机花费创建堆栈帧和设置局部变量的时间。然而，可能需要几毫秒的是分配动态内存对象，以及处理异常，并加载OS上未加载的共享库，以及读写文件。因此，如果速度是一个问题，请尝试避免任何大尺寸或大部分的动态内存分配，因为您也必须释放它们。大多数程序都可以使用静态分配的缓冲区进行大多数存储，因此如果在程序上向上分配它们时，则在程序上将在运行时不必进行程序，并且操作系统内核将不会在程序中不可预测的时间等待在内核中等待。转到您的过程中，然后搜索其免费商店并为您分配一些。当所当所取决于系统负载，过程优先级和无金额，以及每次流程限制。有些关键和安全系统禁止在可能需要瞬时动作的敏感代码区域中的任何动态内存分配，以防止丢失生命或肢体，或破坏硬件，实时关键响应或硬件中断处理。  
一旦加载共享库，它们就在RAM中并像任何其他代码一样快地运行，但后来你真的不知道它们中的内容通常是什么，或者他们可能需要什么代码路径。如果慢速似乎不来自您的代码，则可以跟踪执行，但从您的代码正在使用的某些库。  
到目前为止，最慢的瓶颈几乎总是通过文件系统的I / O。 （网络等待状态和拥塞可能会发生，并且也令人沮丧地缓慢）。尝试不必打开和读取和写入文件，除了程序的开头和结尾，或至少加载，尽可能多地加载。您必须少次返回文件I / O的次数越快，您的程序将完成。  
我喜欢做的一件事是在它上面的主要功能中使用的每个外部函数，并提供函数原型，并简要说明，包括它来自的文件。这为读者提供了一个非正式索引，并帮助您导航源代码库。存在许多更复杂的代码库导航工具。我更喜欢在大多数小程序中排列一行。  
大多数人忘记的一个速度技巧是为平台选择最快的编译器。它可能是一个预算的Buster，但我在GCC上的PGI C编译器上编译的相同代码之间看到了10％至20％的加速。英特尔在非Microsoft代码上击败GCC和MSVC。但成本很高。我想，英特尔和PGI有免费版本来测试。  
更新  
### 回答 31
你是针对实时性能的编码吗？一般来说，我会说在几乎所有的情况下，可读性，更重要的是，可维护性，胜过任何关于函数调用的论据过于昂贵。如果高级工程师坚持，您可以始终使用C预处理器#define机制进行内联函数调用。由于在#define中使用的任何参数，我都不喜欢这些，因为#define中使用的任何参数都会重新评估（因为#define函数只是字符串替换），但它是使用更多使用更多的程序记忆。这总是折衷。  
### 回答 32
没有艰难的规则告诉你如何组织代码。这是一个平衡的行为。  
没有函数调用的代码肯定会更快但更难以维护。具有每个原子操作的功能调用的代码可能更容易维护，但也较慢。有时速度很重要。  
在这两个极端之间，您需要运行的位置取决于许多参数，并且不可能告诉您到底该参数或谁是正确的，而不是知道这些参数。  
如果您在PC或类似的平台上，则速度可能不是问题。如果是，请先查看您的其他代码，而不是函数调用，以便改进。  
如果您在嵌入式环境中为微控制器代码，情况可能非常不同，并且内联可能是去的方式。您可以将代码的块与良好标题分开，它将随着作为函数实现的代码而易于阅读。  
有没有片上存储器的微控制器，因此每个功能条目和退出的多个堆栈访问都是外部存储器访问。它们并不便宜，并且可以迅速成为执行时间的大百分比。即使百分比不大，但代码在SEEN 1.1 MS时执行，当规范允许900件我们时，您必须考虑减少呼叫数量。  
直到你培养一种有效的感觉，并且不会衡量表现：  
使用尽可能准确地写一些小型代码代表您的最终项目。使用函数实现它。测量执行时间。然后将函数转换为内联代码并再次测量时间。看看差异。外推到完整的应用程序大小，看看您是否可以使用函数满足规范。向您的高级同事展示调查结果并讨论。  
最终，您将成为一名高级工程师，告诉新的工程师如何编写代码。该资历应伴随着一些知识，并且知识应该来自测量和事实，而不是基于正确的方式。  
### 回答 33
高级的高级应该被解雇出错。您应该在此处询问您，因为可以使用一个非常简单的基准显示，引入某些功能不会在大多数情况下更改最终结果。  
开玩笑。说真的，如果该公司的技能水平是那么糟糕，你也可以尝试获得不同的工作。  
问题也高度取决于正在使用的编程语言 - 例如Java据说有一个字节大小的函数限制 - 但我不确定它。  
通常，5％的代码中经常优化可以非常改变速度。  
常见建议不是为了优化太耳  
高级的高级应该被解雇出错。您应该在此处询问您，因为可以使用一个非常简单的基准显示，引入某些功能不会在大多数情况下更改最终结果。  
开玩笑。说真的，如果该公司的技能水平是那么糟糕，你也可以尝试获得不同的工作。  
问题也高度取决于正在使用的编程语言 - 例如Java据说有一个字节大小的函数限制 - 但我不确定它。  
通常，5％的代码中经常优化可以非常改变速度。  
常见建议不是为了优化太早。  
### 回答 34
除了其他答案之外：  
在线 - 一切方法都会导致效率低下的点，这将损害CPU绑定性能。  
想象一下，通过使用和重用函数，即主动使用的应用程序，操作系统内核和驱动程序的代码和数据工作集都适合处理器缓存。表现会很棒。即使命中率仅在90+百分比范围内，性能也会出色。  
想象一下，内在的内容导致缓存命中率下降一点，从说95％到94％。这意味着未命中率上升了20％（从5％到6％）。随着内存访问需要50 ..比缓存命中的时间长100倍，这将是一个非常明显的影响。  
如果一切以前适合缓存，现在甚至有1％的错过率，影响就会非常痛苦。  
### 回答 35
你们都没有完全正确。  
您的高级工程师在物质和Mertis中最肯定是错误的。许多语言将在线代码，因此将代码函数中的运行时间成本在许多情况下为零。  
你大多是正确的，但我的问题是，虽然可读性很重要，但它只是可维护性的尺寸。我争辩的规则应该争取是要将单一概念封装到函数中。 Maiin（）函数的概念是执行该程序，随着事项的发展可能成为多种概念。因此，主要函数应该是发射器，它不应该有任何其他逻辑。即，它可能对执行程序工作的函数有一个函数调用。  
### 回答 36
取决于情况，是这种代码，一种方式与其他开发人员/工程师的想法以及这是如何运行的方法，或者是这个代码运行一次，几乎没有时间扔掉。  
没有上下文，你和他都是对的。  
### 回答 37
这是假的问题，或者高级工程师被误解或缺少某些背景。  
### 回答 38
只需将所有函数都标记在线并在一次上编译它，您将获得相同的效果。  
### 回答 39
你的高级是无能的。如果认为它有利于性能，则任何现代编译器都可以为同样的效果提供同样的效果。在另一只手上，过度的手动内联可能会伤害性能，并且没有任何作用者可以逼真地了解它。  
如果误，则每个编译器都有意味着强迫内联。手头有零零的原因。  
### 回答 40
您的经理可能是一位古老的学校基本程序员，他们想要制作所有变量全球，并将他的所有代码放在主程序中，因为这就是他知道如何做的事。节省的边缘（可能）储蓄的执行速度超过了内存成本，清晰度和模块化的损失，以及引入交互错误（对于N个代码行的顺序N ^ 2）。拇指规则是使您的功能大大，但没有更大。此外，如果您发现自己编写大循环，或重复代码的块，请考虑编写一些功能（并将参数传递给那些）来实现相同的结果。  
### 回答 41
所以，如果你正在使用的语言具有良好的优化，你的  
除非你在涉及，比如，汇编代码一些非常低级的情况是，我怀疑你。  
在某些情况下，内联代码将通过让直接通过没有许多分支运行CPU提升性能;在其他国家，分离代码插入功能更好，因为它减少代码大小，并保持被不必要地加载到CPU高速缓存冷（不太可能）路径。在实践中，良好的优化器会非常应该何时内联或大纲代码，治疗你的功能仅仅是建议，自己的决定。  
所以，如果你使用的是与良好的优化语言，你对功能组织的决定不会对性能产生很大的影响。如果你不使用具有良好的优化语言，内联的决定是至少你的性能问题。  
### 回答 42
在软件设计中，实际上并不是很多真正的黑白权利和错误。  
一切都是权衡。  
如果您需要最大的表现，如果没有人必须维护您的高级人员想要的乱七八糟，则可以将所有内容置于主要。在每种情况下，有很多原因，你应该先寻求最具表现力和可维护的解决方案。  
一般来说，只有一旦您演示了，您只能优化您真正需要它。 （这意味着您已经违反了某种性能约束或要求，并且您已经证明有问题的代码是性能问题的来源。）  
### 回答 43
然后使它  
因为它的速度几乎总是一个可怕的原因在2019年编译器做任何事情的软件是优秀的，在优化掉这样的事情，和99次中有100它wouldnt有所作为的价值在现代硬件反正测量。  
首先使它工作，因为代码不工作是没有好给任何人。  
然后，使其漂亮。折射的可读性，总是以为你会喜欢上它再次6个月工作的平均时间没有见过它。如果你觉得代码心不是清楚足以让那么容易，折射。如果你不能折射，使其更清晰，注释  
然后使之快。如果它的速度不够快已经，独自离开好了，如果它不那么，你开始分析，寻找瓶颈。 9倍的10这一步是不必要的，我怀疑你会发现过哪里，使差的优化是写在main方法的整个应用程序的情况下。  
### 回答 44
高级软件工程师说愚蠢的东西......  
你为什么要听这个废话。  
有很少的情况，这可能是必要的。几乎所有这些都在操作系统中。你猜怎么着？O S程序被分解为大量的模块和功能......  
### 回答 45
您的程序对您的程序运行1纳秒更快（如果偶数）或者您不花费几个小时来寻找错误或每次需要调整代码时，您的程序  
### 回答 46
您可以轻松提高软件性能而不会牺牲可维护性，采用某种分布式系统架构，如增加数量  
高级家伙正在谈论的执行速度是非常不可能的，除非您正在开发延迟至微秒的低级系统，否则最重要的事项。这些系统的示例是CERN的LHC周围的粒子检测器，其中每7个纳秒（40 MHz）和软件需要快速检查数据，以便决定是否有用。  
您可以轻松提高软件性能，而不会牺牲可维护性，采用某种分布式系统架构，如增加处理单元，多线程等。如果您的代码遵循良好的设计原则和模式，这将很容易实现。  
### 回答 47
我认为这位开发人员需要他的头部检查。很少有时间让这个极端将使你的代码更快地运行。这绝对是一个关于预优化的引用的区域。  
在我的经验中，重构使您的代码更快地运行，而不是较慢。  
### 回答 48
编译器是很酷的事情，如果认为这会更有效，通常会内联功能。在大多数情况下，自从我是初级开发人员以来，写作单片代码并不是一个明智的设计选择。即使是回来，它通常是因为每个应用程序都有非常具体的东西，通常由一个或两个程序员维护，并将它们一起流水，以制作更复杂的应用。  
### 回答 49
除非您正在处理非常特殊的案例。  
无论如何，大多数应用程序也都是绑定的。如果您使用的是文件或数据库，并且想要更多的性能，请查看IO 1st。  
而且所有人都记得Knuth所说的：过早优化是所有邪恶的根源，所以如果它不能满足性能目标，你可以处理那种问题。  
### 回答 50
已经回到了八十年代，我读了一些关于它的东西：  
如果您需要重复某些内容，请制作过程或功能;即使没有，也要考虑将代码分开以获得可读性。  
如果您只需要获得几个循环，您应该考虑跃入主要。如果是这样的问题，那么也应该考虑使用ASM。  
如果编译器做好工作，创建功能或者在二进制文件中可能没有影响。  
### 回答 51
A2A。高级工程师听起来非常疯狂。如果您将所有内容置于Main：优化器在适当的情况下，它不会更快地执行。  
它肯定会使您的代码不可读，不明智和不扩展。  
这些优化（内嵌）最好留给优化编译器。  
### 回答 52
你说的对。功能分解是一种古老的形式但可行的方式，将大问题分成小型管理。  
我假设相同的软件工程师将反对面向对象的analysys和分解。不仅是通过VTABLES的功能而是间接呼叫。  
将大块代码分成更简单的块的原因应该是显而易见的。我的建议谨此寻求那位高级软件工程师，他可能没有你的最佳利益。  
### 回答 53
你让高级软件工程师做到这一点为自己一段时间，那么你就知道谁是正确的，谁在使用他人的奴隶劳动是违法的。  
然而在实践中并非如此简单，因为你可能会被解雇从高级软件工程师拒绝工作......不过，奴工是奴隶劳动。  
一旦我是从事芯片设计项目，其中算法工程师也采用了这种方法，它是在C，并且没有函数的参数没有返回类型，一切都通过一个变量的全球云全球沟通，使用相同的参数，这是必要的速度。更糟糕的是，每一个全局变量已经编有号码，LXXX，例如，L245是为了保护它侵犯知识产权的窃取...  
再由上级管理层认为这将是很容易将其转换为VHDL，其中每一个通信是明确的，所以你需要搞清楚整个事情经过全球云的沟通方式，对比LXXX号。相同数量意味着有一个连接，那么所有你需要做的是从大约输出和输入的C代码搞清楚。  
不用说，这是完全没有的乐趣，但一旦你有你的奴隶总是把工作做好，这并不意味着管理是正确的。此外，如果管理或高级软件工程师表现出这种水平的思维，有机会，他们已经成为了他们的职称和职位背后隐藏颓废而没有真正做他们的工作权利。这不是简单的事情对这个东西没有进入的问题，但还是有这些情况下，整个工作环境变得完全疯了，然后你需要拔出插头对他们的心理健康和福祉的缘故你的同事，在大家害怕失去他们的工作...  
如果情况不是严重的，也许你可以建议买一个快速的电脑，对于速度，因为它仍有待观察这种原始的说法是否真的在年底成立。比如，也许你可以模拟一个长一点，而不是在全部测试设计过程中有一年的延迟或更长的时间，而芯片设计人员误用为奴隶...  
### 回答 54
如果您正在运行的时间敏感，则代码可能会更快地运行，如果您可以在线代码，但只有您可以适应  
真的吗？在TDSP和OOP中，创建小字节（是是编程笑话）的函数是标准过程。希望您可以尽可能使用语言或公司库中的现有程序。您的主程序基本上只有其它逻辑。然后，下一个级别应该具有处理每个功能区域的逻辑，然后可以在该级别甚至更低的级别功能代码处完成实际的大升降。  
如果您运行的内容敏感，则代码可能会更快地运行，如果您可以在线代码，但只有您可以将其放在一个内存页面中，但通常这不是SOP。  
### 回答 55
答案可能介绍编译器的写入方式，也可能依赖于代码。  
冗余代码也比调用函数快一些倍，但是......这也可能取决于编译器的作业如何。它还取决于其自我的代码。  
你的问题也有些模糊，因为你问了使用泛型的问题，因为我们没有什么可继续。  
### 回答 56
除非您在某些专业的利基（如实时处理或嵌入式编程）中，否则更好地远离高级软件工程师  
A2A.  
### 回答 57
忘记谁是对的。如果有那种编码技能的人被称为贵公司的高级软件工程师，则会运行。甚至不等着说再见 - 只要找到另一份工作并运行。所谓的高级软件工程师从未在他/她的一生中写下玩具作业之外的任何实际软件 - 因此令人难以置信的无知。雇用这次延迟的公司很快就业。  
### 回答 58
这纯粹取决于函数的完成程度。如果您正在编写函数，请添加2个数字，然后是那个矫枉过正。函数调用的开销不合理。  
但是，如果该功能实现了实质性的工作，则将其作为函数使其有意义。  
在没有审议利弊的情况下，内联一切，是愚蠢的人。  
您现在可以在您的内容中进行评估。  
### 回答 59
关于这种愚蠢，我很多时代听到了这一点：我们烧钱以拯救一些便士。  
只是不要。忽略可能的仁慈的恐龙，用几个参数和可读代码坚持你的短函数，让编译器做编译器的工作是什么。编译器将根据需要加入内联的东西，如果支持，则尾部呼叫递归，因此堆栈不会全部用尽（读入它），等等。  
顺便说一句，如果它被称为方法而不是功能，这里显然是腥味......  
### 回答 60
没有冒犯但是......为什么你甚至要这样做？你真的是前程序员吗？真正的程序员可能不太关心Wuo告诉你如何完成你的工作，你应该首先重新开始我们开始编码，因为我们没有像那里发布的工具，我们制作了我们的owm  
### 回答 61
它非常简单，如果代码很小，就像一个小型应用程序，那样简单，功能就没有点。如果代码较大，并且您的应用程序执行多件事，将其组织成功能。如果代码甚至更大，你应该将其组织成对象。也是速度的东西，如果你试图做一些简单的事情（ex。很多迭代，但单个算法）足够快，你知道代码没有需要太多维护，功能或物体中没有点。  
### 回答 62
任何方案都应用一种语言编写的程序，其中优化编译器仍然无关紧要。  
此外，任何人都说那不是高级软件工程师。  
### 回答 63
这是什么语言？在C ++中，您可以在线函数导致它们注入调用代码而不是调用子程序。  
但是，虽然，随着其他人发布，这是一个最佳微量优化。  
### 回答 64
哦，我们可以进一步迈出一步。  
如果你正在寻找速度，你为什么不在装配中写？还是在c？  
现代软件是一种很复杂的方式，这对于那些维持他人编写的代码的人来说是显而易见的。事实上，有一种说法是这样的：代码以这样的方式，即最终维护你的代码的人是一个剧烈的精神病患者，他们知道你住在哪里。  
现代软件是权衡游戏。您牺牲了开发速度和可维护性的执行速度。计算地，他是对的。每个功能跳都会引发计算开销，因此影响执行速度。但另一方面，您最终结束了您无法维护的代码 - 意大利面条代码。它打破了固体原则的所有约定。如果您扩展您的团队，则代码库将成为合作的噩梦。我甚至没有去成为一个失败的部分。  
Remeber，软件工程是一个权衡游戏。明智地选择因素。  
### 回答 65
这个建议非常主观。这是什么特定代码应该是什么？它是一些单关控制台应用程序，有一个责任并在Docker实例上运行吗？如果是的话，那可能没事。如果它是企业级产品上的某种Web API，那么他的建议也不会很好。  
在那里有什么可用的东西，并灵活地对您所采取的方法。使用完全吹休息API模式的骨头与服务存储库层最终增加额外的开销。或者它可能会使未来的扩展/集成更加强大。  
### 回答 66
这意味着有问题的人是不是高级软件工程师，声称他是不是值得这个标题，或者这从未发生过。  
### 回答 67
如果一切都需要在一个像程序编码的一个地方询问，那么在Olden的日子里大多遵循的那样，那么使用面向对象的编程......。  
代码Sholud也不仅要保持更快。  
### 回答 68
他必须是漂亮的高级，那么很久以为人们发明了第四届Gen编程语言。  
一般来说，人们考虑方法 - 包括主要方法 - 如果该方法具有超过百条线路，则是不可读的和杂乱。功能的目的是避免冗余。如果一种方法有太多路径，那么它变得难以理解并且更难测试。  
现代编译器检查调用函数的代码，如果更高效，可以考虑将函数调用转换为某些内联代码。今天通常的规则是：编译器是对的。  
他绝对是错的。  
### 回答 69
你的工程师应该退休，因为他不知道他在谈论什么。在80年代留下了Quidbing函数呼叫开销。从那时起，我们已经学会了一两件事。  
### 回答 70
我认为一般来说，将主程序代码分成单独文件的好理由是具有一种代码的可重用性。另一方面是，可以通过测试程序测试包含明确定义的类/函数的这些独立文件，而不会影响主程序。  
### 回答 71
好像是  
在调用函数时，理论上涉及一些涉及的成本，它们是绝对的ministule（除非您决定通过非常大的记忆明智的参数，这是无论如何都不应该做的），如果这些成本对您的软件有任何相关性，否则您的软件非常相关D可能不是首先以更高的语言开发它。  
如果你愿意，这些小型成本仍然不会证明码级是非常可读和可维护的。  
但更重要的是，我写了呼叫职能，理论上有一些成本。那么为什么理论上？  
好吧，因为在代码成为可执行软件之前，有编译器和编译器优化代码，即通过删除任何不必要的步骤，如果您可以在某种程度上编写主要功能，则可以在其中包含任何功能，然后编译器可以也这样做。  
以及优化的一般建议。编译器旨在优化从您的代码（如果需要）的狗屎（如果需要），并且甚至没有考虑的低级优化，并且甚至不明白，如果您看到它们，甚至不会理解。因此，执行这种低级优化是一个只有绝对专家应该手动尝试的领域。否则你会做的东西编译器在最好的情况下是最好的，并且在最坏的情况下你只是搞砸了一切。  
您的部分优化应该是在设计和算法水平上，而不是在这样的低级上，存在专用软件，这比你好多了。  
### 回答 72
如果它没有思考两种方式，那么我们不能说他是对还是错的。  
它曾经有点真实，但这些日子有这样一个惊人的优化器，这么多的翻译级别是长途的方法可以是编写该代码的最慢的方式。  
但无论哪种方式都是真的，但凌乱/不可读。  
重新推荐它到方法，每路几千次运行它，看看谁是对的  
顺便提一句;如果它是I / O绑定，那么您从更好地优化代码的任何性能提升都无关紧要。  
### 回答 73
这是民间传说，而不是事实。回到当天，当200kips是标准的计算机速度时，花费大量时间通过参数并调用子程序实际上很昂贵。今天，最坏情况下的呼叫时间是250picoSeconds，每个参数通过250ps的成本250ps，并且在任何情况下，Superscalar芯片（原样是大多数桌面和笔记本电脑芯片）每250ps都会在两到六个指令之间发出，这意味着平均呼叫时间从125ps变化到40ps，时间太小，无法担心。你说的对。功能有效零成本。不计算编译器inline inline的能力。  
### 回答 74
这是一个优先事项和背景的问题  
在大多数背景下，高级会错了，但可能在时间关键实时编程（例如制动系统或核反应堆控制）的情况下。  
在有限的存储器上下文中，存储器上的存储器可能比速度增益更重要。  
在企业环境维护中，昂贵的维护是非常昂贵的，所以你将是对的。  
您可以使用函数/方法等编写代码，依此类推，并将编译器inline。  
天真地称呼函数的成本几乎总是远低于th  
这是一个优先事项和背景的问题  
在大多数背景下，高级会错了，但可能在时间关键实时编程（例如制动系统或核反应堆控制）的情况下。  
在有限的存储器上下文中，存储器上的存储器可能比速度增益更重要。  
在企业环境维护中，昂贵的维护是非常昂贵的，所以你将是对的。  
您可以使用函数/方法等编写代码，依此类推，并将编译器inline。  
致电函数的成本几乎总是远远小于函数正文中的代码的成本（OK调用java可能是一个例外情况，我不再需要跟踪那样的东西）  
### 回答 75
这是John Carmack不得不说[1]关于内联的代码（它集中在州，而不是表现）：  
<a> [1] </a>  
>通过内联解决的真实敌人是出乎意料的依赖和突变状态，哪种功能编程更直接解决。但是，如果你要做出很多州的变化，让他们全部发生在线确实有优势;你应该不断意识到你正在做的事情的全面恐怖。当它变得太多时间来拍摄时，弄清楚如何将要置于纯功能（并且不要让它们幻灯片倒入杂质！）。  
脚注  
### 回答 76
自1975年以来我一直在各种语言编写的，也做了PA  
原来的问题是，高级软件工程师告诉我，不要让功能和有我所有的代码在我的主要方法，因为它的速度更快。我认为这使得代码方式太不可读，冗余和凌乱。谁是对的？  
你说的对。所谓的高级软件工程师，除了在一个非常小的一组专业的情况下完全错误的。不知道他是谁，或者他的资格是什么，它听起来好像他的思维还停留在20世纪60年代和70年代时的计算周期为溢价。  
自1975年以来我一直在各种语言编程，并且自1980年以来已经做了付费软件的开发。  
这些天来（2021）几乎所有严重的软件开发项目涉及到征服的复杂性。所有人类的努力软件开发涉及复杂的最大范围内，从一个单一的位最多的一个主要信息系统。一般地，此范围内的复杂性涉及一系列的10 ^ 9，即一个十亿的一个因素。  
征服复杂性涉及破坏系统分解成逻辑上相关的模块，即，程序（函数和子程序）和相关数据包。每个模块应该是整个系统的有机组成部分。类似地，更高级别的模块应该被分解成包含的父模块的功能性的部分相干更小的模块。你应该继续这一过程，直到最底层（或多个）每个模块可以在不需要进一步细分可以写为自己的数据和程序的集合。这个过程被称为模块化分解，是现代软件开发的一个非常强大的工具。  
这些天的几乎所有的应用的硬件资源（计算周期，存储器，辅助存储器等）是非常便宜。相反，对于一个软件开发项目中最重要的资源是人的时间和精力。因此，你应该设计你的软件系统，所以它是很容易建立，同样重要的是，易维护那些你以后谁进来。  
另一个考虑是，缺陷密度与程序的尺寸增加，后200行的代码。即，对于200个行代码或更少的程序，缺陷密度（每1000行代码的缺陷数）是大约相同的。上述200行的每过程代码，缺陷密度上升。这是复杂性的程序获取要大的水平不断提高的结果。  
另外一个重要的考虑是，这些天的编译器是优化源代码的速度，可以假定你正在使用一个有效的算法非常好。因此，你应该让有关优化的执行速度，编译器的担心，而是集中精力合理地设计你的程序。  
因此，忘记调用过程，并从中恢复的程序开销。相反，集中在一个逻辑的，合理的方式，很容易为其他人阅读和理解设计程序。  
希望这可以帮助。  
### 回答 77
在普通世界中，你是对的。所以，正如其他人所说，这将是一个非常奇怪的com  
有一些情况是真实的。在粗略的猜测中，它应用于我所写所有代码的0.00001％。例如，当我有67ns完成计算时它应用。另一个场合是当我有256个字节可以实现引导加载程序时，硬件设计所强加的限制。我从未在金融交易的各个方面工作，但我收集了有毫秒计数的各个部分，也许编码是其中之一的情况。  
在普通世界中，你是对的。因此，正如其他人所说，这将是一个非常奇怪的公司，他们将这样的人作为高级软件工程师。我可以认为适当的唯一方法是，如果它不是他或她给予的一般建议，而且一个与我所列的非常具体的情况有关。  
### 回答 78
我认识的工程师谁想到这样。除在非常特殊的情况下，你是绝对正确的。你应该总是让有关这种低级别的方式优化代码的编译器担心。你应该担心使你的代码的维护。  
一个好的优化编译器将尝试与调用这些功能的内联拷贝替换成您的小功能。甚至使的，适合于通过常数，这些常数被注入到克隆的机构具体调用点这些功能的克隆 - 这可以是针对用作循环边界常数特别好。一个好的编译器也将随后展开循环它认为性能是至关重要的。它将交错操作采取目标处理器和内存子系统的最佳优势，等等等等 - 各种聪明的事情，这将使您的应用程序源代码完全不可读如果你键入的，如果甚至有可能在源语言表达。  
如果你正在编写Java，Scala中，这将在JVM上运行等代码，那么所有的赌注都关闭 - 在运行的应用程序会为你除了任何编译器做了优化。  
### 回答 79
不，他没有。没有软件工程师，普通或高级，会产生这种荒谬的建议。  
### 回答 80
您的高级软件工程师是对的。你也是。  
但这不是故事的结尾。当您在10,000行代码（使用所有这些函数）时，您将填写95％的运行时间是250行代码。  
如果您完全优化剩余的9,750行代码，您将在运行时获得最多5％的改进。如果您完全优化了那些250行的分布式代码，您可能会更快地提高20倍的速度。  
专注于那些250行代码，积极优化它们。这是您仍然拥有所有这些函数并使所有优化的区域，以基准更改。然后根据尽可能多的功能，并重新运行基准。您可能会发现通过联系这些函数的性能改进低于信号 - 噪声阈值，因此您不应该派对内联。也就是说，消除功能不会导致加速。  
现代编译器知道许多优化技巧，所以只需清晰，简洁的样式编写代码。  
有了那么说，如果你正在写一个具有最小资源的设备，并且需要在书中使用每种技巧来获取您的代码以满足性能要求，那么减少函数的数量是一个技巧。但只用它作为最后的手段。  
### 回答 81
哦，进来，他没有告诉你。我更倾向于相信这是一个虚伪的QPP答案 - 诱饵问题而不是相信一位高级实际说。  
### 回答 82
当运行速度比维护速度更重要时，时间很好;人们现在比计算机硬件更贵。好吧，99.9％的时间。  
我不得不更改C ++程序的功能。代码是单个主要功能。 3,000行代码。它是由EX-COBOL程序员编写的。  
我所做的第一件事是“划分并征服”，收集和删除碎片分成单独的函数，与CheckiffBrayhas29days *类似的名称*。经过几天后，我理解程序很好地开始进行改变，因为它被划分的划分可以专注于改变所需的比特。  
*我确实从COBOL学习的一件事，特别是在汇编程序中限制为8个字符名称后，是有意义的名称。它避免了我不得不写评论！当您称为Checkiffech CareAs29days的函数时，有人怎么会说'你没有添加评论，说出它的内容吗？  
这是一个咒语，我在一个地方工作'如果函数名称有超过26个字母，Bryan写道'。也许据说让我难堪;如果是，它就没有工作。  
### 回答 83
在主，你是一个很长的路权。  
也许这就是高级的程序世界真正高级和卡住。在功能实在是a.procedure那么它的确是更清楚在一个单一的代码长块的操作的情况。但现在这就是相当罕见的。一个地方，我坚持做这样的说法是会计或银行。我想一个会计能够读取该程序并确认其遵循的规则所需的手动步骤。  
但如果你往下推3-5线功能，另一侧则所有youre做是建设领域特定语言来解决问题。那以自己的方式是不可能有人不familiar.with代码库遵循。作为一个OPS的家伙，我得到的堆栈跟踪，并没有任何lines.make该死的感觉与实际误差是如此之深，you.get通用的东西一样无法打开文件或着读对象。他妈的什么文件？什么他妈的对象？其他堆栈跟踪线没有告诉我任何事情，因为他们都是DSL的功能，我不知道那独特的语言，开发商刚刚发明的。我坚决beleive这种做法纯粹是为了保证持续就业。  
我的函数/方法的限制，通常是一个页面。 15-25行。大足有上下文（尤其是吐有用的错误信息），但小到足以力所能及领悟。如果你不能领会的代码5行以上，那么你不应该做这项工作。  
快点？咩，不是因为80年代中期。  
### 回答 84
我怀疑你的问题不是真的，除非你正在编写一个非常简单的程序  
在垃圾中。最少的函数，阻止您重复代码。如果您已经说了一个10行功能，并且您在应用程序中使用它时，请保存10 *（n-1）代码行。一些功能是普遍存在的数据库操作。  
然后有问题如何实现类或更复杂的变量。每次执行新变量时都需要重复结构和初始化！  
图书馆本身是函数的集合，所以你也不能使用库？  
我怀疑您的问题不是真实的，除非您正在编写一个非常简单的程序，这需要很少重复和复杂性并且不访问资源。  
### 回答 85
有时不应使用函数。可以采取简单的程序和超前事。你好世界将是一个可以在主要编码的程序的示例。  
否则，我很难相信这场据称的谈话发生了。从这一点前，我将行动好像它从未如此。  
### 回答 86
它是关于平衡和长期维护。未提及语言和应用程序类型，因此您更难评论。每条指南都有例外  
如果单个活动超过8-10行，或者重复，则将其移动到函数。  
使用常识 - 我已经看到人们疯狂并创建一次使用的功能，只包含几行。我也看到人们一遍又一遍地去另一个方向并剪切和粘贴代码。  
如果应用程序不仅仅是一个简短的实用程序程序，则应编写代码以进行维护而不是执行速度。除非发现性能问题，否则除非嵌入式系统或类似的发展，否则不要担心微小的性能延迟。在不必要的优化代码中修复错误，您将浪费更多的资金。在优化性能之前，请确保代码工作。还要确保优化真正优化。编译器有很多技巧来优化代码，并且可能无法解除可读性无缘无故。  
### 回答 87
许多优秀的答案在这里。  
底线。不要听他的。他可能在1985年一直右后卫。  
让编译器和优化做好自己的工作。可执行命令流动比该源代码非常不同。  
从技术上讲，他可能是对的。在运行时有一个函数调用少量的开销。但请记住，在多线程服务器，这可能实际上允许操作系统优化的运行时性能。主程序较小。较不频繁使用的功能调出让在最快的内存中最频繁执行的逻辑坐。其他线程可以共享可执行存储器在那里该逻辑坐，其整体产生更好的性能。  
只专注于写作清洁，可靠和易于维护的代码。让编译器，优化，以及OS处理其余部分。  
记住。 CPU和内存比遭受停机调试蹩脚的代码更便宜。  
### 回答 88
绝对的垃圾！你是对的100％。我甚至不想去想这家伙是怎么到这个位置。这里有人说，在99％你是对的 - 我相信你是正确的情况下99.9999％甚至100％。首先，编译器会内联函数，如果这导致其次更好的性能，具有令人难以置信的低水平操作外，增益（如果有的话）将是nanoseconds.I已汇编40年前编写设备驱动程序（因此低水平和1000倍较慢的计算机），甚至然后这种想法的面条代码是愚蠢的并没有给在speed.Much任何优点更加被寄存器代替存储器，技巧（如移位值，而不是相乘的明智使用获得）使用的，而不是内联code.Can你想象内嵌排序比一个很好的排序过程快好例程？  
### 回答 89
有时长功能是清晰的，如果功能作为单纯的分裂和不要让感觉。  
龙，时序逻辑可以有一个相应的长顺序功能和完全的罚款。不分解的另一个好处是，别人可能会认为这是一个非常适合一些问题，他们即使将它称为其不适当的或唯一的逻辑上类似于他们所需要的，但实际上并不是他们想要的东西。  
ID为优化清晰度和正确性，并不会考虑长度非常频繁。  
大主可能心不是速度更快，但可能会更清晰。不能告诉没有看到代码。  
不磕长功能......是大段或长的章节写不好？  
### 回答 90
谁雇用了他作为一个所谓的“软件工程师”？他是计算机科学毕业生的耻辱。  
计算机科学和新计算机语言的所有进步都是可读性，稳定性和良好的结构。  
良好的软件工程始终强调可读性，良好的程序结构与意大利面条代码可以通过几个纳秒运行更快  
如果您想要最快的代码，那么代码在机器代码中，这是最快的，但确保您维护凌乱的代码。  
### 回答 91
起初我想，不，他们没有  
然后我想到了我在软件开发中遇到的所有怪人。  
他们绝对是。  
他们错了。你说得对。  
### 回答 92
你说得对，而且还有更多。  
作为基督教冬指出，有可能是在很窄的情况下，性能有轻微的差别，但是这几乎没有什么事情。  
你的点可以是超出了可读性和冗余的点扩展的途径。除非代码非常琐碎，组织代码，让你非常接近永不重复的东西有助于节省时间的调试和提高可靠性。  
除此之外，在设计，因为它是自己的图书馆是一个宝贵的知识积累技术，该技术一般适用于各种用途。在这种情况下，我是指不只是一个人的知识，而是一个实体企业。  
我会很积极地想你已经讲了一个笑话，一个谎言意，如果你同意会使您。  
这是最好的，你不知道。  
### 回答 93
询问您的高级软件工程师如果在汇编语言中编写代码更好。它会更快。  
### 回答 94
高级软件工程师不是高级，因为他不知道编译器做的优化步骤，以优化速度运行的代码。简而言之：你不需要打扰编译器会为你做的事情:)  
### 回答 95
让我们开始更快。这是一个有趣的断言。您必须知道编译器的INS和OUTS，以知道没有运行大量测试。  
这让我达到了我的实际答案。干净的代码总是更好。你的方法应该做一件事，做得好，没有副作用。没有绝对的公制，但通常这些功能基元将很小。  
为什么我们更喜欢这个？这些方法更容易读取，更容易单元测试，并提供更多的重用潜力。  
### 回答 96
取决于要何种代码线但几乎反对封装和OOP标准。IE。一种方法应该只做1件事，并且很好地做到这一点。祝他在战略中与任何多态性好运。我的意思是，似乎他可能是一个意大利面编码器。  
### 回答 97
如果可能，最好为每50到100行代码编写功能。将代码组织成功能是软件工程中最愚蠢的方式。函数调用可能在16 MHz处理器上需要3微秒。它可以在更快的CPU上更快。大量的小功能使用比大型等效代码的RAM更少。有些人有没有职能的书面代码，因为他们不得不以任何原因。只需使用一种允许重用，可扩展性和维护的方法。如果软件要求正在发生变化，使用功能允许轻松添加和删除功能。我宁愿写作用作我可以在一遍又一遍地重用的组件。  
### 回答 98
说什么？你不提什么语言，或者你正在使用的编译器，但任何现代（好比说在90年代中期的Visual C ++！）支持内联函数。所以，你可以拥有所有的重构的很好的效益，避免函数调用的性能开销。  
需要注意的是内联（或单片代码）并不总是最高性能的选择。代码扩展可以吹的指令高速缓存和降低性能。所以，你必须仔细挑选的标准内联。在Microsoft SQL Server的6.5项目另一开发商和我做了很多工作内联的。在一个点上的表现开始下降，这是我们如何结束搞清楚缓存VS调用开销权衡。并行当然，新的处理器做分支预测和预测执行大部分的呼叫。所以今天实际上价格比他们25年前电话是。内联是最终比调用序列小功能始终是虽然赢了，而这正是重构产生了很多。  
此外，你不给任何围绕这个问题的背景下。这是很可能的是，有具体的例子（例如，中断处理代码），其中单块代码是有意义的。但通常情况下并非如此。  
### 回答 99
哈哈。非常恰当在右边。即使高级工程师对速度有右侧，它仍然不会重要。初级工程师无法理解的代码只会通过初级工程师，浪费时间和金钱重新编写。它结束了成本高于丢失毫秒为适当的代码重构。  
### 回答 100
对不起，我不相信你。任何开发人员都知道，对于任何严肃的应用程序，这才是不可能的，因为涉及的巨大代码复制。他不能说，至少不是这种方式。  
### 回答 101
如果你看看埃文韦斯的形象，谁问的问题，他的个人资料说，他已经要求3个问题，并写20个答案。但是，如果你看看他的编辑日志，他有4777项，主要的问题。他似乎4月15日单独（最后一天在历史上），以增加了53题，与数百名编辑的调整他的问题的主题，和几个unmerges一起。  
换句话说，他已经撰写了大量的问题，旨在收集答案，但取消关注几乎所有的人，避免他们出现在他的个人资料。他不会读任何这些问题的答案的。我想说，在这个特别的问题是不真诚 - 它只是clickbait。这种情况并没有发生。  
我不感兴趣，在回答clickbait问题。时间静音这个家伙。  
### 回答 102
想听听真正的独包吗？  
自2000年代初以来，过去两年一直在这个大规模的项目。我没有计算这些线，但一百万行不会让我感到惊讶。其中一半是使用com的c ++，另一半在c＃中。大多数它受到旧学校C专家综合症的患者。  
该项目的关键部分最初是在2000年初的基于模型的软件工程工具中创建的。没有代码开发的早期尝试之一。即便如此，它也可以与项目一起使用，因此必须出口。  
和她们应该冒犯你的工程敏感性。如果你很容易冒犯，现在就停止阅读。  
请参阅，唯一基于模型的代码可以导出到其他内容的唯一方法是作为SQL文件，该文件甚至没有定义表关系。它超过100,000行的SQL行，没有迹象表明，与其他事情有关。  
然后通过Perl脚本转换为C ++代码。  
是的。  
不是一个笑话。  
基于模型的东西→SQL文件→Perl脚本翻译→C ++。  
脚本需要20分钟运行。  
有效。没有人理解如何。有时事情没有工作得很好，但由于没有人真正触摸任何东西，任何没有工作权利的东西都在更高的水平。胶带解决方案。  
我的预算大约是一个数月的时间，只是为了让我现代化，所以它不会再碰到这一点。我同时在个人生活中经历了很多东西。我设法首先解开SQL并提取其中的一些含义，然后将一个实用程序（不是脚本！）放在一起，可以消耗SQL文件并将其转换为C＃。我在那里得到了大约90％的百分比，一些语法并不完全匹配足以编译。但是，嘿，它有一个完全集成的构建过程，转换只需要10秒钟，所以它也会随着能够停止使用Python脚本来构建项目的辅助益处，因为它可以使用MSBuild完成。 yup，python脚本调用Perl脚本在调用项目中的所有单独版本之前转换。  
所以它坐着。没有人敢触摸这个丑陋的怪物，但整个项目都取决于。  
真实的故事，不是一个笑话。  
而每个人都讨论Python脚本以构建项目，但至少是那个维护。  
### 回答 103
你都错了。  
高级软件工程师是错误的，因为PHP是不是真的任何更快地编写代码不是像Python语言。当然，他们可能是对的这取决于你比较它的语言和项目的确切性质。他们也可能是正确的取决于你有机会获得各种语言的内部刀具。 PHP是我快得多，在我目前的公司，因为我没有写一堆新的适配器为其他内部系统我想使用。但是，这不是PHP的固有属性。  
你错了，因为怎么不可读的，多余的，凌乱的代码是有更多的与作家不是语言做。如果你不能写可读，干燥，在PHP干净的代码，这是一个个人的问题，而不是PHP的过错。你可能会写糟糕的代码PHP，因为你与它不太熟悉。如果你付出努力，你的代码将变得更具可读性，减少冗余和杂乱随着时间的推移。  
### 回答 104
这取决于你的项目。  
### 回答 105
即使三地启动其关闭w ^  
其所谓的馄饨代码，而不是意大利面条:)  
我还没有遇到一个真正可怕的馄饨代码库 - （其不直观，或者直白地写_clean_馄饨代码）最有可能，因为很少人甚至知道或试图写入馄饨代码，如果谁做一般都比较高级程序员  
5线规则已在几本书（“清洁守则是我能记得的最早的参考，而最近的/相关的一个我所知道的是，从三地梅斯（三迪梅斯规则对于开发商未来被提及（三弟梅斯规则适用于开发人员） ））。  
即使三地与这些仅仅是开始规则它关闭 - 你应该打破他们时，你认为合适的。教条地执行任意的规则不工作在软件工程 - 几乎比替代每一个决策有赞成和反对。  
因此，我wouldnt甚至称这些规则，而是指引（所以，如果规则说5，它实际上意味着6-7，甚至高达10（或更多，在某些情况下）是可以接受的，但你可以看到，这是那么容易被滥用 - 如果10好，所以是11 ...，因此你必须划清界限的地方）。  
我觉得像这样的规则，目的是使你思考各种情况下，如  
*为什么是方法，只要摆在首位？  
*我怎么可能是重构的方式，将使它更短，但仍一致？  
*如果我把它分解为多条件会发生什么 - 这应该是私有的，哪些应该被移到一个不同的类（战斗特性羡），或者可能给自己，全新的类  
作为太教条可能导致强制执行规则强制执行的规则，产生一些奇怪的结果的缘故。因此，总是问的问题很多，考虑每个解决方案的缺点/上升空间，总是知道你为什么正在做的事情（高级软件工程师告诉我是不是一个好）。  
这就是说，我上面链接的文章介绍Thoughtbot的经验谁应用Sandis规则，他们不平凡的Rails代码库，把它关闭（最好的Ruby / Rails /花好月圆/ iOS的咨询公司之一）。  
他们的重构过程中发现了令人兴奋的事情（例如把Facade模式使用，以满足仅实例化一个对象控制器，想出办法来消除，如果/ ELSIF /其他完全（其超过5行，即使每个分支包含一行只）等，获得了一些有价值的见解和认识到，一般不弹出模式。  
谁是对的？ - 没有一个是正确的。每一种情况是不同的;没有一个正确的方式（如果任何人声称，在另一个方向上运行）。这也取决于团队负责人/建筑师监督团队，团队成员自己的域名，使用的语言（它更具挑战性，坚持规则的更详细的语言），现有的代码库，可测试性，和这么多。  
长话短说：总是问“为什么”在任何情况下，绝不接受任何“规则”盲目。不要听教条“高级软件工程师”，声称通用规则。  
### 回答 106
有可能会或可能不知道一些不成文的规则。  
所以，我还是怀疑，你得到了主意，你是一个薄弱开发商。你可能已经工作过少或已经显示出作为一个开发者越来越多的兴趣。在即使你研究和实践工作，成为摇滚明星的话，你仍然不会挑战自己，并再次你会发现自己比别人弱。  
你需要问自己这一点。 - 如果你发现你的技能是不是一个CS毕业生下，如何在公司去年你做了8年？除非你的公司不是好公司??。弱这里是一个相对的概念！你知道主人;）亲自???。  
你是不弱，你有没有表现出浓厚兴趣增长。你需要工作在不断增加自己或自己养自己。没有人能帮助你在这里。  
无论你是在自己的等级或者你是不是在你的愿望实现了正确的地方。  
在任何情况下，如果你感到虚弱，你想成长，如果你目前的工作犯规挑战，请你辞职，另谋高就，将带给你走出自己的安乐窝。  
所以你的问题直观地说，无论你有没有工作的提高自己故意或者你只是在自己的评级很低。  
### 回答 107
首先，我想提请你注意这里：巧合的是编程，进行彻底的讨论，为什么您所描述的感觉，实际上是尽可能地避免。第二，让我继续前进，衷心建议书上说的链接引用，程序员修炼。我觉得任何专业（或志向的专业），软件开发者应该看它。  
这就是说，有一个程序员的智慧另一位在那里，说，那你写的，你有没有看在过去的一个月中的任何代码，还不如被别人写的。这是因为它是很容易的东西那样复杂的软件赔方面，如果你不是一直接触到它。  
要明白，这是两个截然不同的现象，虽然是很重要的。首先是一些可以用经验和培训来避免。第二个是我们作为人类的必然条件。  
### 回答 108
我总是试图从每个阅读中学习一些东西 - 要么是我应该做的事情，我可以做得更好，或者我永远不应该做的事情。  
如果代码长度超过几页，则我打印出来，以便我可以在适当的地方做笔记。  
我开始小，看看更大，更大的碎片。我首先通过自己读取每行代码，以确保我理解它（99.9％的时间在这里没有惊喜）。然后我开始看看完整的函数和动作，看看他们在做什么（这通常是惊喜开始的地方）。然后我看看较大，更大的代码块，直到我检查整个代码基础（惊喜继续来到这个级别）。  
我试图阅读其他人的代码，就像我在看宝藏地图。大多数代码（甚至是我的）有美丽，贵金属的宝石，以及隐藏在他们身上的炸弹。如果我想完全理解代码库，我的任务是找到它们中的每一个。一旦我找到一个，我试图确定程序员觉得需要把它放在那里。偶尔有评论会给提示一个提示，但通常评论是错误的或不适用于我检查的代码行。提示：始终读取代码，永远不要相信评论。有时我发现代码是一个优雅的解决方案到一个复杂的问题，但通常我最终发现糟糕的尝试强迫虐待或不善理解的想法或要求符合现有的代码基础。  
一旦我觉得我理解或可以解释代码所做的一切，那么我觉得有资格讨论代码。  
### 回答 109
和佛  
将代码称为对象，避免拥有。说这个代码不是正确做x比你的代码正确地执行x。  
由于代码审查是通过定义的一种否定程序，因此使用工程师来保持一些虚构的代码在制作奇迹评论时，您将更好地与工程师进行更好的事情。是的，编写它的程序员究竟知道什么是究竟发生了什么，就像桌子上的其他人一样，但如果您保留人员和代码在您的讨论中分开，则将温度降低得多。  
跟随乔治·冈萨雷斯的评论，你过去做过类似的坏事是让事情保持愉快，避免对着指责或冠军的好方法。  
### 回答 110
这是一个该死的好问题。  
我同意我们应该尝试* *瞄准这一目标。但我知道它（在我的经验）不会发生在现实生活中，至少不是当该项目已不再是小。根据我的经验，较大的项目获得更多关于它的开发者的工作，更多样化的（我被委婉这里）代码变得。  
当我的代码（我用C＃开发），我遵循了我公司工作的编码标准。在没有编码标准，我最难过我工作的公司说的有没有任何不同之处了题为按照微软的准则（甚至是那些声誉的顶级开发房屋哈哈），我尝试超链接鼓励我的同事按照现有的相关风格指南在线（用于HTML，CSS，Javascript代码等），并使用工具，如微软了StyleCop（最新的化身在这里：DotNetAnalyzers / StyleCopAnalyzers）和ReSharper的，以确保在源代码一致的编码风格。  
事情是这样的。这些工具轰炸我们的规则开发者。当你的代码开始看起来像弯弯曲曲的红线和蓝线的质量（IDE提示来改变代码以满足规则），那么开发者只是说啊，地狱与此，你有你的手反抗。它需要一个强大的技术领先，以保持编码标准到位。而且，坦率地说，大多数科技引线只是喜欢平静的生活。  
TL：DR版本？是的，目的是为一个人写的所有。是的，尽量采用编码样式和约定。预计这些项目时增长到走出去的窗口。  