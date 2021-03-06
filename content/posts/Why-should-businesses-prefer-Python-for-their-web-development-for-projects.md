---

title: 为什么企业更喜欢Python为项目的Web开发？
date: 2022-01-23T22:08:09+08:00

---




## 为什么企业更喜欢Python为项目的Web开发？  
### 回答 1
企业不需要浪费时间聚焦，用于建立其产品和网站的语言 - 将此留给专门编写代码的程序员。  
对于网站，应用程序或在线服务，业务确实需要尽早从客户开始反馈，最好首先使用小型可信客户组 - 然后继续基于此反馈优化其产品。  
任何业务也需要确保其产品可访问，可用且易于导航 - 再次，只要它具有足够的程序员，以及一个很好的社区，编程语​​言就是无关紧要的。  
要求的非编程管理人员 - 例如 -  React开发人员实际上需要前端JavaScript开发人员，并且对于Python开发人员阅读有经验的程序员。除非您在特定框架或图书馆中编写的遗留系统。将代码留给编码器和管理到经理！  
### 回答 2
他们不应该，除非：  
Python是一个糟糕的选择完整的严肃的网络应用程序，其他人已经陷入了陷阱，不要重复他们的错误。对于系统的灯光部分，实际零件是用更有能力的实现编写的，就像YouTube所做的那样。  
但是，如果您坚持，请随时证明并加入上面提到的那些。  
### 回答 3
这真的依赖于他们正在建造的应用类型。Python是一种像其他任何其他人一样的语言，并且有一个越来越多的窗口，而不是另一个，但选择适用于您正在建设的应用程序的东西。Python非常多样化，在编程中的大量区域工作。也很容易学习和发展。  
### 回答 4
商业关注成本和上市时间，所以有两个优惠他们将选择更便宜的交付，这更可能是基于Java的Python，这也是为什么Python在初创公司中非常流行。  
### 回答 5
真正有趣的问题，并在Dropbox的工程总监答案应该真的被认为有点明确。  
话虽如此，让我探索问题一点点，因为它进入了超级尺度应用程序的核心。  
超级应用程序是为数百万用户提供服务的应用程序。  
要问的问题是：峰值计算周期的计算周期方面的单个用户成本是多少？  
和继承人的不正当答：不是很多。事实上，如果你做数学，它可能会出于分数的便士。在Zynga，我们在2011年和D做了数学  
真正有趣的问题，并在Dropbox的工程总监答案应该真的被认为有点明确。  
话虽如此，让我探索问题一点点，因为它进入了超级尺度应用程序的核心。  
超级应用程序是为数百万用户提供服务的应用程序。  
要问的问题是：峰值计算周期的计算周期方面的单个用户成本是多少？  
和继承人的不正当答：不是很多。事实上，如果你做数学，它可能会出于分数的便士。在Zynga，我们在2011年做了数学，发现每用户成本小于0.1美分。如果另一个供应商分享他们的数据，我会感到惊讶和高兴，但我怀疑任何人都会。  
令人惊讶的结果。  
这意味着什么？  
这意味着单个用户的单个线程的CPU成本很小;费用仅在规模上。如果他们只在规模上，那么问题就会成为如何支付规模的？  
最佳和最乐观的答案是最终用户将足够支付以支付成本。我假设Dropbox已经解决了这个问题:-)  
事实证明，少数用户必须支付少量以支付基础设施的成本。  
如果是这种情况，那么Python的性能成本只是增加必须支付的用户数量以满足基础设施的成本。如果必须支付休息的用户甚至从纯基础设施的角度来看，那么你已经有足够了，那么这不是一个有趣的优化。  
让我们做一些算术，以使最后一段更清楚：  
cost_per_user = $ 0.001total_users = 1000infra_cost = $ 1  
单个用户必须支付多少费用以满足Infra_costs？ 1美元  
因此，只要一个人支付1美元，那么你就不要在纯粹的成本角度来看python缓慢。您有足够的现金运行基础架构。  
现在，显然这是一个简单的例子，它假设货币化模型非常差。像Dropbox这样的公司可能拥有超过0.1％的用户支付存储，因此他们产生的收入远远超过基础设施的成本。  
这让我带来了余量。事实证明，由于它们影响您的业务模式，因此仅费用。假设Dropbox是一个经营良好的业务 - 感觉合理:-)  - 我预计与销售，营销和工程相比，他们的基础设施的成本是微小的。而你制作基础设施的更便宜，您可以花费更多的钱在其他活动中。  
这是其中一个潮流的情况。  
让我们做一些算术来制作我的观点  
假设总收入= $ 100工程成本= $ 30.CRA = $ 1SALES +营销= 30美元  
如果您可以将50％的红外线成本节省50％，这将减少0.50美元的总费用  
但这些储蓄将以工程生产力为代价 - 大概是它更容易使用Python开发功能。工程生产率的下降将转化为特征速度的下降或工程成本的增加。在实践中，它真的转化为特征速度的下降。  
如果从企业角度来看，您需要更多的功能而不是更便宜的基础架构，这是一个不良的折衷。  
这让我带来了我的下一点。鉴于Python的生产力胜利，以及移动到C的真正成本，更好的问题是：Dropbox会对Python使用某种JIT吗？这就是Facebook的聪明人所做的。面对从基础设施的角度来看PHP的成本，而不是移动到C，他们使PHP变得更快。  
如果您可以获得少数人支付，则使用除C之外的语言始终是超级应用程序的好解决方案。并使动态语言更快，总是比在这些环境中移动到C的更好答案。  
### 回答 6
Python是一种通用语言，这意味着它不仅仅用于一个目的，例如web开发.Rather，它在许多不同的行业中使用，以及您选择工作的行业将确定您如何实际学习语言。例如，如果您聘请编写与操作系统和监视设备交互的应用程序，您可能不需要知道如何使用Python模块进行科学和数值编程。在类似的时尚，如果您雇用编写与MySqldatabase交互的Python代码，然后您无需掌握它与CouchdB的运用方式。因此，我将建议有三个级别来学习Python的基础：  
真正的初学者  
在基本级别，Python是一种简单的语言来学习和使用。您可以快速了解如何创建变量和循环，例如，以超越元组，列表和词典扩展.Any Python Newbie需要知道哪种类型不可变，这意味着该类型的对象无法更改（答案：元组和字符串）。与不可变的类型，对象的值本身不能更改，但包含对象的变量可以：  
a = abc.  
a = a.upper（）  
在上面的示例中，原始字符串ABC没有改变，因为字符串无法改变;相反，我们计算了一个全新的字符串，abc，并将其存储回到原始变量中。这类东西应该是任何寻求了解理解Python Works的人的第二种。此外，学习Python的人应该知道如何语言处理面向对象的编程，以及如何创建类和实例化对象。知道如何使用异常和异常处理程序以及模块的互动方式也很重要。（对于关键洞察，我建议您阅读并理解Python语言参考;如果你不确定语法或语言如何工作，或者是用同事争论，那个网站将有最后的词。）Python初学者还必须知道Python 2和Python 3是不同的.Python 3已经不同.Python 3出于相当长的时间，但仍有很多项目依赖于Python 2.如果您正在面试，您将想问他们使用的是哪个Python;如果您是知识渊博，那么您可以谈论差异。更高级的差异  
一旦你掌握了一些基本概念，你就可以继续前进到稍微高级的概念。如果您熟悉JavaScript等语言，Python的强大打字可能会让您感到惊讶;例如，您不能只需加入10即可获得Hello10。（您将获得一个例外。）这意味着可以防止代码中的错误，这意味着您需要变得非常熟悉动态键入，强大的键入，鸭键入以及Python如何实现到Python的所有三个C ++程序员可能会感到惊讶，您无需为函数中的参数提供接口;如果对象通过了所需的方法，你很糟糕。这使得多态变得容易。从那里有所了解，了解封闭和一流的对象.Python支持两者，这导致了这篇文章的概念很好地解释了一个有趣的封闭例子，从相关文章中提供的一个有趣的案例;这是从交互式shell输入的：  
>>> def外部（x）：  
... y = x * 2  
... Def Inner（z）：  
...返回y + z  
......返回内在  
......  
>>> Q =外（5）  
>>> r =外部（6）  
>>> Q（2）  
12.  
>>> Q（3）  
13.  
>>> R（2）  
14.  
>>> R（3）  
15.  
>>>  
函数外部创建一个名为Y的变量的闭包，返回您可以调用的新函数。我称之为外部功能两次以创建两个这样的功能;然后我每次调用这两个函数.Last但肯定并非最不重要的是：读取Python的Zen，它是有趣的，真实的，并在堆栈溢出上查看这个线程，了解如何掌握语言的一些重要建议.Go to Github以及查找许多流行的Python项目中的任何一个;研究代码尽可能多。侧面注意：了解模块  
该模块是您的库，您的帮助者。了解标准图书馆中有哪些内容;您不必记住每个类的每个成员，以及每个模块的每一类，但您确实想知道什么是可用的，以便在需要某些内容时，您不会从划痕中重写一个。用每个模块重写一个自己.many，如文件I / O，几乎可以在每个应用程序中访问;知道这些内部和外面。  
### 回答 7
一个像这样的复杂问题无法用单一句子回答。所以，让我试着分享一个完整的解释。  
首先，这种用户友好的语言也是世界上增长最快，最流行的编程语言，用于数据分析和可视化，AI和ML，自动化和测试。  
资料来源：数据Flair  
Python是Web应用程序，移动应用程序和桌面应用程序开发的完美选择。这巨大使用的原因很少：  
Python有任何限制吗？它有一些。我将分享一个有趣的文章的链接，了解Python对产品开发的优势和缺点，以便您可以了解更多信息。  
### 回答 8
当然，Python我会说，没有任何第二种想法，你应该和Python一起去。它是一种多功能语言，它几乎可以做任何事情。  
让我为你提供这种方式，可以为您开发一个端到端游戏吗？当然，它可以开发一个网站，即使python也可以做到。  
但是，你可以用php开发人工智能吗？无权利？ Python可以帮到你！  
好的，现在你可能会想到它吗？ AI，Games和网站？ python仅限于此吗？  
不，它可以做的是，它可以做Web刮擦，它可以做脚本，使用Python脚本你可以构建int  
当然，Python我会说，没有任何第二种想法，你应该和Python一起去。它是一种多功能语言，它几乎可以做任何事情。  
让我为你提供这种方式，可以为您开发一个端到端游戏吗？当然，它可以开发一个网站，即使python也可以做到。  
但是，你可以用php开发人工智能吗？无权利？ Python可以帮到你！  
好的，现在你可能会想到它吗？ AI，Games和网站？ python仅限于此吗？  
不，它可以做到这一点，它可以做Web刮擦，它可以做脚本，使用Python脚本你可以建立交互式聊天，它可以做数据可视化，数据操纵，数据争吵，数据库连接，使用机器学习预测分析算法，等等。  
所以，这些都是所有技术方面，我很确定有一千多万技术因素我可以在你面前留在你面前，以证明我的观点，但是现在，让我们看看一些统计数据，证明Python更受欢迎比php。  
在Google趋势上看看这个图表，我刚刚检查了Python对PHP的普及。蓝色是Python的结果，红色的是PHP：  
让我们在地理上检查：  
您可以看到上面的图表中的差异以及世界如何使用Python流出蓝色。它在每个类别中有更多的搜索条件，它是谷歌搜索，是IT教育搜索，作业搜索，技术搜索。  
再次，让我在Python作业的作业和红色作业的蓝色向下向您展示图表。  
它是同样的方式，Python是真正的赢家。  
现在，让我谈谈他们的社区支持。  
与社区我的意思是，您可以在那里获得更多的开发人员来帮助或支持您解决您所面临的编码问题。  
因此，如果您检查STACKOVER-FLUS上发布的问题数量，则Python每年都会多于PHP获取更多问题。  
从2009年到2016年的PHP还有更多问题，但现在该图已经下降了最糟糕，并且对于一个好的，因为现在每个行业都在采用Python的业务，几乎可以获得所有目的。  
现在，让我们查看GitHub：  
Python：  
PHP：  
你现在必须弄清楚，这是谁是这里的胜利者。  
现在，我会把它留给你来决定，我已经向你展示了这个事实，现在明智地选择。  
我希望我的答案帮助你！  
快乐的学习:)  
### 回答 9
不可以。Python的比PHP显着更好。  
原因很简单地简单地说，Python被设计为从GOT开始的完整语言，而PHP则开始小而简单，然后在另一个克劳德作为事后寻求一个特征。结果没有什么是一致的，很多事情都非常凌乱和令人困惑。  
一些例子就足够了：  
你可以在这里阅读更多：PHP：一个不良设计的分形  
本质上，没有人在PHP中开始新的大项目。 PHP仍然很受欢迎，但主要是2件事：要么在PHP在PHP中开始的项目，或者对于开发人员恰好知道PHP的小型简单的东西。  
相比之下，Python非常令人惊讶，并且具有比较符合的令人惊讶。它还从一开始就拥有OO，而不是以偶然的方式添加到PHP中的事后。  
通常在Python中进行Web工作时，您将使用诸如Django等众多流行框架之一。这些还具有从显示模板中干净地分离编程逻辑的优势。  
Python具有比PHP更多的功能。除了更可读和更一致之外，语法更强大。  
### 回答 10
像网站一样开发Facebook或Quora并不适合初学者Web开发人员！这就像向初学者画家建议绘制Mona-Lisa！  
练习普通的JavaScript！  
如果你知道vanilla javascript，你对它感到舒服，那么你几乎是一半的工作！  
 *在运动场等平台上进行日常挑战！*审查其他人的代码并尝试反向工程师！*尝试在没有框架的情况下代码javascript  
一旦你对此感到舒服，你......  
### 回答 11
您有错误的信息。很多大公司正在使用Fintthon。这是您在Python中开发的这个问题的网站。  
请阅读一下Quora选择Python以其开发？创始人在他们决定与Python相反而不是PHP之前，这是什么技术挑战？  
以下是公司列表，这些公司使用Python从官方Python网站构建真实世界应用程序。请留下一看法。OrganizationsUsingPython  -  Python Wiki  
如果您是一名新手，我强烈敦促您留下其他语言并开始学习Python和JavaScript。  
### 回答 12
我建议一个不断和战略的方法，帮助您轻松地进入广阔的网络开发宇宙，而不是直接跳过一些WSGI框架并陷入其复杂性。  
重要的是要注意的是，Web开发对于不同的人来说是不同的，这意味着取决于技能集，计算熟练程度和创造力水平不同的人可以采取不同的时间和编程方法来达到相同的结论。  
吧开始，  
请记住，Web开发是一个连续和缓慢的过程，在几天或几周内无法学习。此外，只有＃4中提到的Python和相关框架将仅在您制作基于Web2的WebApp时使用，否则不需要制作内容在每个交互上更改内容的个人/静态网站。因此＃1非常重要。  
对于纬线，一旦您正在进行Web开发并且熟悉上面的概念，可能需要技能并挖掘更高级的概念，如：  
