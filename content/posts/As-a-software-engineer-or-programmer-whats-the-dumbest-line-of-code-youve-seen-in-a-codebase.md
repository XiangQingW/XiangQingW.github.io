---

title: 作为软件工程师或程序员，在CodeBase中看到的最愚蠢的代码行是什么？
date: 2022-01-23T22:08:10+08:00

---




## 作为软件工程师或程序员，在CodeBase中看到的最愚蠢的代码行是什么？  
### 回答 1
两个好的例子来到了我的脑海里。  
1）首先是正式语言表达的存在危机：  
<ol>如果我没有什么... </ ol>  
<li>如果我没有什么...... </ li>  
或者，翻译成更常用的语言：  
<ol> if（这！= null）// ... </ ol>  
<li>如果（这！= null）// ... </ li>  
但VisualBasic的原始版本要好得多。这几乎是哲学的，就像我想的一些混淆版本，所以我是。  
2）对于第二个例子，一张照片比千言万语更好：  
这是我工作站的图片。在所有的显示器上都有一个视觉工作室的窗口。  
你看到了小两个箭吗？它们指向第75行。第75行是811个字符长。  
第75行I.  
两个好的例子来到了我的脑海里。  
1）首先是正式语言表达的存在危机：  
<ol>如果我没有什么... </ ol>  
<li>如果我没有什么...... </ li>  
或者，翻译成更常用的语言：  
<ol> if（这！= null）// ... </ ol>  
<li>如果（这！= null）// ... </ li>  
但VisualBasic的原始版本要好得多。这几乎是哲学的，就像我想的一些混淆版本，所以我是。  
2）对于第二个例子，一张照片比千言万语更好：  
这是我工作站的图片。在所有的显示器上都有一个视觉工作室的窗口。  
你看到了小两个箭吗？它们指向第75行。第75行是811个字符长。  
第75行不是生成的计算机。人类做到了。  
编辑：  
根据评论，我认为榜首＃2值得上下文。  
那么......如何发生这种情况？  
首先要了解：这是专业开发人员（至少在最专业开发人员理解学期专业开发人员）的最具产品。  
你看，不仅是专业开发人员的编程。有许多专家有一些非常具体的领域知识，但这不是专业程序员。它可以是天体物理学家，投资分析师或企业员工，他们正在努力改进/扩展公司流程，因为ERP软件很糟糕（或只是剂量解决一些具体的问题）。  
对于这些人来说，编程意味着结束。他们可能不使用版本控制，不知道最佳实践，并不熟悉术语技术债务或者不认为这是重要的（=如果它的工作，为什么浪费更多的时间呢？）。但没有错误：他们非常聪明。记住：他们不是程序员，但他们解决了大多数程序员无法解决的问题。  
这正是第75行的情况。人写这一点，知道的，知道商业问题是没有其他人。  
要更具体，我猜在这种情况下发挥了作用：  
有人问道，究竟是什么：  
它处理一些数据。有一个带有数十个加法器和一些嵌套的LINQ扩展方法的构造函数（GroupBy，Sum，Select，更具体）。  
有人问它是如何掌握分公司的。准备被吹走：  
那时（我猜2014年或15左右）我们没有使用版本控制。那有多疯狂？！  
BTW，车臣这件Stackoverflow调查从2018年起：  
### 回答 2
不幸的是，可以经常看到以下内容：（B是一个布尔）如果（b == true）。这表明程序员没有得到布尔的召开。我曾经提到过一些程序员。他的回答：我想确保它绝对清晰。  
### 回答 3
我的最有趣的部分是这个家伙不知道为什么是愚蠢的。  
他有：  
$ x = $ x  -  $ x + 1;  
然后他认为这是合法的，因为伙计...... $ x可以是任何东西  
我不得不重复大约50倍，任何东西减去任何东西是0..s .. $ x = 1  
### 回答 4
它实际上不是一行代码，所以说话，但代码线。  
我在Salesforce工作，对于那些不熟悉其云架构的人，如果生产的总体测试覆盖率为75％或更多，则可以将来自QA的组件移动到生产。意思是，如果所有组件的代码行总数，包括新介绍的，必须使用适当的测试场景写入足够的测试类，以便覆盖至少7500行的块。 Salesforce本身强制执行此规则，因此无法解决它。另一方面，断言可以没有。  
如果组件的移动导致生产的平衡转移并将其整体覆盖范围提高到75％以下，您应该在新组件上工作并在部署之前提高其覆盖范围。一个噩梦的噩梦，因为你的代码有很好的机会，只有在多年来已经进入的肮脏代码的历史记录拖动整体覆盖范围的历史记录，才会发生这个问题。  
我以前的公司中有人发现了一种偷偷摸摸的方式来在他（或她）的一些代码中偷渡，而无需担心这个问题。  
所以这是简单的数学，对吗？如果您有5000行代码，则必须涵盖3750行。但是如果我设法只占用2500（50％），我的截止日期是危险的？  
简单的。我添加了5000行不必要的代码，即我可以通过一个函数调用肯定地覆盖，使整个线路编号现在是10000，覆盖线是7500，使我的覆盖率百分比甜点75。  
为此目的，他们在每个中引入了几个完整的课程。该方法始于，  
Integer i = 0;  
并继续重复上行数千次。  
I ++;  
他们有大胆的方法在整个笨重的方法中复制和粘贴这个重复的代码，并且以这种鲁莽的方式，您可以在每一100行左右完全在第一行中看到错误的选项卡。  
现在，您留下的所有这些都在测试类中呼叫此方法，您可以在不破坏汗水的情况下覆盖线路的得分。实际上重要的所有代码可能在自动覆盖检查中未经测试，如果一个人应该注意看看，但是你有效地有效地蒙上蒙蔽了销售部署机制。  
和后果甚至是疯狂的。看到囤积组件的方式可以在不必踏上写作测试类的繁琐过程中，这项技术获得了我们在我们实践中的Salesforce最佳实践等同于Salesforce最佳实践的状态。在几乎所有主要的组织中，如果您搜索它，您可以找到具有I ++流的类;沿着屏幕流动，据您所能滚动下来。  
好吧，在一些未经测试的情景开始再欣培之前，这些披肩陷入困境仍未被未被发现。更明智的开发商捕捞了I ++;课程，抬起闹钟并下来清理混乱。只需删除这些课程将整体生产覆盖率推向深处低，防止任何形式与生产相互作用。我能说什么，这让我们许多人至少忙于一个月。  
我不打电话给愚蠢地把这个代码的开发人员打电话。我宁愿去邪恶。较高的头部和测试人员在鼻子下面传递的时候没有注意看看，确实有资格愚蠢。  
和这个代码......男人，那是我见过的最愚蠢的事情。  
### 回答 5
也许不是最愚蠢的，但我曾发现了一段代码，它携带100％的保证它从未被测试过。它是这样的：  
<ol> if（some_condition）{200_lines_of_code; } else {//呵呵，现在这将是奇怪的_200_lines_of_code; } </ OL>  
<li> if（some_condition）{</ li>  
<li> 200_lines_of_code; </ Li>  
<li>} else {//呵呵，现在这将是奇怪的</ li>  
<li>另一个_200_lines_of_code; </ Li>  
<li>} </ li>  
它来自我们团队中的一个人，他们一般喜欢在阅读时写下'谈话'的代码，他的内在独白构成了他写的大部分代码。不幸的是，我不记得他的大部分评论，但遇到的东西并不罕见：  
<ol> if（some_condition）{//然后做什么{...} </ ol>  
<li> if（some_condition）{</ li>  
<li> //然后不做</ li>  
<li>} else {</ li>  
<li> ... </ li>  
<li>} </ li>  
或（在第一个示例的基调中）：  
<OL>} E </ OL>  
<li>} e </ li>  
也许不是最愚蠢的，但我曾发现了一段代码，它携带100％的保证它从未被测试过。它是这样的：  
<ol> if（some_condition）{200_lines_of_code; } else {//呵呵，现在这将是奇怪的_200_lines_of_code; } </ OL>  
<li> if（some_condition）{</ li>  
<li> 200_lines_of_code; </ Li>  
<li>} else {//呵呵，现在这将是奇怪的</ li>  
<li>另一个_200_lines_of_code; </ Li>  
<li>} </ li>  
它来自我们团队中的一个人，他们一般喜欢在阅读时写下'谈话'的代码，他的内在独白构成了他写的大部分代码。不幸的是，我不记得他的大部分评论，但遇到的东西并不罕见：  
<ol> if（some_condition）{//然后做什么{...} </ ol>  
<li> if（some_condition）{</ li>  
<li> //然后不做</ li>  
<li>} else {</ li>  
<li> ... </ li>  
<li>} </ li>  
或（在第一个示例的基调中）：  
<ol>} else {/ *这可能永远不会发生，但是在下面的代码下面只是在它做* / </ ol>  
<li>} else {/ *这可能永远不会发生，但在下面的情况下，如果它确实* / </ li>  
### 回答 6
<ol>试试{dothework（）; catch（例外e）{//有未知问题导致程序停止//我不知道它是什么//，但我们真的需要继续//所以让我们只是抑制这个例外并继续前进的例外（）; </ OL>  
<li>尝试{</ li>  
<li> dothework（）; </ Li>  
<li>}捕获（例外e）{</ li>  
<li> //存在未知问题，导致程序停止</ li>  
<li> //我不知道它是什么</ li>  
<li> //，但我们真的需要继续</ li>  
<li> //所以让我们只是抑制这个例外并继续</ li>  
<li>} </ li>  
<li> </ li>  
<li> dosomemorework（）; </ Li>  
故事的悲伤部分是我多次看到这个。而不是修复原因，人们只会隐藏问题。  
不用说这使得系统以非常意外的方式行事。想象一半的例外情况下以这种方式抑制了！  
嘿，付款期间有一个问题，你能发现出了什么问题吗？ ......现在我真的不能！  
一旦我工作了  
<ol>试试{dothework（）; catch（例外e）{//有未知问题导致程序停止//我不知道它是什么//，但我们真的需要继续//所以让我们只是抑制这个例外并继续前进的例外（）; </ OL>  
<li>尝试{</ li>  
<li> dothework（）; </ Li>  
<li>}捕获（例外e）{</ li>  
<li> //存在未知问题，导致程序停止</ li>  
<li> //我不知道它是什么</ li>  
<li> //，但我们真的需要继续</ li>  
<li> //所以让我们只是抑制这个例外并继续</ li>  
<li>} </ li>  
<li> </ li>  
<li> dosomemorework（）; </ Li>  
故事的悲伤部分是我多次看到这个。而不是修复原因，人们只会隐藏问题。  
不用说这使得系统以非常意外的方式行事。想象一半的例外情况下以这种方式抑制了！  
嘿，付款期间有一个问题，你能发现出了什么问题吗？ ......现在我真的不能！  
一旦我在一支球队工作，这是一个标准程序 - 他们会捕获异常并记录并继续。每天有成千上万的日志，但没有人会花一分钟的时间来看看日志，就在那里，那就是:-)工作做得很好:-)  
### 回答 7
我在其中一个测试中找到了这一点。我知道这些家伙没有知道如何编写测试，但建筑师强制执行它并希望在报告中看到。她所做的事情：  
<ol> @test public void testthatmethod（）{//各种各样的sh * ts在这里，可能是20-25行长asserttrue（true）;} </ OL>  
<li> @test </ li>  
<li> public void testthatmethod（）{</ li>  
<li> //各种各样的sh * ts在这里，可能是20-25行长</ li>  
<li> asserttrue（真实）;</ Li>  
<li>} </ li>  
当我发现它时，大约6个月大，已经明显刺激了途径。  
写这段代码的那个人让团队成为一些其他团队。所以，我向我的团队展示了这一点。有趣的事情是我团队中的一些人没有得到它。  
### 回答 8
这是我9年前写道的代码，我不能忘记并原谅自己来提出它。  
//生成100个字符的单词  
让fiveletterword = abcde;  
让百分点=';  
for（i = 1; i <= 20; i ++）{  
百分点=百分点+ fiveletterword;  
}  
为什么我没有一封信并循环100次？它令我迷惑我。  
### 回答 9
最愚蠢的两者因为影响和原因，可能是20年前：  
在一个循环中调用的函数中，我最终写了：  
x = malloc（尺寸）;  
是的，每次使用时都会泄露内存的副本和粘贴错误。  
复制和粘贴错误是愚蠢的。内存泄漏是愚蠢的。当我终于找到它时，额外的malloc感到愚蠢！  
### 回答 10
我不会说它在代码中写的最愚蠢但最有趣的行。  
有一天，我通过应用程序日志浏览，并在下面的调试下面由沮丧的开发人员编写。在修复错误之后，他可以解决问题，所以在给出最后一次尝试之前，这是在日志中打印的警告:)。  
代码模板：  
<ol> if（productind == consts.tfn_byte）{if（systemutils.isusempty（terminateno））{tracesutils.trace（缺陷＃6372 -if此修复程序不起作用，我的简历已准备好！\ n）;抛出新的validateException（errormsgs.field_not_valid，终止TFN）; }} </ OL>  
<li> if（productind == consts.tfn_byte）{</ li>  
<li> if（systemutils.isusempty（terminateno））{</ li>  
<li> traceutils.trace（缺陷＃6372-如果这个修复程序不起作用，那么我的简历就绪！\ n）; </ Li>  
<li>抛出新的validateException（errormsgs.field_not_valid，终止tfn）; </ Li>  
<li>} </ li>  
不知道wh  
我不会说它在代码中写的最愚蠢但最有趣的行。  
有一天，我通过应用程序日志浏览，并在下面的调试下面由沮丧的开发人员编写。在修复错误之后，他可以解决问题，所以在给出最后一次尝试之前，这是在日志中打印的警告:)。  
代码模板：  
<ol> if（productind == consts.tfn_byte）{if（systemutils.isusempty（terminateno））{tracesutils.trace（缺陷＃6372 -if此修复程序不起作用，我的简历已准备好！\ n）;抛出新的validateException（errormsgs.field_not_valid，终止TFN）; }} </ OL>  
<li> if（productind == consts.tfn_byte）{</ li>  
<li> if（systemutils.isusempty（terminateno））{</ li>  
<li> traceutils.trace（缺陷＃6372-如果这个修复程序不起作用，那么我的简历就绪！\ n）; </ Li>  
<li>抛出新的validateException（errormsgs.field_not_valid，终止tfn）; </ Li>  
<li>} </ li>  
不知道是否持续工作或不起作用，但这绝对是有趣的。  
### 回答 11
两条routi的执行速度之间没有人类可感知的差异  
不是最愚蠢的代码行，但如果你理解软件极客，这很有趣  
一个人正在努力实现我们需要的一些少量数据的聪明和快速的分类例程。另一个Wiseguy程序员写了一个分类的例程，并挑战了第一个展示他所有的辛勤工作的价值。  
第二个家伙的排序例程如下所示：  
两种例程的执行速度之间没有人类可察觉的差异。  
### 回答 12
多年来几乎没有几个人不能开始评价一个人：  
在一个常见的内容中，为正在移植到C的一组代码的文件，我发现它已陈述：  
<ol> #define null 1 </ ol>  
<li> #define null 1 </ li>  
一天或两个人稍后同一个人，（现在谁现在正在运行不同的模块），将其改为：  
<ol> #define null 3 </ ol>  
<li> #define null 3 </ li>  
毋庸置疑，虽然这些变化得到了他当时在通过邮政移植术后测试的哪个模块，但它就会突破其他一切。  
在其他地方，在终端仿真器中应该模拟图形终端：  
<ol> case invert_video：/ *现在是一个</ ol>  
<li>案例Invert_video：</ li>  
<li> / *现在是一个</ li>  
多年来几乎没有几个人不能开始评价一个人：  
在一个常见的内容中，为正在移植到C的一组代码的文件，我发现它已陈述：  
<ol> #define null 1 </ ol>  
<li> #define null 1 </ li>  
一天或两个人稍后同一个人，（现在谁现在正在运行不同的模块），将其改为：  
<ol> #define null 3 </ ol>  
<li> #define null 3 </ li>  
毋庸置疑，虽然这些变化得到了他当时在通过邮政移植术后测试的哪个模块，但它就会突破其他一切。  
在其他地方，在终端仿真器中应该模拟图形终端：  
<OL>案例INVERT_VIDEO：/ *现在是一个VGA显示，不支持逆视频，所以没有。 */     休息; </ OL>  
<li>案例Invert_video：</ li>  
<li> / *现在是一个VGA显示，不支持逆视频所以</ Li>  
<li>无所事事。 * / </ li>  
<li>打破; </ Li>  
虽然评论是严格的，但没有什么可以阻止代码交换前景和背景颜色 - 这一点少量的代码，导致在未来25年的黑色黑色上定期显示一些重要信息。  
怎么样：  
<ol> #define start_choice {#define选择（项目，fnid，val）案例％项目：return（函数_ %% fn（％val））;休息; #define end_choice} </ ol>  
<li> #define start_choice {</ li>  
<li> #define选择（项目，fnid，val）案例％项目：返回（函数_ %% fn（％val））;休息; </ Li>  
<li> #define end_choice} </ li>  
实际代码更加复杂，涉及更多的％迹象，但您可以获得图片。  
### 回答 13
不记得具体的线条，但是当我在一个Y2K项目工作时，有一系列的COBOL这是这样的。  
日期=日期+ 512  
我们花了大量的时间试图弄清楚为什么抵押计划将增加512到达日期。从来没有弄明白，但它成为我们项目经理的痴迷。  
### 回答 14
它是显示任何适用的项目列表。  
情况1：  
其中一些代码库中的人使用了所有IF-else语句。  
<ol> if（cond1）{if（cond2）... else ...} else {} </ ol>  
<li> if（cond1）</ li>  
<li> {</ li>  
<li> if（cond2）</ li>  
<li> ... </ li>  
<li> else </ li>  
<li> {</ li>  
<li>} </ li>  
有8条条件： - 他可以将它们添加到列表中。  
<ol> if（cond1）list.add（item1）... </ ol>  
<li> if（cond1）</ li>  
<li> list.add（item1）</ li>  
<li> ... </ li>  
一个更有趣的事件:(案例2）  
一些名为dilevep命名列的开发人员作为摊钱，仍然使用相同的列名称。  
我的一个朋友加入那个团队，他的技术领导给他发了一条消息，说数据不是来自摊钱，请检查。  
这家伙认为摊款应该给予数据，他正在寻找公社的摊钱  
它是显示任何适用的项目列表。  
情况1：  
其中一些代码库中的人使用了所有IF-else语句。  
<ol> if（cond1）{if（cond2）... else ...} else {} </ ol>  
<li> if（cond1）</ li>  
<li> {</ li>  
<li> if（cond2）</ li>  
<li> ... </ li>  
<li> else </ li>  
<li> {</ li>  
<li>} </ li>  
有8条条件： - 他可以将它们添加到列表中。  
<ol> if（cond1）list.add（item1）... </ ol>  
<li> if（cond1）</ li>  
<li> list.add（item1）</ li>  
<li> ... </ li>  
一个更有趣的事件:(案例2）  
一些名为dilevep命名列的开发人员作为摊钱，仍然使用相同的列名称。  
我的一个朋友加入那个团队，他的技术领导给他发了一条消息，说数据不是来自摊钱，请检查。  
这家伙认为摊款应该给数据，他正在寻找通信者的摊钱，但他没有找到这样的名字:)  
案例3：  
第二个是最有趣的事件，在听我的朋友叙事后，我们笑了大约30分钟。  
### 回答 15
最愚蠢的代码？  
可能这款宝石是一位前同事在Visual Basic 6中写道，我记得它很好：  
我= i + 1'这个增量我  
然后，再次回到1998年，我为继承了近海写的一些C ++代码。C ++最难以理解，但这是一个完全的混乱。  
在代码中，有一个名为RR的变量。你能猜到它是什么吗？  
错误代码。  
### 回答 16
//制作真正的随机数  
r = rand（）+ rand（）;  
在该样品中，R倾向于根据CLT的正常分布：  
中央极限定理 - 维基百科  
### 回答 17
<OL>公共静态最终字符串报价=;</ OL>  
<li>公共静态最终字符串报价=;</ Li>  
这是在一个严肃的公司的严重项目的主分支机构中（并且已经），该变量也用于某些地方。  
### 回答 18
大约5年前，同时优化一个由高级人建造的Drupal项目功能比我建造，我看到了直接写入项目根目录的一些.php文件。我打开了一个所需的文件和该死的，是：  
<ol>如果（true）{} {... ...} </ ol>  
<li>如果（true）{</ li>  
<li>} else {</ li>  
<li> ... </ li>  
<li>} </ li>  
到这一天，我不明白为什么如果使用else条件：d  
### 回答 19
不是一行代码，但许多程序员不会捕获错误。一个简单的'die（错误x）;会让我的工作（我也做故障排除）这么容易，并会让我很多时间......  
我大部分时间都看到了一个（PHP）项目，这些项目表现了一个使用他们可以找到的所有框架的公司的“有趣”它的一个“伟大”产品，用MVP设置膨胀，所有专业开发人员都假设一切都很好。在生产中，他们禁用ERROR_REPORTING（嗯，显然很好），但他们忘记了丝毫的数据库更改（例如，将字段设置为“not null”）可能会阻止DB插入。在这种情况下，狗屎应该死（）......不忽视它，所以我必须支持Al Zillion的代码行只是为了找出他们f * cked。  
tl;博士;没有或错误的错误处理是你能做的最愚蠢的事情（imho）。  
### 回答 20
我记得一个源自64位整数的时间的遗留项目。但是需要64和128位整数和数学操作。  
而不是使用32位值并检查溢出，那些家伙只是将整数转换为字符串并按列法实现了添加和乘法，就像在3年级的基本数学类中教授一样。  
### 回答 21
<OL>线程=新螺纹（SomerUnnable）;thread.start（）;thread.join（）;</ OL>  
<li>线程=新线程（SomerUnnable）;</ Li>  
<li> thread.start（）;</ Li>  
<li> thread.join（）;</ Li>  
什么是更有趣的，后来我仍在考虑这3行代码的时候，我想出了几个案例，实际上是有意义的：D  
### 回答 22
单位TE.  
我猜我见过的最愚蠢的代码是非单元测试中的测试代码。  
在某些时候，我注意到有一些功能不适用于仓库管理系统。调试大功能后（是的，他们没有写漂亮的代码）我看到了一个巨大的句子，如果（b> 1）...  
我问他为什么这样做。他回答说，他的基本思想是在一个大的if语句中封装一些代码，以便在if语句之外的值b来测试行为。太糟糕了，因为他忘了删除测试代码，然后关键功能不起作用。哎呀，那伤害了。  
单位测试不是我回来的公司的一部分。  
### 回答 23
在我之前的工作上，我发现了一个引起了很多问题的错误。我不知道是否故意测试我对Java或纯粹的愚蠢代码的了解  
有人试图为localdate使用simpleDateFormatter，它没有形成日期，但抛出异常，并且需要日期的值来制作导出的PDF。  
我更改了将localdate转换为java.util.date的代码，然后正确地编制了日期。  
### 回答 24
在Java.  
<ol> switch（value）{默认值：//代码中断行;} </ OL>  
<li>开关（值）{</ li>  
<li>默认值：</ li>  
<li> //有效的代码行</ li>  
<li>打破;</ Li>  
<li>} </ li>  
在非常乞求的是一个带有案例的开关，但随着时间的推移，从那天起，我从不忘记什么可以让他放松的交换机  
### 回答 25
这不是愚蠢的代码行，但这是一个有趣的错误;很久以前，系统中有一些代码格式化为字符串的日期/时间值。这是一般的，甚至可以告诉你特定日期的月球阶段。但是，它有一个错误，使得它在一个特定情况下扔了一个错误。  
当有一个人无法追踪看似随意发生的错误时，程序员有时会说'它取决于月球的阶段'。  
但这实际上是一个真正依赖月球阶段的错误。  
### 回答 26
我在相同的代码基础上看到了两个可爱的。  
铸造任务的左侧。当然，如果你正在写作：  
<ol> a =（int）b = c; </ OL>  
<li> a =（int）b = c; </ Li>  
它确实在一些奇怪情况下可能有用。但我看到的是：  
<ol>（int）a = b; </ OL>  
<li>（int）a = b; </ Li>  
我喜欢假设它是一个评论，以提醒某人的偏航类型。  
第二是：  
<ol> memset（缓冲区，0，sizeof（缓冲区））; Sprintf（记录，％s，buffer）; //零射出记录</ ol>  
<li> memset（缓冲区，0，sizeof（缓冲区））; </ Li>  
<li> Sprintf（记录，％s，缓冲区）; //零录制记录</ li>  
让它进入。首先，将缓冲区的每个字节设置为0.然后使用sprintf使用第一个字节，并且只使用第一个字节的缓冲区将第一个字节设置为0.但请务必覆盖  
我在相同的代码基础上看到了两个可爱的。  
铸造任务的左侧。当然，如果你正在写作：  
<ol> a =（int）b = c; </ OL>  
<li> a =（int）b = c; </ Li>  
它确实在一些奇怪情况下可能有用。但我看到的是：  
<ol>（int）a = b; </ OL>  
<li>（int）a = b; </ Li>  
我喜欢假设它是一个评论，以提醒某人的偏航类型。  
第二是：  
<ol> memset（缓冲区，0，sizeof（缓冲区））; Sprintf（记录，％s，buffer）; //零射出记录</ ol>  
<li> memset（缓冲区，0，sizeof（缓冲区））; </ Li>  
<li> Sprintf（记录，％s，缓冲区）; //零录制记录</ li>  
让它进入。首先，将缓冲区的每个字节设置为0.然后使用sprintf使用第一个字节，并且只使用第一个字节的缓冲区将第一个字节设置为0.但请务必包含暗示的注释你确实记录了你对缓冲的东西。这自然是缓冲区的唯一使用。  
### 回答 27
我认为很难提出单一，最愚蠢的代码，但我见过的最近最愚蠢的行是在一种试图获取连接字符串的凭据的方法中。它去了：  
<ol> string userid = configurationManager.AppSettings [用户ID]; if（string.isnulloremaly（userid））{userid = gazmo; } </ OL>  
<li> string userid = configurationManager.AppSettings [用户ID]; </ Li>  
<li> if（string.isnulloremaly（userid））</ li>  
<li> {</ li>  
<li> userid = gazmo; </ Li>  
<li>} </ li>  
此外，如果在.config文件中没有密码，则该方法返回了同一密码的默认情况下，该方法返回了相同的用户的默认值，硬编码密码。  
现在，让我解释为什么它是愚蠢的，如果使用硬编码的用户和连接字符串的密码  
我认为很难提出单一，最愚蠢的代码，但我见过的最近最愚蠢的行是在一种试图获取连接字符串的凭据的方法中。它去了：  
<ol> string userid = configurationManager.AppSettings [用户ID]; if（string.isnulloremaly（userid））{userid = gazmo; } </ OL>  
<li> string userid = configurationManager.AppSettings [用户ID]; </ Li>  
<li> if（string.isnulloremaly（userid））</ li>  
<li> {</ li>  
<li> userid = gazmo; </ Li>  
<li>} </ li>  
此外，如果在.config文件中没有密码，则该方法返回了同一密码的默认情况下，该方法返回了相同的用户的默认值，硬编码密码。  
现在，让我解释为什么它是愚蠢的，如果使用硬编码的用户和连接字符串的密码尚未触发您的代码olfactory感官。  
GAZMO是仅在开发人员和QAS用于测试的DEV和测试数据库中仅存在的用户。如果要在生产数据库上使用该代码，它将失败。  
此外，由于我无法在这里解释的原因，因此不会以这样的方式配置生产系统，以便在第2行导致条件进行评估。  
我是怎么绊倒的？在其他地方进行了一些变化后，涵盖案件的单元测试失败。  
如果在.config中没有存在有效的，则与提交的提交相关联的任务介绍了默认凭据。  
在那里，您有：不需要的代码，不会实际执行，是错误的，并且仅由单个单元测试使用。  
你现在可能想知道：为什么这段代码甚至存在？简单：Dilbert原理。这是我的前老板犯下的，然后是一位高级软件工程师2，目前是一个软件团队经理。他也恰好是一块人的垃圾。  
编辑：语法。  
### 回答 28
每次想到它都有一段代码让我厌恶地颤抖。这不仅仅是可怕的，对我来说，它违背了这么多水平的谷物。  
<ol>} catch（例外e）{if（e.getclass（）。toString（）.Equals（java.lang.nullpointereException）{dosomething（）;否则if（e.getclass（）。toString（）.Equals（java.sql.sqlexception）{dosomethingelse（）;否则如果（....）{...} else of（...} </ ol>  
<li>}捕获（例外e）{</ li>  
<li> if（e.getclass（）。ToString（）</ li>  
<li> .equals（java.lang.nullpointerexception）{</ li>  
<li> dosomething（）;</ Li>  
<li>} else if（e.getclass（）。ToString（）</ li>  
<li> .equals（java.sql.sqlexception）{</ li>  
<li> </ li>  
<li> dosomethingelse（）;</ Li>  
<li>}否则如果（....）{</ li>  
<li> ... </ li>  
<li>}否则如果（.. </ li>  
<li>} </ li>  
这是生产代码，它可能仍然是因为它的工作。  
### 回答 29
我写过的最愚蠢的代码是在我在Codeforces解决问题时。  
<ol> int x，y; CIN >> X >> Y; int ans =（x / y）* y </ ol>  
<li> int x，y; </ Li>  
<li> cin >> x >> y; </ Li>  
<li> int ans =（x / y）* y </ li>  
所以基本上如果你读取（x / y）* y你会说这个代码没有什么，ANS变量一直不会x右？但这里的诀窍是变量数据类型是int，所以ans变量不会始终是x，因为分数不会被计算。  
编辑：这个代码我写的是解决代码问题，它是一个愚蠢的代码，它通过了所提供的代码，所以我已接受的第一个两个测试用例，所以它已经解决了这个问题  
我写过的最愚蠢的代码是在我在Codeforces解决问题时。  
<ol> int x，y; CIN >> X >> Y; int ans =（x / y）* y </ ol>  
<li> int x，y; </ Li>  
<li> cin >> x >> y; </ Li>  
<li> int ans =（x / y）* y </ li>  
所以基本上如果你读取（x / y）* y你会说这个代码没有什么，ANS变量一直不会x右？但这里的诀窍是变量数据类型是int，所以ans变量不会始终是x，因为分数不会被计算。  
编辑：这个代码我为解决了一个守则问题，它是一个愚蠢的代码，它通过了所提供的代码，所以我接受了代码，这意味着它正确解决了这个问题我当被接受时震惊了，因为我认为这是完全错误的。  
### 回答 30
在一段代码中，我接管了程序员负责它退出的程序员，我在头文件中找到了以下行：  
#define true 0.  
#define假1  
我仍然有一半相信程序员，目的是使代码更难调试。它大多数正常，因为它（与这些行无关），但是当我在找到这些行之前尝试修改它时，我遇到了一些非常意外的行为。  
### 回答 31
情况1：  
代码是将数组中的字符串加入其中::在它们之间，除了第一个元素之外。  
这是它的编码方式：  
<OL>＃他加入了数组的所有元素My $ authtext =加入（::，@Array）; #then他在加入的字符串中排出的第一个元素#using Regex替换我的$ first = $ array [0]。 ::; $ authtext =〜s / $ first //; </ OL>  
<li>＃他加入了数组的所有元素</ li>  
<li> my $ authtext =加入（::，@ array）; </ Li>  
<li> #then他在加入的字符串</ li>中排出第一个元素  
<li> #using Regex替换</ li>  
<li>我的$ first = $ array [0]。 ::; </ Li>  
<li> $ authtext =〜s / $ first //; </ Li>  
最糟糕的部分是阵列中的元素是来自用户的纯文本。在随机的一天，阵列的第一个元素有一个打开的方括号（[），因此地面表达式创建了语法错误。  
他本来可以忽略第一个元素并加入休息  
情况1：  
代码是将数组中的字符串加入其中::在它们之间，除了第一个元素之外。  
这是它的编码方式：  
<OL>＃他加入了数组的所有元素My $ authtext =加入（::，@ array）; #then他在加入的字符串中排出的第一个元素#using Regex替换我的$ first = $ array [0]。 ::; $ authtext =〜s / $ first //; </ OL>  
<li>＃他加入了数组的所有元素</ li>  
<li> my $ authtext =加入（::，@Array）; </ Li>  
<li> #then他在加入的字符串</ li>中排出第一个元素  
<li> #using Regex替换</ li>  
<li>我的$ first = $ array [0]。 ::; </ Li>  
<li> $ authtext =〜s / $ first //; </ Li>  
最糟糕的部分是阵列中的元素是来自用户的纯文本。在随机的一天，阵列的第一个元素有一个打开的方括号（[），因此地面表达式创建了语法错误。  
他本来可以忽略第一个元素并加入其余的元素。  
案例2：  
下面的查询是在特定日期或之后使用DATECOLUMN值的表中从表中提取记录。  
<ol> select * from to_date的表（table.datecolumn，yyyy-mm-dd hh24：mi：ss）> = to_date（2018-08-13 00:00:00，yyyy-mm-dd hh24：mi：ss ）; </ OL>  
<li>选择</ li>  
<li> * </ li>  
<li>从</ li>  
<li>表</ li>  
<li>其中</ li>  
<li> to_date（table.datecolumn，yyyy-mm-dd hh24：mi：ss）> = to_date（2018-08-13 00:00:00，yyyy-mm-dd hh24：mi：ss）; </ Li>  
在这里，他试图将与日期的日期数据类型转换为日期的Coulumn的值（对我没有意义）。他在SQL ++工具中执行了此查询，它运行，因为会话日期格式是yyyy-mm-dd hh24：mi：ss。（to_date能够按照日期再次转换为），但在它遇到的作业框中运行时失败不同的会话日期格式。  
到这一天，我不知道为什么他用来转换约会。  
### 回答 32
事件1：  
<ol> void main（）; {/ *函数的主体* /} </ ol>  
<li> void main（）; </ Li>  
<li> {</ li>  
<li> / *函数的主体* / </ li>  
<li>} </ li>  
你在跟我开玩笑吗？？？？ （某人实际上以分号结束了主要功能）  
事件2：  
不完全是代码行，但我班上的一个人真的搞砸了oops的概念  
什么是封装？  
将数据和指令作为单个单位包装在一起。  
很简单！  
让我们看看这里的普雷表写了什么：  
（更改了隐私名称）  
在单个单位中强奸数据和说明！  
我们的先生（谁是谁，由于火星的一个人也是我的父亲）读了大声和我们所有人在内的所有人都嘲笑我们的驴子在下一个四十  
事件1：  
<ol> void main（）; {/ *函数的主体* /} </ ol>  
<li> void main（）; </ Li>  
<li> {</ li>  
<li> / *函数的主体* / </ li>  
<li>} </ li>  
你在跟我开玩笑吗？？？？ （某人实际上以分号结束了主要功能）  
事件2：  
不完全是代码行，但我班上的一个人真的搞砸了oops的概念  
什么是封装？  
将数据和指令作为单个单位包装在一起。  
很简单！  
让我们看看这里的普雷表写了什么：  
（更改了隐私名称）  
在单个单位中强奸数据和说明！  
我们的先生（谁是谁，由于火星的某种方式也是我的父亲）大声朗读，我们所有人在内的所有人都嘲笑我们的驴子在接下来的四十分钟内。  
它已经四年了，我又忘记了你没有封装。  
即使是现在，当我记得那个不幸的一天，我花了很多时间笑！  
r aka早期猫头鹰  
再见  
欢呼：D.  
### 回答 33
老实说，我不能说我见过一个真正愚蠢的代码线，我不能说我已经与之合作或听说过任何同事过去或现在真正做过愚蠢的事情。他们都至少有意图，做一些增加价值的东西，好事。  
我已经看到了很多角落切，但没有一个是愚蠢的。我可以回忆的最“糟糕”角落削减是（这是Java代码）人所做的地方：  
<OL> Object某种功能（...）{list <entity>结果列表= new linkedlist <>（）; ... return resultList.toArray（新对象[RESELLLIST.SIZE（）]）; void某些情况下（...）{对象</ ol>  
<li>对象某种功能（...）{</ li>  
<li>列表<entity>结果列表= new linkedlist <>（）; </ Li>  
<li> ... </ li>  
<li> return结果list.toArray（新对象[RESELLLIST.SIZE（）]）; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> void某些情况（...）{</ li>  
<li>对象</ li>  
老实说，我不能说我见过一个真正愚蠢的代码线，我不能说我已经与之合作或听说过任何同事过去或现在真正做过愚蠢的事情。他们都至少有意图，做一些增加价值的东西，好事。  
我已经看到了很多角落切，但没有一个是愚蠢的。我可以回忆的最“糟糕”角落削减是（这是Java代码）人所做的地方：  
<OL> Object某种功能（...）{list <entity>结果列表= new linkedlist <>（）; ... return resultList.toArray（新对象[RESELLLIST.SIZE（）]）; void以某种情况（...）{对象处理=某种功能;对象[] procestthingArray array =（对象[]）处理; for（对象元素：processthingArray）{Entity Entity =（实体）元素; ...}} </ ol>  
<li>对象某种功能（...）{</ li>  
<li>列表<entity>结果列表= new linkedlist <>（）; </ Li>  
<li> ... </ li>  
<li> return结果list.toArray（新对象[RESELLLIST.SIZE（）]）; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> void某些情况（...）{</ li>  
<li>对象处理=某种功能; </ Li>  
<li>对象[] procestthingArray array =（对象[]）处理; </ Li>  
<li> for（对象元素：processthingarray）{</ li>  
<li>实体实体=（实体）元素; </ Li>  
<li> ... </ li>  
<li>} </ li>  
这是令人反感的，说最少和如此非常不必要的角落。它令人困惑，有助于更多的努力，而不是做到整洁的方式。有礼貌的方式：  
<ol>列表<实体>某种功能（...）{list <entity>结果列表= new linkedlist <>（）; ...返回结果表; void某些方法（...）{list <entity> procestthing = somefunction（...）; for（实体实体：processthing）{...}} </ ol>  
<li>列表<实体>某种功能（...）{</ li>  
<li>列表<entity>结果列表= new linkedlist <>（）; </ Li>  
<li> ... </ li>  
<li>返回结果表; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> void某些情况（...）{</ li>  
<li>列表<实体> procestthing = somefunction（...）; </ Li>  
for（实体实体：Processthing）{</ li>  
<li> ... </ li>  
<li>} </ li>  
### 回答 34
我在一个程序上工作了，其中有超过260个调用system.exit（）通常基于一些未知错误而不记录为什么。  
例如  
<ol> if（properties.size（）> 10000）system.exit（1）;</ OL>  
<li> if（properties.size（）> 10000）</ li>  
<li> system.exit（1）;</ Li>  
### 回答 35
我在几年前工作过没有模数运营商。以前的团队通过从循环中的股息中减去偏差，直到该数字小于偏差者，因此获得了模数。  
### 回答 36
我已经看到了每个SRC文件（如100个文件）应用此模式：  
<ol>试试{...有一些代码} catch（例外Exc）{oppl;} </ OL>  
<li>尝试{</ li>  
<li> ...这里有一些代码</ li>  
<li> catch（例外Exc）{</ li>  
<li>扔;</ Li>  
<li>} </ li>  
### 回答 37
我已经看到了以下样式的C代码：  
<ol> if（条件）goto标签1;做一点事（）;转到标签2;标签1：dosomethingelse（）;标签2：</ OL>  
<li> if（条件）goto标签1;</ Li>  
<li> dosomething（）;</ Li>  
<li> goto标签2;</ Li>  
<li>标签1：</ li>  
<li> dosomethingelse（）;</ Li>  
<li>标签2：</ li>  
### 回答 38
我会告诉你可能是一个我现在所说的一个人的最愚蠢的人，它是由我写的。虽然这不是那么愚蠢。  
它是：  
if（1 == 3）{  
（数十行代码）  
}  
但它是故意的。  
我曾经在那个项目上工作，为那家公司创造整个内联网，但我计划离开，一位同事试图继续我的工作。  
有些日子我见过他有点沮丧，而且很紧张，也许想着他无法继续我的工作，我问他是否需要帮助，他说不需要，谢谢，我可以做到。  
他有几天，直到他告诉我一天：你让我松散的ALM  
我会告诉你可能是一个我现在所说的一个人的最愚蠢的人，它是由我写的。虽然这不是那么愚蠢。  
它是：  
if（1 == 3）{  
（数十行代码）  
}  
但它是故意的。  
我曾经在那个项目上工作，为那家公司创造整个内联网，但我计划离开，一位同事试图继续我的工作。  
有些日子我见过他有点沮丧，而且很紧张，也许想着他无法继续我的工作，我问他是否需要帮助，他说不需要，谢谢，我可以做到。  
他遭受了一些日子，直到有一天他告诉我：你让我松散了几乎一周的时间寻找血腥的错误或丢失的代码，我找不到任何地方，并且只有今天我发现了这个，如果我发现了它（1 = = 3）这里!!!我只需要删除它的工作，如果我知道你已经完成了这一点，我本可以在10秒内完成这一点，而不是整整一周！  
我向他解释了，就像我一个人一样，当时我对我来说更容易，只是为了（1 == 3）{评论大块代码，而不受/ *和中里面的评论。  
当然，具有if（1 == 3）的评论代码不会显示评论！  
他理解为什么我使用了（1 == 3），但他真的很生气，因为几天来搜索一些用if（1 == 3）评论的一些评论代码。  
他说他甚至更改了内部的代码，如果声明，几次并不明白为什么问题没有解决哈哈（因为它被评论而且他不知道）。  
当我想搜索评论代码时，我有时会搜索1 == 3。 ：D.  
他说这是愚蠢的。这可能是他作为程序员的最糟糕的噩梦。  
几年过去了，我现在仍然这样做，在C / C ++甚至PHP等中。  
但现在我只有单独编程。至少我可以自由地使用if（1 == 3）。 :)  
### 回答 39
我认为这是最好奇的：  
<ol> var somebadvariablename = 1.tostring（）;</ OL>  
<li> var somebadvariablename = 1.tostring（）;</ Li>  
最愚蠢的可能不是单行，而是巨大的代码，所以我可能（绝对）不能在Quora上转储整个代码库。  
我公司之一的一个项目是一个WPF应用程序，大多数应用程序都是用单对XAML文件和代码背后写入的。  
我的同事玩得很有趣的时间重写它，然后我稍后有了重写UI（当我到达它时仍然有很多愚蠢）  
### 回答 40
由于几乎所有的例子都来自现代​​语言（C和Perl），请让我提供一个更经典的编程语言，fortran ...  
线本身并不愚蠢，而是通过设计决策的组合，它归因于灾难性的应用。  
这是一个问题的子程序的片段......  
<ol>子程序read_file（data，file_name，file_id）！ ---参数和变量声明打开（Unit = file_id，file = file_name）！ ---子程序结束子程序read_file </ OL>  
<li>子程序read_file（data，file_name，file_id）</ li>  
<li>！ ---参数和变量声明</ li>  
<li>打开（Unit = file_id，file = file_name）</ li>  
<li>！ ---剩下的子程序</ li>  
<li> </ li>  
<li>结束子程序read_file </ li>  
ReadFilereadFile中子程序的相关部分是它打开文件并存储文件  
由于几乎所有的例子都来自现代​​语言（C和Perl），请让我提供一个更经典的编程语言，fortran ...  
线本身并不愚蠢，而是通过设计决策的组合，它归因于灾难性的应用。  
这是一个问题的子程序的片段......  
<ol>子程序read_file（data，file_name，file_id）！ ---参数和变量声明打开（Unit = file_id，file = file_name）！ ---子程序结束子程序read_file </ OL>  
<li>子程序read_file（data，file_name，file_id）</ li>  
<li>！ ---参数和变量声明</ li>  
<li>打开（Unit = file_id，file = file_name）</ li>  
<li>！ ---剩下的子程序</ li>  
<li> </ li>  
<li>结束子程序read_file </ li>  
ReadFilereadfile中的子程序的相关部分是它打开文件并将文件句柄存储在参数FileIdfileId中，以便可以在其他地方使用。  
它可能不采取天才意识到，如果fileidfileId已分配给另一个文件，则调用另一个文件上的readfilereadfile将强制fileidfiled引用较新文件。通常，如果FileIDfileID具有有限的范围和文件关闭，则不会是一个问题，但是开发经理，一个旧的Dude，一个带有Die Fortran / 77态度的旧家伙，要求所有变量全局访问。作为进一步巩固代码基础的尝试，他还强调所有文件处理持续打开。他的逻辑是，由于程序出口时它们会自动关闭，为什么要浪费另一行代码来明确关闭它们？  
结果是相当可预测的。全局句柄将定期被其他开发人员覆盖，因为他们不知道已经分配了哪个句柄，以及哪个文件，您最终读取或（更差）写入未知文件。在厌倦此之后，我决定在未使用时将自己的FileDfileIds本地封闭并关闭它们。  
### 回答 41
我可以做得更好。有一个整个Lotus 123电子表格宏观应用程序，这是如此复杂，所以组织得很厉害，甚至无法确定它如何正常运作。就像一群中世纪的德鲁伊，那些只曾经碰过某些细胞的人，也可以点燃香烟，或者也许是陈旧的香烟。  
我决定也许我可以打印出代码并搞清楚。与Excel不同，它在自己的单独文件中存储宏码，Lotus刚刚将其放在函数中的随机单元格中。在打印出来后，它超过了一百页的电子表格，可以在某个点宽，并且在长度为20页之前。我接过一个会议室试图搞清楚。它是通过电子表格进行预算的Necromonicon。这是一个令人恐惧的噩梦，今天叫醒我，在一个冷的汗水中尖叫着谁将在Cell C：567中放置一百线逻辑代码！  
最终我带来了需要这个申请的部门的头部，并给了他们坏消息。不，这不会像Excel一样拯救，摇动剩下的一些问题。我有两个选择。  
他们选择选项2，直到他们可以将预算正确重做。我相信有一台电脑包围着乳香，一系列钟声仍然经营公司的长期设备预算。  
编辑：为读取此读取的后代修复拼写错误。  
哇7k喜欢。非常感谢你。  
阅读关于这是关于这是多么普通的评论，我已经加入了一个世界末日预先预付款，我是在不可避免的崩溃发生的情况下贸易的库存堆积食品，太阳能电池板和486个电脑零件。我必须用我的DOS技能拯救社会。  
### 回答 42
我。  
我是一个可怕的程序员。我的代码总是非常写。我只使用易于编程语言的基本功能。我的方法很弱，他们可以重写，以便他们更有效地运行。我寻求帮助上的stackoverflow和谷歌数百次来编写相当简单的代码。大多数时候我都不完全明白我的复制。我只是粘贴那个友好的代码，运行程序，如果它有效，我很高兴:)但它只工作了50％的时间，因为有时我不明白如何正确地将该代码放在我的程序中。我不记得任何语言的语法。所以我必须几乎每次需要它们时都在线看。即使是最简单的和基本的，也可以像循环的语法或Java中类型的类型（不是开玩笑）的语法。我很慢。我需要比普通程序员更多的时间比平均程序员写入基本功能。我的代码是非常不专业的，我需要在一小时前在我的代码中使用的互联网上查找基本的东西。  
但！  
我设法在所有的Android应用程序上获得100,000 00,000下载！我为此感到骄傲。游戏很简单，但人们喜欢他们。平均评级为4.2 / 5。我不得不测试。做出改变。重新设计整个应用程序多次。分析用户行为并更改应用程序的某些部分以满足他们的需求。我每天都会得到几十个星级评分和令人敬畏的评论，让我开心。我从第1天货币化了我的应用程序，所以我也没有从我的创作中收入不好。我用营销策略进行了多大实验。有些人没有工作。有些人已经提升了我的下载。我在Quora学到了很多，我非常感谢这个令人敬畏的社区！我还在Udemy上买了一些课程（在购买课程之前总是谷歌搜索优惠券）。 Thay也帮我了很多。  
所以我正在写这个答案的原因是，即使你知道你在世界上最糟糕的20％甚至1％之间，你仍然可以成功。做你爱做的。激情让奇迹。  
### 回答 43
在许多设计缺陷中，两个最令人震惊的  
当我在现有的现有（虽然过时的）电子商务网站上作为领导开发人员开始新的工作时，我任务了解具有愿望清单，信用卡付款，采购订单等功能的新的购物车系统。  
我分析的第一部件之一是购物图表/信用卡系统，该系统已经作为一十年的经济实惠的第三方插件购买。我被这个模块的设计如此惊慌，它立即成为我最优先的更换，不能等待任何其他模块推出。  
在许多设计缺陷中，两个最令人惊叹的：  
### 回答 44
我工作了一段时间（现在已经过错了）搜索引擎公司，其中间件由疯狂的人（约有5000个Java源文件）撰写的。一些特点：  
这家公司有一个新的首席执行官，他们希望将这东西卖给其他行业，而不是美国政府的三个字母代理商，我被聘请用可靠的东西取代这东西。然而，他们在顾问中追溯到弗吉尼亚地下室的顾问上，当它损坏了自己的数据时，在弗吉尼亚州托幼儿，并用十六进制编辑来解决这些数据，这是每天几次。软件尴尬地破碎的是他们的现金牛。而且我了解到这并不罕见。  
所以我不知道为什么斯诺登可以访问他可以访问的东西，或者为什么obamacare网站的第一个版本是灾难，或者为什么希拉里可能不想使用承包商运行的邮件系统。这是政府的状态。  
编辑：由于有些人怀疑这个码比赛中的疯狂程度，我会从中留下这个小宝石，我最近在阅读一些旧电子邮件时找到。它有什么作用？它需要一个整数。并将其转换为字符串 - 即，请使用2并获得2.将字符串转换回整数 - 需要2并将其解析为2.并返回。换句话说，除了浪费CPU周期之外，此代码没有任何内容完成。什么都没有。它是从码比上的各种调用。  
<ol> public int fn_gs_as_int（int fi_p）{string fl_v = fn_gs_as_as_str（fi_p）;返回fn_str_to_int（fl_v）; } </ OL>  
<li> public int fn_gs_as_int（</ li>  
<li> int fi_p）</ li>  
<li> {</ li>  
<li>字符串fl_v = fn_gs_as_str（fi_p）; </ Li>  
<li>返回fn_str_to_int（fl_v）; </ Li>  
<li>} </ li>  
### 回答 45
以下事件对我来说太令人震惊，即使今天我与其他程序员谈论这一点。  
事件。  
### 回答 46
这发生在90年代的某个地方。我正在使用我们公司建造的新中间件的C ++库。该图书馆由HQ的研发团队开发，我在一个不同的国家。电子邮件是我与研发团队沟通的唯一方法。  
这是在大多数C ++编译器有适当的标准库之前。然后每个主要项目都创建了自己的字符串类，以满足他们的需求。而这个中间件的字符串类看起来像这样的东西：  
你看到这个问题吗？分配运算符是CONST功能。这意味着Const合同被侵犯。这将使以下代码有效。  
输出：  
我通过电子邮件联系了开发人员，他告诉我它是通过设计，并让我克服它。我对他的傲慢感到愤怒，并开始通过电子邮件争论解释它可能导致的伤害，同时保持他的老板和我的老板在CC中。这持续了一周，他终于承认了这是一个理由作为解决方法。修复它会破坏很多代码，所以他从未重新审视它。  
该公司计划将此中间件销售为100多家客户，并将使用此C ++库。如果将常量字符串传递给此库中的任何功能，则无法保证不会更改。一位高级C ++开发人员的恐怖设计决定。  
我不记得他是否固定它。无论如何，它并不重要，因为产品由于价格不好而浮现。  
### 回答 47
我主要是因为我看到很多答案都没有真正地解决过于解决的答案。我不是说所有人，但公平的数字不是真正的过度工程的纯粹例子。它们更好地描述为A）的例子是年轻和缺乏经验的或b）不了解问题或c）只是引入效率低下并且不起作用的坏代码。  
过度工程是过度思考问题的过程，产生过度卷积，然而，可能非常聪明，通常是非常通用的代码，其实在现实中最终难以使用，理解或维护。  
一个例子是工程师创造一个如此令人惊讶的系统的人，使得它可以用来在特定主题域中解决几乎任何问题，但是当实施时，当实施时是一个噩梦，因为它是如此疯狂地从问题中抽象出来。  
过度工程的最大迹象是当代码到目前为止抽象出来的问题，你几乎无法找到一块实际代码，一种方法，可变分配，一些具体实施的东西，等等。  
编辑：几个用户想要一个例子或回答，更好地说明概念并回答问题。同样，将代码放在这个论坛中对于大多数现实世界问题来说是禁止的，所以我将提供一些额外的插图和信息。  
过度工程卡通（伟大的比喻）：  
卡通的点，为什么它说明过于工程，是最终用户（桌子末尾的家伙）只是想要一些盐。这告诉我们什么？避免过度工程的最佳事物之一是不要设计到未来的太远，猜测您的客户可能会要求的内容。这可以是计算的风险，或者是一个良好的业务举措，如果您知道您拥有客户或业务需求将在那里，但您需要仔细考虑它。  
超过工程通常会在您提供超过要求的情况下发生的。我问你锤子，水平和螺丝刀。你去商店并用整个300pc力学工具集回来。这很好，但不必要（B / C在这种情况下我只是挂了一张图片）。有时你可能想要这样做，但你需要仔细考虑他们。  
它通常发生的另一种方式是通过过度抽象。上面的卡通是这个问题的一个完美的例子。它不仅在表格需要结束时提供的远远超过用户，另一个人正在创建一些通用，抽象的系统，以便无论谁要求某种东西，无论什么样的调味品，都可以处理。系统不再适用于盐，创建了一层抽象，然后他建立了系统，为该用户的盐来实现它。一个漫长的过程。在这种情况下不必要。您可以再次进一步逐步摘要，并说这不仅仅是一种传递调味品的系统，现在它将成为通过任何物品的系统。您可以进一步逐步说明它不仅仅是传递项目，它可以组合它们，添加它们，减去它们。另一个步骤更进一步，它不再只是物品，但现在它几乎是什么。  
抽象不差，这是一个精彩的概念，你只需要小心你在寻求方面有多远来实现完美的松散耦合和高凝聚力。  
### 回答 48
A2A by Josh Knight [https://www.quora.com/profile/josh-knight-19]。我正在回答这个问题作为软件工程师，开发人员和/或程序员;您在Codebase中见过的最野蛮评论是什么？  
您的问题导致我记得收购由公司源代码中的单一评论保存的软件公司。不是你想到的，而是一个有趣的战争故事。  
1986年末，我对r ...的电子表格计划的源代码进行了困扰  
### 回答 49
问：作为一个软件工程师，您已经看到的一行代码是什么，吹过你的想法？  
THX为A2A。  
没有单一的代码我会促进这个状态。  
相反，有许多技巧恕我乎令人惊叹：  
<a> [1] </a>  
脚注  
