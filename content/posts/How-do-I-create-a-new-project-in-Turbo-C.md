---

title: 如何在Turbo C中创建一个新项目？
date: 2022-01-23T22:08:13+08:00

---




## 如何在Turbo C中创建一个新项目？  
### 回答 1
在20世纪80年代后期，我曾经在当天的Atari st上回来涡轮增压，以后它被重命名为纯C.这是一个很好的编程环境，但我绝对无法告诉你如何创造今天的项目。  
### 回答 2
它不存在。  
现在，如果您有特定的需求集，您可能会找到一个可能与该情况最适合的编译器（或一组编译器）。  
尽管如此，没有单一。您甚至没有说明测量标准。没有单一的判断编译器的价值。  
最好的价钱？最棒的表演？最好的诊断？最好的代码大小？最佳许可证？最好的文件？最佳支持？最佳遵守标准？最佳编译extensions？最好的交叉编译支持？最好的编译时间？最佳便携性？最佳名称识别？最好的整合到您的工作流程中？最佳内存消耗？  
即使在这些指标中的几个指标上，所有C程序可能都有统一。  
GCC和LLVM都有很好的C编译器。 MSVC更好地集成到Windows生态系统中，虽然Microsoft在C ++上专注于C ++，而不是保持最新状态。英特尔有一个C编译器，它在自己的筹码上做了鞭打的东西。 TI的C编译器确实为他们的DSP疯狂优化。  
而且，如果您正在编制Commodore 64，我听到CC65是去的方式，虽然我没有直接经验。  
### 回答 3
蒂姆  
是的，我们可以在Turbo C ++编译器中运行C程序，然后您询问如何实现它。因此，答案很简单只是按照下面给出的步骤  
这如何如何在Turbo C ++编译器中运行C程序。  
快乐编码🙂  
### 回答 4
这里有很多热情的C ++编码器，但我会违背谷物并说出它一般，但并不总是用C ++开始一个新项目的错误选择。  
与其他选项相比，在C ++中开发代码的总成本和维护该代码库的成本要高得多，并且开发更慢。此外，维护C ++ CodeBases的团队通常不太敏捷（不是过程而言，而且在改变产品相对于市场的能力方面）。最后，C ++的性能增益通常小于可以更快的迭代所获得的增益，C ++中项目的开发成本通常远远超过更多机器。跨平台方面具有一些值，但语言之间的端口代码成本通常远低于在C ++中通常开发的成本。净网络：作为技术选择的经常成本无效。  
但是，有例外。复杂的模拟，高级计算机图形，嵌入式系统，电源管理是一个重要的代码，是一个重要的问题，高度分布式的问题或具有自定义数字优化的问题落入一类通常最适合C ++的问题。每年框架在尽量减少未托管代码的优势时会更好地保持托管代码的优势，例如TensorFlow和CNTK在非常大的数据集上使机器学习在不使用非托管代码的情况下，或者单位已经制作（一些）游戏没有非托管代码的开发可能，但存在许多框架造成的案例。  
即使C ++是正确的选择，它往往不是真的，整个项目应该在C ++（或C）中开发。相反，成功的策略是抽出需要高性能的代码进入库，然后将其嵌入到具有较低成本语言开发的项目中。  
作为一般规则，如果您确切地知道您正在尝试构建的内容，那么该图书馆的性能要求挑战，那么它值得考虑。但是，用睁大眼睛考虑它：它是一种昂贵的语言，且成本通常但并非总是消化的性能优势。  
### 回答 5
终极编码项目是我称之为活力的代码  
活力代码基本上是一个现场编码项目。  
什么是现场编码，你可能会问。  
在简单的术语中，现场编码是一种编码形式，其中代码在代码正在执行时写入代码。  
基本上与执行代码相反 - >崩溃/退出，因为错误 - >在源文件中找到错误 - >更改代码以更正错误 - >重新启动执行  
实时编码是Lisp和Smalltalk代码的主要方式。我最喜欢的语言pharo是一种现代的小型技术。  
这看起来很奇怪或难以做到，但实际上非常简单。全部  
终极编码项目是我称之为活力的代码  
活力代码基本上是一个现场编码项目。  
什么是现场编码，你可能会问。  
在简单的术语中，现场编码是一种编码形式，其中代码在代码正在执行时写入代码。  
基本上与执行代码相反 - >崩溃/退出，因为错误 - >在源文件中找到错误 - >更改代码以更正错误 - >重新启动执行  
实时编码是Lisp和Smalltalk代码的主要方式。我最喜欢的语言pharo是一种现代的小型技术。  
这看起来很奇怪或难以做到，但实际上非常简单。所有所花款是一个简单的循环，调用对象，这些对象可以替换实时，使得代码不必停止或结束以执行新代码。  
您可以使用动态链接库在C中实现这一目标。它们在Windows上被称为DLL，麦斯科斯轿车上的DLLIBS等。我会从现在开始称为DLL，这意味着所有3个重要的内容。  
iOS和Android基本上只不过是自定义版本的麦克斯和Linux。 iOS不允许使用DLL，Android确实如此。  
DLL基本上是一个无法自身执行的可执行文件，而是必须被另一个可执行文件调用。它还执行每个函数，因此它不需要主要功能。  
要在C中进行实时编码，您将需要首先是包含3件事的主要可执行文件。主循环。在此循环中，在检测到其源文件的更改时，将会加载DLL，并且当然将调用特定的DLL函数。可执行文件将需要一个指针到内存。您不需要更多，因为DLL也将处理内存的管理。所以基本上几乎没有任何东西在可执行文件中会发生任何事情以及DLL中的其他一切。  
基本上所有这都是基本的C编码知识。没有什么复杂的。 C / C ++项目在巨大案例方案中大量取决于DLL，因此它甚至没有一种不寻常的代码方式。  
这将产生效果，即您将不再需要提前计划或定义编码项目。相反，您可以尝试随机想法，直到您找到一个对您感兴趣的东西。由于更改代码和执行它之间没有延迟，但实时编码允许大量的实验。  
活着的代码可以进一步进一步，它不仅仅是因为它听起来很酷，它实际上是模仿生活。源文件成为单元格，库成为生态系统。您的代码一直在执行，它永远不需要停止，它可以以这样的方式使其与生态系统的新想法一起增长和发展。  
所以基本上你可以说活着代码更像是科学实验室，而不是实际项目。  
然而，这是一个很好的工具来克服心理障碍，并在飞行中产生想法。  
您在此处找到有关Live Coding的一些代码（C ++（C是非常相似）  
千克/ livecpp.  
这是我的github repo，它受到这些youtube教程的启发  
玩得开心 ：）  
### 回答 6
你绝对不使用turbo c，因为这真的是一个老式的项目。你的现代c编译器是：gcc或windows mingw.that程序被移植到处都是巨大的目标平台。没有真正的竞争。没有真正的目标平台。没有真正的目标平台。目前的GCC。第二个编译器是铿cl的，来自LLVM Project.That是做得很好的代码，但它是一个饥饿的记忆怪物，它会与每个螺纹一起吃3 GB的内存。在6个线程上有18个线程GB的RAM只是为了编译而且很有趣，很可能会让你交换，并在1/10000的速度或更少的时间内推动你的速度..你的代码在夜晚编译你的代码而不是在一分钟内部编译。我真的很棒因为那件事变得可用，但我不认为他们已经存在了。所以坚持GCC是我的建议。你也有一个更好的界面到那里的其他语言，就像我不知道克朗与装配联系如何例如。不要使用，我的意思是从来没有，永远不要使用专有的编译器你的项目。这将不仅导致您无法找到的错误，因为您无法控制编译器和工具集的工作，它也会为您提供更好的事情免费或您在某些公司Fucketry中获得类似Intel编译器，如果它检测到您的计算机中不是真正的Intel处理器，但是某些AMD处理器或您瞄准体系结构的人，则会创建效率低效代码.I英特尔C编译器（ICC）如何与GCC不同，是什么让它值得购买？好奇，如果ICC在您的情况下，那种情况是什么。与SIMD / Vectorizizizization相关的经验值得赞赏。因为他们认为这将是一个好的想法用这种措施搞砸了AMD的基准，特别是因为一些最突出的基准是用英特尔编译器完成的，因此涂抹AMD处理器非常有效。这一切都被证明，这是o持续的事情。但英特尔不是唯一做这样的混蛋，所有专有的工具链做那样的事情。你真的不能这样做。如果你这样做，你将依赖他们的工具 - 如果你想把你的项目给朋友，他也无法编译这件事，直到他也可以购买他妈的工具链。这是在没有必要的情况下投入枷锁，没有任何利益。我不明白为什么人们会这样做。所以不要这样做，这将是我的推荐.GCC确实产生了非常好的代码。它不是完美的代码，我发现众多装配用很多事情做得更好，但它是非常不错的代码，它不必隐藏其他编译器，实际上gcc是参考编译器。你不仅仅是只是x86平台，你可以编译到所有类型的目标。什么也是你的不要在别的地方得到其他，但在铿cl声。但是克朗远离GCC支持的广泛基础。不要使用复古工具像Turbo C一样，不要使用像Microsoft Visual C ++这样的专有工具链。如果您想要一个IDE，我会指向Qt Creator.i更喜欢使用Vim，Tmux和Zsh。但是，这是真正的个人品味。在qtcreator上工作很好，它被广泛考虑了MS Visual Studio后的下一步。当然它是免费的软件，就像GCC一样。没有绑定你的专有软件的开发是一个普遍的良好建议，我想，几年经验落后于此。我一直在那里;这是可怕的。另外，我建议您离开Windows平台进行开发。因为该平台是非常糟糕的，不健康和不安全的开发平台。您在Linux上更好地做到了更好，更快，交叉制作.Works为me.works .as，Windows仍然有一些参数将它放在Linux上。但是对于开发工作，它只是一个不可以一个可行的选择。它是活着的复古和死人走路。这将是一个很棒的线计算机历史博物馆的技术，在那里关闭了Dos到Windows的线路10.但是人们今天使用它作为他们的系统，我只用不相信的方式盯着。我有一个我必须使用的程序运行了一个VM，我必须使用只在窗户上运行，甚至没有在葡萄酒上工作。  
### 回答 7
有。但不多。除了到目前为止答案中引用的差异，这里有几点，你可以立即在键入代码时立即注意到，然后尝试执行它们。  
这些是我可以记住我头顶的几点。我会继续编辑，因为我记得更多！  
### 回答 8
即使在标准化之前，Turbo C ++已过时。  
最佳选择是使用IDE和像GCC，Clang这样的编译器。或者真正的经验，您甚至可以尝试使用自定义makefiles的vim和clang。  
尝试代码块或代码单位或eclipse甚至NetBeans。在Linux上，有kdevelop，qtcreator，anjuta等的更多选项。  
有vim和emacs等硬核选项......  
但请避免涡轮增压，使用GCC / Clang保持标准。  
### 回答 9
Turbo C ++是一个已停用的C ++编译器和来自Borland的集成开发环境和计算机语言。最近，它是由Embarcadero Technologies分发的，该技术在2008年购买了其Codegear划分的所有Borlands编译工具。1994年后，原始的Turbo C ++产品线被搁置，并于2006年被恢复为介绍级IDE，基本上是他们旗舰C ++建设者的剥离版本。 2006年9月5日发布的Turbo C ++于2006年9月5日发布，可在探险家和专业版中提供。 Explorer Edition免费下载和分发，而专业版是商业产品。 2009年10月Embarcadero Technologies停止了2006年C ++版本的支持。因此，Explorer Edition已不再可供下载，专业版不再可用于从Embarcadero Technologies购买。 Curbo C ++由C ++ Builder成功。  
turbo c ++  
开发人员_ TypeInitial发布于1990年5月  
2006年9月5日稳定发布  
操作系统Microsoft Windows  
网站www.turboexplorer.com.  