---

title: JSON对象和JSON字符串之间有什么区别？
date: 2022-01-23T22:08:29+08:00

---




## JSON对象和JSON字符串之间有什么区别？  
### 回答 1
JSON对象：  
<ol> {key1：value1，key2：[1，true，3.14，值]，key32：{}，key33：[]}，key4：false，full：255} </ ol>  
<li> {</ li>  
<li> key1：value1，</ li>  
<li> key2：[1，true，3.14，值]，</ li>  
<li> key3：{</ li>  
<li> key31：null，</ li>  
<li> key32：{}，</ li>  
<li> key33：[] </ li>  
<li>}，</ li>  
<li> key4：false，</ li>  
<li> key5：255 </ li>  
<li>} </ li>  
json字符串：  
<ol> heck yeah，我甚至用于对象！</ OL>  
<li> heck yeah，我甚至用于对象！</ Li>  
### 回答 2
JSON对象  
有时，在进行项目时，两个概念会混淆，特别是在使用Spring MVC时，背景@RequestBody接受JSON格式的字符串，该字符串必须是STRING.LET以JSON对象开头，从而以对象的概念开头，可以使用Object属性调用。例如：  
<ol> var person = {name：tom，性别：男性，年龄：24} / / json object console.log（person.name）; //在控制台警报中输出tom（typeof（personof））; //对象</ OL>  
<li> var person = {名称：汤姆，性别：男性，年龄：24} / / json对象</ li>  
<li> console.log（person.name）; //在控制台中输出tom </ li>  
<li>警报（类型（人））; //对象</ li>  
以上是JSON对象。第三行代码是看到一个人的类型，它是对象类型。  
JSON对象  
有时，在进行项目时，两个概念会混淆，特别是在使用Spring MVC时，背景@RequestBody接受JSON格式的字符串，该字符串必须是STRING.LET以JSON对象开头，从而以对象的概念开头，可以使用Object属性调用。例如：  
<ol> var person = {name：tom，性别：男性，年龄：24} / / json object console.log（person.name）; //在控制台警报中输出tom（typeof（personof））; //对象</ OL>  
<li> var person = {名称：汤姆，性别：男性，年龄：24} / / json对象</ li>  
<li> console.log（person.name）; //在控制台中输出tom </ li>  
<li>警报（类型（人））; //对象</ li>  
以上是JSON对象。第三行代码是看到一个人的类型，它是对象类型。  
json字符串  
跨越我们经常说的javascript中的字符串是单引号括起来的。那么JSON字符串的概念是什么？  
<ol> var b ='{名称：2323，性别：afasdf，年龄：6262}'; // json string console.log（b）; // {name：2323，性别：afasdf，年龄：6262}警报（ Typeof（b））; //字符串</ ol>  
<li> var b ='{name：2323，性别：afasdf，年龄：6262}'; // json string </ li>  
<li> console.log（b）; // {name：2323，性别：afasdf，年龄：6262} </ li>  
<li>警报（类型（b））; //字符串</ li>  
上面是b是一个字符串，也是一个json字符串，原因被称为json字符串，因为字符串的格式为json格式，所以称为json字符串，第三行代码也匹配类型字符串。  
想了解JSON字符串和JSON对象转换吗？请检查这篇文章。  
### 回答 3
尽可能多地指出，JSON是一种简单的标准化格式，用于交换数据。  
但XML也是如此，我相信XML预测JSON。那么为什么JSON存在？答案是XML由委员会设计。或者也许更准确地，XML由委员会变异。 XML开始作为一种相当简单的格式，但随后各种专家都添加了功能，如名称空间，引用，dtds等。每个增加的功能都有一个使用 - 但结果是一个难以解析的混乱。  
另一方面，JSON开始简单，保持简单。它抵抗了蠕动特色。结果是一种数据交换格式，易于解析和易于创建。 JSON不做XML所做的一切。例如，JSON没有注释，并且大块的自由形式文本难以在JSON中表示。所以JSON永远不会替换XML，但JSON确实做得很好。  
### 回答 4
解析通常意味着解释。  
JSON是一个格式规范，如其他人所述。  
解析json意味着用目前使用的语言解释数据。  
JSON通常首先读取为字符串 - 我们通常称之为JSON字符串（遵循JSON规范的字符串）。  
当我们解析JSON时，它意味着我们通过遵循规范将字符串转换为JSON对象，我们可以随后以任何方式使用我们想要的方式。  
例如在JavaScript中  
var jsonstr ='{name：peter}';  
var obj = json.parse（jsonstr）;  
console.log（obj.name）; //打印彼得  
C  
解析通常意味着解释。  
JSON是一个格式规范，如其他人所述。  
解析json意味着用目前使用的语言解释数据。  
JSON通常首先读取为字符串 - 我们通常称之为JSON字符串（遵循JSON规范的字符串）。  
当我们解析JSON时，它意味着我们通过遵循规范将字符串转换为JSON对象，我们可以随后以任何方式使用我们想要的方式。  
例如在JavaScript中  
var jsonstr ='{name：peter}';  
var obj = json.parse（jsonstr）;  
console.log（obj.name）; //打印彼得  
console.log（jsonstr.name）; //打印未定义  
在解析之前，它只是一个常规字符串 - 你无法真正访问里面编码的数据。  
解析后，它成为一个JavaScript对象，其中您可以访问内部各种数据。  
### 回答 5
JSON数组VS JSON对象可以简单地称为列表VS键值对。  
JSON数组在收集订单值[]时，JSON对象是无序密钥的集合，值对沃特括号{}。  
JSON数组示例  
<ol> [{城市：kophal，州：Null，国家：印度尼西亚}，{城市：Wootton，州：英格兰，国家：英国}，{城市：Ust'-Kachka，州：Null，国家：俄罗斯}， {城市：州：州：NULL，国家：阿根廷}，{城市：NovoPavlovsk，州：Null，国家：俄罗斯}，{城市：Melaka，State：Melaka </ OL>  
<li> [{</ li>  
<li>城市：kophal，</ li>  
<li>状态：null，</ li>  
<li>国家：印度尼西亚</ li>  
<Li>城市：Wootton，</ Li>  
<li>状态：英格兰，</ li>  
<li>国家：英国</ li>  
<li>城市：ust'-kachka，</ li>  
<li>国家：俄罗斯</ li>  
<li>城市：Viedma，</ Li>  
<li>国家：阿根廷</ li>  
<li>城市：NovoPavlovsk，</ Li>  
<li>状态：null，</ li>  
<li>国家：俄罗斯</ li>  
<li>}，{</ li>  
<Li>城市：Melaka，</ Li>  
<li>状态：Melaka </ Li>  
JSON数组VS JSON对象可以简单地称为列表VS键值对。  
JSON数组在收集订单值[]时，JSON对象是无序密钥的集合，值对沃特括号{}。  
JSON数组示例  
<ol> [{城市：kophal，州：Null，国家：印度尼西亚}，{城市：Wootton，州：英格兰，国家：英国}，{城市：Ust'-Kachka，州：Null，国家：俄罗斯}， {城市：州：州：Null，国家：阿根廷}，{城市：NovoPavlovsk，州：Null，国家：俄罗斯}，{城市：Melaka，State：Melaka，国家：马来西亚}] </ OL>  
<li> [{</ li>  
<li>城市：kophal，</ li>  
<li>状态：null，</ li>  
<li>国家：印度尼西亚</ li>  
<Li>城市：Wootton，</ Li>  
<li>状态：英格兰，</ li>  
<li>国家：英国</ li>  
<li>城市：ust'-kachka，</ li>  
<li>国家：俄罗斯</ li>  
<li>城市：Viedma，</ Li>  
<li>国家：阿根廷</ li>  
<li>城市：NovoPavlovsk，</ Li>  
<li>状态：null，</ li>  
<li>国家：俄罗斯</ li>  
<li>}，{</ li>  
<Li>城市：Melaka，</ Li>  
<li>状态：melaka，</ li>  
<li>国家：马来西亚</ li>  
<li>}] </ li>  
JSON对象的示例  
<ol> {城市：[{城市：kopral，州：Null，国家：印度尼西亚}，{城市：Wootton，州：英格兰，国家/地区：英国}，{城市：Ust'-Kachka，州：Null，Country：俄罗斯}，{城市：Viedma，州：Null，国家：阿根廷}，{城市：NovoPavlovsk，州：Null，国家/地区：俄罗斯}，{城市：Melaka，State：Melaka，国家：马来西亚}，} </ OL >  
<li> {</ li>  
<li>城市：[{</ li>  
<li>城市：kophal，</ li>  
<li>状态：null，</ li>  
<li>国家：印度尼西亚</ li>  
<Li>城市：Wootton，</ Li>  
<li>状态：英格兰，</ li>  
<li>国家：英国</ li>  
<li>城市：ust'-kachka，</ li>  
<li>国家：俄罗斯</ li>  
<li>城市：Viedma，</ Li>  
<li>国家：阿根廷</ li>  
<li>城市：NovoPavlovsk，</ Li>  
<li>状态：null，</ li>  
<li>国家：俄罗斯</ li>  
<li>}，{</ li>  
<Li>城市：Melaka，</ Li>  
<li>状态：melaka，</ li>  
<li>国家：马来西亚</ li>  
<li>}]，</ li>  
<li>} </ li>  
### 回答 6
使用json.parse（jsonstr）;  
这应该返回您可以使用的JSON对象  
例如：  
var str = {key：value，key2：value2}; var jsonobj = json.parse（str）;  
这不会在版本8之前工作。  
### 回答 7
看着您的个人资料，似乎您在Java上询问了这个问题，因为您似乎专注于Android应用程序。  
最简单的方式是使用GSON，Google库用于在Java中处理JSON。它非常简单，在下面的网站上提供了很多示例。  
如果要使用内置Java库，则使用JAXB是一个更复杂的。我不确定在开发Android平台时建议使用此方法。  
Google / Gson.  
使用JAX-R与JAXB  
### 回答 8
序列化是转换a的过程  
如果我们是拆分毛发，那么是的，JSON是序列化的。 JSON是数据的文本表示。 JSON不是JavaScript。它是一种格式，其语义与JavaScript对象（毕竟，它是在JavaScript对象之后建模的）。  
反序列化是将数据存储格式转换为结构编程语言/运行时理解的结构的过程。这是一种无关的方法，这意味着它几乎可以在任何语言中完成。 JavaScript可以用JSON.parse方法执行此操作，但它也可以用其他语言完成。  
序列化是将数据结构转换为可以存储的格式的过程。同样，JSON是用于存储数据的一种格式。 XML，CSV和其他类型的格式也存在。  
不要被语义混淆。在编写JavaScript时，对象看起来几乎与JSON相同，但它们明显不同。 JavaScript对象具有原型，它们可以具有方法，getter / setter等。  
它被称为JSON（JavaScript对象符号）的事实是不幸的，因为它将格式与单个语言紧密相关联，即使它比这更广泛。 XML遭受了类似的命名（但更准确）挑战...可扩展标记语言。没有任何关于该名称的名称可以清楚它是一种数据格式。  
### 回答 9
JSON（JavaScript对象表示法）是一种开放标准格式，它使用易于可读文本来传输由键值对组成的数据对象。它是用于异步浏览器/服务器通信的最常用的数据格式，在很大程度上替换XML。  
JSON都更紧凑，并且（在我的观点中）更可读 - 在传输中，它可以简单地更快，因为传输了较少的数据。  
JSON是一种跨语言数据格式。  
JSON建于两个结构：  
这是摘要来自：哪一个是更好的XML或JSON？  
1.对于服务器和浏览器之间的数据传递，JSON更好的选择。 2.为了在服务器端的配置文件中存储信息，XML更好。 3.在浏览器方面：解析JSON的速度和轻松，以及从JavaScript对象中易于简单的数据检索;让JSON是一个更好的选择。 4.服务器端：查询数据和格式更改;使XML更好的选择。  
希望这可以帮助。  
### 回答 10
看起来我在这里无法得到任何答案。幸运的是，我在Twitter线程中询问了类似的问题，我从Twitter.com/andrewmccright获得了一个美好的答案。我在这里发布了它，以便在这个问题之后的别人。  
我的问题是：  
我很困惑：Java的JSON-B＆JSON-P API之间有什么区别？他们没有重叠功能吗？谢谢  
和他的答案：  
JSONB是一个类似于Jackson的直接对象到JSON映射。 JSONP通过像JSONObject / JSONARRAY / etc等API地图地图。 jsonp是更多的手动。 HTH。  
他进一步提供了一个非常有关JSON-P的文章的链接  
看起来我在这里无法得到任何答案。幸运的是，我在Twitter线程中询问了类似的问题，我从Twitter.com/andrewmccright获得了一个美好的答案。我在这里发布了它，以便在这个问题之后的别人。  
我的问题是：  
我很困惑：Java的JSON-B＆JSON-P API之间有什么区别？他们没有重叠功能吗？谢谢  
和他的答案：  
JSONB是一个类似于Jackson的直接对象到JSON映射。 JSONP通过像JSONObject / JSONARRAY / etc等API地图地图。 jsonp是更多的手动。 HTH。  
他进一步提供了一个非常链接，其中包含关于JSON-P和JOSH-B API的文章。我会把它作为我的枕头作为参考。  
JSON-B：用于JSON绑定的Java API  -  Dzone集成  
希望这可以帮助。  
### 回答 11
JSON是一种特定于域的语言（DSL），数据格式独立于JavaScript，它具有自己的MIME类型i.e.应用程序/ JSON。  
{名称：Web技术，网站：Web技术专家笔记}  
JSONP是填充的JSON。响应是JSON数据，但使用函数调用跳据。  
FunctionCallexample（{name：web技术，网站：web技术专家笔记}）;  
JSONP是一种简单的方法，可以在从客户端发送来自不同域的JSON响应时克服浏览器限制。  
JSON（JavaScript对象符号）是应用程序之间的交通数据的便捷方式  
JSON是一种特定于域的语言（DSL），数据格式独立于JavaScript，它具有自己的MIME类型i.e.应用程序/ JSON。  
{名称：Web技术，网站：Web技术专家笔记}  
JSONP是填充的JSON。响应是JSON数据，但使用函数调用跳据。  
FunctionCallexample（{name：web技术，网站：web技术专家笔记}）;  
JSONP是一种简单的方法，可以在从客户端发送来自不同域的JSON响应时克服浏览器限制。  
JSON（JavaScript对象表示法）是在应用程序之间传输数据的便捷方式，尤其是当目标是JavaScript应用程序时。  
jQuery具有使Ajax / Httpd调用从脚本到服务器的函数非常容易，$ .getjson（）是一个很好的速写功能，用于在JSON中获取服务器响应。  
但是，如果将Ajax调用中的页面处于来自服务器的不同域中，则此简单方法失败。相同的原始策略禁止某些浏览器中的这些跨域呼叫作为安全措施。  
应在您的应用程序中仔细考虑允许跨域请求的安全影响，但如果您确实想要允许它们，那么您需要一种克服浏览器限制的方法。  
JSONP（带填充的JSON）在所有浏览器中都可以实现这一目标。  
JSONP将JSON响应归结为JavaScript函数，并将其作为脚本发送回浏览器。脚本不受同样的原始策略，并且在加载到客户端时，函数就像它包含的JSON对象一样。  
想要查询更多的信息 -  
JSON与JSONP教程  
### 回答 12
JavaScript和Json有时可以真正令人困惑，这就是为什么我写这一点，所以它回答了所有问题。  
JSON代表JavaScript对象表示法。它基本上是一种文本格式，可以轻松共享客户端和服务器等设备之间的数据。它的起源是基于JavaScript对象如何在这种意义上工作，它与之相关/靠近但不是完全JavaScript对象。无论它从JavaScript起源，它都广泛使用了许多语言，如C，Ruby，Python，PHP只是提到了一些。由于转换为数据结构的大小和容易，因此它是XML等其他格式的替代方案。  
使用JSON的一个非常好的优势是可以读取的容易。  
<ol> {name：mohammad alqanneh，作业：开发人员} </ ol>  
<li> {</ li>  
<li>名称：Mohammad Alqanneh，</ Li>  
<li>工作：开发人员</ li>  
<li>} </ li>  
考虑上面的片段。我创建了一个带有一些键值对的JSON对象。键位于左侧（姓名，语言和爱好），而键的值位于右侧。这很容易被javascript和读它的人被理解为对象。  
JSON的另一个好处是能够将值或数据传递到JavaScript对象中。这可以使用JavaScript命令简单地完成，如下所示。  
<ol> {name：mohammad alqanneh，作业：developer} var userinfo = json.parse（数据）; </ OL>  
<li> {</ li>  
<li>名称：Mohammad Alqanneh，</ Li>  
<li>工作：开发人员</ li>  
<li>} </ li>  
<li> </ li>  
<li> var userinfo = json.parse（数据）; </ Li>  
使用该单行命令，可以从对象数据访问任何内容。所以，假设你要获得名称值，你所做的就是简单地输入：  
userinfo.name; //使用dot表示法。  
UserInfo [name] //使用括号表示法  
另一个好的优点是它比XML更精简。当您尝试使用XML运行相同的命令或脚本时，您会观察到传递XML可能会耗时，而与JSON一起时，它会更快。  
让我们来看看JSON字符串是如何写的。  
<ol> {firstname：mohammad，lastname：alqanneh} </ ol>  
<li> {</ li>  
<li>名字：穆罕默德，</ li>  
<li> lastname：alqanneh </ li>  
<li>} </ li>  
非常好看钥匙。你会观察他们是用引号编写的。键也可以是任何有效的字符串。 JSON值只能是六个数据类型（字符串，数字，对象，阵列，布尔，NULL）之一。另一方面的JavaScript值可以是任何有效的JavaScript结构。  
<ol> {firstname：mohammad，lastname：alqanneh} </ ol>  
<li> {</ li>  
<li>名字：穆罕默德，</ li>  
<li> lastname：alqanneh </ li>  
<li>} </ li>  
在上面的代码段中，您会注意到键不会用引号包裹。这是JavaScript对象的典型示例。 JavaScript对象值可以是包括函数的任何数据类型（您不能与JSON执行。查看下面的代码段显示有效的JavaScript对象。  
<ol> var info = {firstname：mohammad，lastname：alqanneh，getName：function（）{Alert（this.firstname）; }}; </ OL>  
<li> var info = {</ li>  
<li>名字：穆罕默德，</ li>  
<li> lastname：alqanneh，</ li>  
<li> getName：function（）{</ li>  
<li>警报（this.firstname）; </ Li>  
<li>} </ li>  
<li>}; </ Li>  
与JavaScript对象不同，必须将JSON对象作为字符串送入变量，然后解析为JavaScript。在解析时，jquery等框架可以非常有用。  
<ol> var data = {firstname：mohammad，lastname：alqanneh}; var userinfo = json.parse（数据）; </ OL>  
<li> var data = {</ li>  
<li>名字：穆罕默德，</ li>  
<li> lastname：alqanneh </ li>  
<li>}; </ Li>  
<li> </ li>  
<li> var userinfo = json.parse（数据）; </ Li>  
您可以使用的一些工具来验证您的JSON代码，其中一些产品如下：  
