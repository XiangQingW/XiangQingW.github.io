---

title: 如何从Python中的另一个函数调用变量？
date: 2022-01-23T22:08:28+08:00

---




## 如何从Python中的另一个函数调用变量？  
### 回答 1
Aloha !!  
如果U R要求如何调用1个函数的变量，则可能的方式是 -   
第一路  
<ol> def a（）：a.i =变量＃函数属性def b（）：a（）＃调用函数打印（a.i）＃acess变量b（）</ ol>  
<li> def a（）：</ li>  
<li> a.i =变量＃函数属性</ li>  
<li> def b（）：</ li>  
<li> a（）＃调用函数</ li>  
<li>打印（a.i）＃Acess变量</ li>  
<li> </ li>  
<li> b（）</ li>  
第二次  
<ol> def a（）：全局i i =变量＃global变量def b（）：a（）＃自从我们在a（）中达到全局，我们需要调用a（）打印（i）b（i）b（）</ OL>  
<li> def a（）：</ li>  
<li>全球I </ Li>  
<li> i =变量＃全局变量</ li>  
<li> def b（）：</ li>  
<li> a（）＃由于我们将i作为全局在a（）中，我们需要调用a（）</ li>  
<li>打印（i）</ li>  
<li> </ li>  
<li> b（）</ li>  
jd.  
### 回答 2
tldr：返回变量。还有其他方法，但它们并不清洁。  
这就是我理解你的问题的方式：如何访问在Python函数中定义的变量？  
我认为你有这样的东西：  
<ol> def foo（）：＃做一些事情。 a = 42返回10 </ OL>  
<li> def foo（）：</ li>  
<li>＃做一些事情。 </ Li>  
<li> a = 42 </ li>  
<li>返回10 </ li>  
我们定义一个函数，说foo，做一些非常重要的东西和返回10.在foo内部我们定义了一个可变的a，您要在Foo之外访问。  
解决方案1：使用返回。  
在Foo外面的清洁方式是返回它。您可以返回任意对象，因此您可以返回默认响应（在我们的情况下10）  
tldr：返回变量。还有其他方法，但它们并不清洁。  
这就是我理解你的问题的方式：如何访问在Python函数中定义的变量？  
我认为你有这样的东西：  
<ol> def foo（）：＃做一些事情。 a = 42返回10 </ OL>  
<li> def foo（）：</ li>  
<li>＃做一些事情。 </ Li>  
<li> a = 42 </ li>  
<li>返回10 </ li>  
我们定义一个函数，说foo，做一些非常重要的东西和返回10.在foo内部我们定义了一个可变的a，您要在Foo之外访问。  
解决方案1：使用返回。  
在Foo外面的清洁方式是返回它。您可以返回任意对象，因此您可以返回默认响应（在我们的案例10中）和包含在元组，列表，字典或甚至是自定义类类的实例中的变量A.  
<OL>＃解决方案使用元组。 def foo（）：＃做一些事情。 a = 42返回（10，a）foo（）[0]＃10 foo（）[1]＃42 </ OL>  
<li>＃解决方案使用元组。 </ Li>  
<li> </ li>  
<li> def foo（）：</ li>  
<li>＃做一些事情。 </ Li>  
<li> a = 42 </ li>  
<li>返回（10，a）</ li>  
<li> </ li>  
<li> foo（）[0]＃10 </ li>  
<li> foo（）[1]＃42 </ li>  
我将这种灵魂视为清洁，因为它没有将隐藏的元素引入您的命名空间（既不是包含全局的模块命名空间，也不是与功能属性的函数命名空间。输入 - 输出系统是函数的默认接口。  
所说的，也许这些其他解决方案中的一个符合您的用例。  
解决方案2：使用全局。  
全局变量无处不在。您可以在函数中定义全局变量。您无法从函数中编辑它们而不将其声明为全局首先。  
<ol> def foo（）：＃做一些事情。全球A = 42返回10 foo（）＃10 a＃42 </ ol>  
<li> def foo（）：</ li>  
<li>＃做一些事情。 </ Li>  
<li>全球a </ li>  
<li> a = 42 </ li>  
<li>返回10 </ li>  
<li> </ li>  
<li> foo（）＃10 </ li>  
<li> a＃42 </ li>  
在foo内，我们将a声明为全局变量。 A目前无处不在。  
请注意，我们仍然需要打电话。刚刚定义函数不会在运行时运行其代码。这种方法的缺点是模块的全球状态现在在运行时至少召集一次，而不是FOO。  
解决方案3：使用函数属性。  
一切都是Python中的一个对象，甚至是函数。这就是为什么您可以像对象一样分配要用的属性。  
<ol> def foo（）：＃做一些事情。 foo.a = 42返回10 foo（）＃10 foo.a＃42 </ OL>  
<li> def foo（）：</ li>  
<li>＃做一些事情。 </ Li>  
<li> foo.a = 42 </ li>  
<li>返回10 </ li>  
<li> </ li>  
<li> foo（）＃10 </ li>  
<li> foo.a＃42 </ li>  
这个Solutuon与前一个人基本相同，除了您修改的命名空间是Foo之一。  
它具有相同类型的缺点。您基本上在动态存储名称空间中的值，然后期望使用它来了解在哪里看的代码以及它被放置在那里。  
### 回答 3
你不能调用变量;您只能调用函数。我认为这个问题更为恰当是恰当的措辞，你如何访问另一个函数中使用的变量？  
如果变量是本地的（默认为Python变量），那么您绝对不能。除非将其作为当前功能的参数传递，否则无法访问来自另一个函数的本地变量。  
全局变量是另一件事。它们由任意数量的函数共享，它们会在函数调用之间保留其值。  
Python中的全局变量有点复杂解释。但使用全局变量的最简单方法如下：  
### 回答 4
从函数内部访问全局变量  
<ol> c = 1＃全局变量def add（）：print（c）add（）</ ol>  
<li> c = 1＃全局变量</ li>  
<li> def add（）：</ li>  
<li>打印（c）</ li>  
<li> </ li>  
<li> add（）</ li>  
当我们运行上述程序时，输出将是：  
<OL> 1 </ OL>  
<li> 1 </ li>  
但是，我们可能有一些方案，我们需要从函数内部修改全局变量。  
示例2：从功能内部修改全局变量  
<ol> c = 1＃全局变量def add（）：c = c + 2＃增量c by 2 print（c）add（）</ ol>  
<li> c = 1＃全局变量</ li>  
<li> def add（）：</ li>  
<li> c = c + 2＃增量c by 2 </ li>  
<li>打印（c）</ li>  
<li> </ li>  
<li> add（）</ li>  
当我们运行上述程序时，输出显示错误：  
<ol> unboundlocalerror：局部变量c在分配之前引用</ ol>  
<li> unboundlocalerror：在分配之前引用的局部变量c </ li>  
这是因为我们只能访问全局变量，但无法修改它  
从函数内部访问全局变量  
<ol> c = 1＃全局变量def add（）：print（c）add（）</ ol>  
<li> c = 1＃全局变量</ li>  
<li> def add（）：</ li>  
<li>打印（c）</ li>  
<li> </ li>  
<li> add（）</ li>  
当我们运行上述程序时，输出将是：  
<OL> 1 </ OL>  
<li> 1 </ li>  
但是，我们可能有一些方案，我们需要从函数内部修改全局变量。  
示例2：从功能内部修改全局变量  
<ol> c = 1＃全局变量def add（）：c = c + 2＃增量c by 2 print（c）add（）</ ol>  
<li> c = 1＃全局变量</ li>  
<li> def add（）：</ li>  
<li> c = c + 2＃增量c by 2 </ li>  
<li>打印（c）</ li>  
<li> </ li>  
<li> add（）</ li>  
当我们运行上述程序时，输出显示错误：  
<ol> unboundlocalerror：局部变量c在分配之前引用</ ol>  
<li> unboundlocalerror：在分配之前引用的局部变量c </ li>  
这是因为我们只能访问全局变量，但无法从函数内修改它。  
解决方案是使用全局关键字。  
### 回答 5
您可以使用全局关键字从Python中的另一个函数调用变量。例如：  
def示例（）：  
a = 2  
全球A.  
打印（a）  
要了解更多关于全局关键字，请注意以下视频：  
### 回答 6
您可以在最后使用返回统计。  
并在调用它的变量中存储它  
例子 ：  
def func1（）：  
A = 10.  
返回A.  
调用功能  
var = func1.  
10将存储在var中，因为它由func1返回  
在第二个功能中使用var  
### 回答 7
你不叫变量。您名称变量。在函数内定义的变量不存在于该函数的调用外部。所以你不能说明它。如果您需要在另一个函数中的值，那就是参数的。  
### 回答 8
您的原始代码是：  
<ol> def func1（）：a = 8 b = 9 def func2（x，y）：z = x + y + a + b返回z a = func2（4,6）打印（a）</ ol>  
<li> def func1（）：</ li>  
<li> a = 8 </ li>  
<li> b = 9 </ li>  
<li> def func2（x，y）：</ li>  
<li> z = x + y + a + b </ li>  
<li>返回z </ li>  
<li> </ li>  
<li> a = func2（4,6）</ li>  
<li>打印（a）</ li>  
做这件事有很多种方法 ：  
<OL>＃使用返回值＃将对Func2的调用依赖于Func1 Def Func1（）的结果数量依赖于呼叫的结果：a = 8 b = 9返回a，b def func2（x，y，args）： a，b = * args＃从参数z = x + y + a + b返回z a = func2（4,6，args = func1（））打印（a）＃但是您可以执行以下操作：a = func2（ 4,6，args =（9,11））＃您不需要创建数据的函数</ ol>  
<li>＃使用返回值</ li>  
<li>＃明确地呼叫func2依赖于结果</ li>  
<li>对Func1的呼吁</ li>  
<li> </ li>  
<li> def func1（）：</ li>  
<li> a = 8 </ li>  
<li> b = 9 </ li>  
<li>返回a，b </ li>  
<li> </ li>  
<li> def func2（x，y，args）：</ li>  
<li> a，b = * * args＃从参数中解压缩</ li>  
<li> z = x + y + a + b </ li>  
<li>返回z </ li>  
<li>打印（a）</ li>  
<li> </ li>  
<li>＃但你可以做：</ li>  
<li> a = func2（4,6，args =（9,11））＃您不需要创建数据的函数</ li>  
或者  
<OL> #pass函数：＃在此解决方案中，您可以在您调用#func2时进行呼叫func1：func </ ol>  
<Li> ##通过功能：</ li>  
<li>＃在此解决方案中，您正在调用</ li>时显而易见  
<li> #fuc2需要调用func1：func </ li>  
您的原始代码是：  
<ol> def func1（）：a = 8 b = 9 def func2（x，y）：z = x + y + a + b返回z a = func2（4,6）打印（a）</ ol>  
<li> def func1（）：</ li>  
<li> a = 8 </ li>  
<li> b = 9 </ li>  
<li> def func2（x，y）：</ li>  
<li> z = x + y + a + b </ li>  
<li>返回z </ li>  
<li> </ li>  
<li> a = func2（4,6）</ li>  
<li>打印（a）</ li>  
做这件事有很多种方法 ：  
<OL>＃使用返回值＃将对Func2的调用依赖于Func1 Def Func1（）的结果数量依赖于呼叫的结果：a = 8 b = 9返回a，b def func2（x，y，args）： a，b = * args＃从参数z = x + y + a + b返回z a = func2（4,6，args = func1（））打印（a）＃但是您可以执行以下操作：a = func2（ 4,6，args =（9,11））＃您不需要创建数据的函数</ ol>  
<li>＃使用返回值</ li>  
<li>＃明确地呼叫func2依赖于结果</ li>  
<li>对Func1的呼吁</ li>  
<li> </ li>  
<li> def func1（）：</ li>  
<li> a = 8 </ li>  
<li> b = 9 </ li>  
<li>返回a，b </ li>  
<li> </ li>  
<li> def func2（x，y，args）：</ li>  
<li> a，b = * * args＃从参数中解压缩</ li>  
<li> z = x + y + a + b </ li>  
<li>返回z </ li>  
<li>打印（a）</ li>  
<li> </ li>  
<li>＃但你可以做：</ li>  
<li> a = func2（4,6，args =（9,11））＃您不需要创建数据的函数</ li>  
或者  
<OL>＃通过功能：＃在这个解决方案中，您正在明确调用#fucc2时需要调用func1：func1是一个帮助函数def func1（）：a = 8 b = 9返回a，b def func2（ x，y，func）：a，b = func（）z = x + y + a + b返回z a = func2（4,6，func1）打印（a）＃如果您有另一个函数，则生成一对值＃您可以通过它太多</ ol>  
<Li> ##通过功能：</ li>  
<li>＃在此解决方案中，您正在调用</ li>时显而易见  
<li> #fuc2需要调用func1：func1是一个辅助功能</ li>  
<li> </ li>  
<li> def func1（）：</ li>  
<li> a = 8 </ li>  
<li> b = 9 </ li>  
<li>返回a，b </ li>  
<li> </ li>  
<li> def func2（x，y，func）：</ li>  
<li> a，b = func（）</ li>  
<li> z = x + y + a + b </ li>  
<li>返回z </ li>  
<li> a = func2（4,6，func1）</ li>  
<li>打印（a）</ li>  
<li> </ li>  
<li>＃如果您有另一个函数，它会生成一对值</ li>  
<li>＃你可以通过它太多了  
我会说根本不使用全局 - 他们看起来像一个快速的解决方案，但它们是一个非常糟糕的习惯。  
通过定义是关于函数工作方式的信息，它可以在函数之外的参数之外，这可以使您的功能更难以测试 - 因为您现在必须将参数传递给您的功能并单独设置相关的全局值要测试函数（您确实测试了您的函数，不是你）.Sometsimes，无法远离全局数据（例如数据库，外部网站），您必须有时跳过箍以测试您的代码当你有外部数据 - 但不要让生活对自己更加困难。  
### 回答 9
请不要。  
### 回答 10
如果我们在函数内定义了一个变量，那么我们直接无法在函数之外或在任何其他函数中访问该变量（这里列表），因为该变量的范围仅限于函数本身。但如果该函数返回该变量，则可以访问它。  
<ol> def一个（）：lis = [1,2,3,4]返回lis def second（）：#access函数列表一个lis = One（）打印（LIS）第二（）</ OL>  
<li> def一个（）：</ li>  
<li> lis = [1,2,3,4] </ li>  
<li>返回lis </ li>  
<li> </ li>  
<li> def second（）：</ li>  
<li> #access函数列表一个</ li>  
<li> lis = One（）</ li>  
<li>打印（lis）</ li>  
<li> </ li>  
<li>第二（）</ li>  
### 回答 11
标准答案是FUNC2（FUNC1（VAL）））。  
但是，如果FUNC1的输出类型与FUNC2不兼容，则会遇到问题。因此，您可以使用str＆int进一步扩展。  
但对于更有趣，您还可以在功能内调用函数。  
<ol> def func1（val）：def func2（str）：返回嘿+ str def func3（int）：return int + 2 try：print（这是一个字符串：+ val）返回func2（val）除typeerror之外：print （这是（可能）一个int：+ str（val）返回func3（val）x = func1（dude）//这是一个字符串：dude x =嘿dude y = func1（4）//这可能是一个int ：4 x = 6 </ OL>  
<li> def func1（val）：</ li>  
<li> def func2（str）：</ li>  
<li>返回嘿+ str </ li>  
<li> def func3（int）：</ li>  
<li>返回int + 2 </ li>  
<li>尝试：</ li>  
<li>打印（这是一个字符串：+ val）</ li>  
<li>返回func2（val）</ li>  
<li>除了TypeError：</ Li>  
<li>打印（这是（可能）int：+ str（val）</ li>  
<li>返回func3（val）</ li>  
<li> </ li>  
<li> x = func1（dude）//这是一个字符串：dude x =嘿dude </ li>  
<li> y = func1（4）//这可能是int：4 x = 6 </ li>  
或者你可以  
标准答案是FUNC2（FUNC1（VAL）））。  
但是，如果FUNC1的输出类型与FUNC2不兼容，则会遇到问题。因此，您可以使用str＆int进一步扩展。  
但对于更有趣，您还可以在功能内调用函数。  
<ol> def func1（val）：def func2（str）：返回嘿+ str def func3（int）：return int + 2 try：print（这是一个字符串：+ val）返回func2（val）除typeerror之外：print （这是（可能）一个int：+ str（val）返回func3（val）x = func1（dude）//这是一个字符串：dude x =嘿dude y = func1（4）//这可能是一个int ：4 x = 6 </ OL>  
<li> def func1（val）：</ li>  
<li> def func2（str）：</ li>  
<li>返回嘿+ str </ li>  
<li> def func3（int）：</ li>  
<li>返回int + 2 </ li>  
<li>尝试：</ li>  
<li>打印（这是一个字符串：+ val）</ li>  
<li>返回func2（val）</ li>  
<li>除了TypeError：</ Li>  
<li>打印（这是（可能）int：+ str（val）</ li>  
<li>返回func3（val）</ li>  
<li> </ li>  
<li> x = func1（dude）//这是一个字符串：dude x =嘿dude </ li>  
<li> y = func1（4）//这可能是int：4 x = 6 </ li>  
或者您可以使用装饰器，以便更有趣的方式传递函数。  
<ol> def makeasandwich（func）：def sandwich（）：打印（面包）func（）打印（面包）返回三明治（）@makeasandwich def addmeat（）：print（肉）addmeat（）//面包肉面包</ OL>  
<li> def makeasandwich（Func）：</ li>  
<li> def sandwich（）：</ li>  
func（）</ li>  
<li>打印（面包）</ li>  
<li>返回三明治（）</ li>  
<li> @makeasandwich </ li>  
<li> def addmeat（）：</ li>  
<li>印刷（肉）</ li>  
<li> </ li>  
<li> addmeat（）//面包肉面包</ li>  
Python为初学者的一种伟大的语言，但它对更多高级用户也有一些非常有趣的事情。保持学习！  
