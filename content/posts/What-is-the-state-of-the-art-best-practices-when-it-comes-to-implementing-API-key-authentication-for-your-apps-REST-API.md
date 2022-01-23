---

title: 在为应用程序REST API实现API密钥身份验证时，最先进的艺术/最佳实践是什么？
date: 2022-01-23T22:08:02+08:00

---




## 在为应用程序REST API实现API密钥身份验证时，最先进的艺术/最佳实践是什么？  
### 回答 1
嗯，一般这意味着JWT，通常通过SHA512等东西签名。您可能会或可能不在意也可以加密令牌，但通常不需要。这些令牌通常被设计为在短时间内到期（我经常见过2分钟）。如果密钥由客户持有，则到期将更长，通常（在该案例中几个小时）。当您拥有正在进行密钥生成的API网关时，使用这种模型（然后在网关和客户端之间使用一些其他会话管理协议）。通常，这完全是一个或另一种类型的OAuth2流动，以建立客户真实性等。  
显然，这里的主要考虑因素是确保用于签署令牌的密钥仍然是安全的。  
### 回答 2
假设您的意思是使用API键签署请求，我将从头顶列出以下内容：  
### 回答 3
RESTFUL API  - 也称为RESTful Web服务或R  
图像来源： - 谷歌  
RESTful API是用于应用程序接口的架构风格，它使用HTTP请求访问和使用数据。该数据可用于获取，放置，邮寄和删除数据类型，这是指读取，更新，创建和删除有关资源的操作。  
网站的API是允许两个软件程序彼此通信的代码。 API为开发人员写出了从操作系统或其他应用程序请求服务的程序的正确方法。  
RESTful API  - 也称为RESTful Web服务或REST API  - 基于代表性状态传输，这是一种架构风格和经常用于Web服务开发的通信方法。  
REST技术通常优于其他类似技术。这往往是这种情况，因为休息使用较少的带宽，使其更适合高效的互联网使用。 RESTFUL API也可以通过编程语言（如JavaScript或Python）构建。  
六个休息API规则  
为了完全受益于REST提供的功能，API必须遵循六个要求。 （嗯，技术上五是必需的，一个是可选的。）每个要求为快速和多功能API奠定了基础。  
1.客户端 - 服务器分隔  
在REST架构下，客户端和服务器只能以单向交互：客户端向服务器发送请求，然后服务器将响应发送回客户端。服务器无法使请求，客户端无法响应 - 客户端启动所有交互。  
通过简化客户端和服务器之间的通信，RESTful API保持两个方便独立的。这样，在不担心影响任何其他服务器的情况下，客户端软件可以增长它们的构建，并且可以在不无意中影响客户端的情况下修改服务器内容。  
2.统一界面  
本指南表示所有请求和所有响应都必须遵循公共协议或格式化其消息的方式。应用程序和服务器用各种不同的语言编写，没有中间人在没有中间人一起工作的巨大工作。统一界面是任何与任何REST API通信的客户端的通用语言。  
没有标准化的通信，软件之间的翻译请求和响应将是一个完全杂乱。轻微的差异将导致信息困扰和丢失，并且应用程序必须在API更新时更新他们的请求流程。统一的界面消除了这种可能性。  
对于大多数REST API，这种通用语言是HTTP或超文本传输​​协议。 HTTP没有专门为休息而创建。相反，休息采用此通信协议作为使用它的应用程序的标准。  
要使用HTTP与REST API，客户端以特定格式发送可能看起来熟悉的请求。例如，对视频数据的YouTube API的请求如下所示：  
阅读更多： - 为您的移动应用程序开发选择第三方API的10个提示  
### 回答 4
第二个是模型方法，也称为规范方法，NewsData.io新闻API是一个例子，它从规范和/或开始  
RESTful API设计的方法可能有所不同，但有五个基本的API设计元素可以帮助指导工具选择难题并解决RESTful API设计问题。  
有两个主要的途径来设计RESTful API。  
一个是开放的过程方法，这是最常见的。此方法侧重于支持API设计过程的步骤和工具，几乎没有或没有对要生成的API的性质的约束。  
第二种是模型方法，也称为规范方法，NewsData.io新闻API是一个示例，它以RESTful API的规范和/或模型开头，并支持该模型的调整RESTFUL API。每个项目特定的界面。随着蜜蜂变得越来越普遍，这种策略正在获得地面，但并非没有其并发症的份额。  
开放的过程方法  
将软件架构师创建的统一建模语言变换为特定API，以及大多数交互式开发环境（如NetBeans和Eclipse），具有促进所谓的开放过程转换的工具。  
这些工具假设API的基本性质由组件之间的关系定义，并将这些关系转换为实际API是相当机械的，特别是如果它是单个API或有限使用应用程序中的一组密切相关的API。 。  
模型方法  
基于模型的方法的目标是为所有RESTful API创建最佳实践结构，有时即使是API被改进到特定功能的API，也是关于NewsData.io新闻API的特定功能从网上获取新闻数据。  
此方法适用标准方法来执行不同位置的相同操作，从而降低开发人员的混乱和错误，并更容易监视安全性和合规性。  
### 回答 5
一起捆绑在一起，dropwizrd捆绑码头/ jersty / jackson帮助您编写基于JSON的REST服务器，Spring Rest为您提供了弹簧解决方案  
您需要为此编写一些代码  
送一点捆绑在一起，Dropwizrd捆绑码头/杰克逊可以帮助您编写基于JSON的REST服务器，春台休息给您Spring解决方案。  
爱JavaScript？  
然后，您可以使用Node和Express使用高级REST客户端。这几乎是琐碎的跑步。  
喜欢节点/快速解决方案编程风格，但讨厌javascript？然后尝试Java Spark库，它使用Java 8 Lambda函数来做同样的事情。  
对于教程，使用Jersey与Java（JAX-RS）休息 - 教程看起来不错  
### 回答 6
常用方法是：  
最好的方法是使用OAuth。  
这里可以找到更多信息：3解释的API身份验证的常用方法|北欧API |  
### 回答 7
关注的分离是软件开发中最古老的设计原则之一。 Djikstra于1974年创造了这个短语，即使那么，在介绍这篇文章中，表示这个想法是如此之旧，有时它似乎忘了。  
论科学思想的作用（EWD447）  
介绍API层是实现和强制关注的良好方法（以保持诚实的感觉强制执行）。通过人们普遍地呼叫REST API，即HTTP（见下文），是一种方法，是一种方法。在基于Web的应用程序的背景下，这是一个特别明显和方便的方法，无论如何将使用HTTP。有很多工具可以帮助你这样做，所以这对它的另一票。  
顺便说一下，我建议避免使用只需为每个数据库表中的一个http / json端点生成一堆http / json端点的静止生成工具来避免显而易见但不明智的策略。只有这样一个人不会给你买得很多，可以导致一个设计不良的应用程序，你会把你的发芽撕下来。  
如果您的编程技巧或自律是足够成熟的，以抵制将其用作拐杖使用它的诱惑，那么使用这种休息API发电工具可以是JumpStart开发的好方法。但是你的意图应该是远离那些简单的CRUD电话。诀窍是找到自然分界线，提示点，在客户端上应该发生在哪个逻辑之间，并且应该在服务器上发生。  
注意：HTTP / JSON自身不是一个REST API。实际上，REST API并不一定需要使用HTTP或JSON。看到我对此问题的回答，下面是：  
Steven J Owenss回答软件工程：什么是REST API，以及如何熟悉它？  
### 回答 8
API是两种类型。一个是肥皂，其他是休息。  
REST API比SOAP高得多。它也支持JSON格式。  
来测试点，  
那是所有人。  
### 回答 9
不要认为任何一个完美的语言或框架只是根据您的用例来折衷。  
大多数Web框架都旨在为人类消费提供给浏览器的内容，这可能意味着在建立RESPIS时它们有粗糙的边缘。通常，状态200（一切正常）没有问题，但是404页或错误页面的内容通常是如此粗略的边缘，该框架服务于HTML而不是JSON / XML，并使难以改变该行为。  
要注意的一个项目是WSGIService，编写在Python  -  https://github.com/pneff/wsgiservice  - 符合Pythons WSGI规范，旨在使其轻松创建宁静的服务。  
### 回答 10
成功率在API中是可比的，因为它也不是  
不应该为每个应用程序重新调整警报。  
您需要监视每个API的三个重要标志：成功率，延迟和QPS。  
1.成功率（SR）是监控故障所需的指标。  
成功率在API中是可比的，因为它标准化QPS。  
警报卷会随着QP而随时间变化。您的成功率应保持稳定。  
请记住为您的API设置期望并记录SLA。大多数API应具有3-九（99.9％）或4-九（99.99％）的SLA。 UPI的上游客户应该知道他们的SLA不能高于您的SLA，除非他们有一个倒退。  
衡量成功率的最佳方法是出口成功和失败计数。使用此公式：  
<OL>成功=成功/（成功+失败）</ OL>  
<li> success_rate =成功/（成功+失败）</ li>  
我更喜欢这个公式与成功/ QP，因为这个公式永远不会超过100％。如果您的监控系统在导出为您的指标的时间戳出口时，您可能会最终获得成功> QP，在这种情况下，您的成功率将超过100％。  
三个高级提示：  
2.延迟：使用它来捕获坏代码，坏主机和坏的下游依赖项。  
延迟可以总结每个主机的行为以及下游主机的行为方式。  
坏代码将增加所有主机的延迟。坏主机将增加群集的最大延迟。糟糕的下游依赖项，如数据库，导致群集中的一些服务器行动。  
监控的最佳指标是多用途，可帮助您避免心理过载。  
您服务的延迟使用您需要调整的两个聚合计算：  
每个服务器将在一段时间内聚合请求的延迟。然后，您的监控系统将将每个服务器指标汇总为群集的摘要统计信息。  
我建议每台服务器监控四个统计信息：P50，P90，P99，P999。当您将这些从群集中的所有服务器聚合时，请考虑您可以容忍的服务器数量处于恶劣状态。例如，如果您有100个服务器群集，您可以容忍10个坏，请使用p90聚合它们。如果您不能拥有单个行为不当使用。  
延迟仪表板和警报频繁测量服务舰队中所有主机的所有延迟的平均值或中位数（P50）。这些汇总统计数据都不能可靠地捕获不良主机或下游依赖项。  
3.每秒查询（QPS）：意外的QPS滴剂和尖峰是事件的领先指标。  
始终衡量您的QPS。  
QPS是您需要与其他工程师进行通信的最重要的指标之一。你的用例是多少QP？我的申请处理多少钱？  
QP滴滴和增加通常由其他系统引起。但是你需要意识到下降，因为如果您的服务不可用，可能会出现故障。 QPS增加可能会过载您的服务或其依赖项。  
需要根据其QPS构建和缩放应用程序。  
不要衡量每分钟的查询，每小时或每十秒钟：仅每秒。 QPS是一个有用的指标，可以跨服务进行比较。如果您的服务未按每秒不到1个请求，则会汇总，然后标准化为秒。  
在QPS上提醒的最佳方法是将其与历史数据进行比较。在过去，我已经监控了日常生活和一周时间的测量以捕获事件。  
在跨多个API和服务时，标准化QPS将帮助您维护您的理智。  
首次发表于此：  
### 回答 11
最常用的REST API身份验证方法如下  
基本：使用此方法，发件人将用户名置于请求标题中。用户名和密码使用Base64编码，它是将用户名和密码转换为一组64个字符以确保安全传输的编码技术以确保安全传输。这方法不需要cookie，会话ID，登录页面和其他特殊解决方案，并且因为它使用HTTP标题本身，不需要握手或其他复响应系统。该请求标题中的基本验证的示例：  
授权：Basic BG9Sonnly3vyzq ==  
承载：承载者身份验证（也称为令牌认证）是一个HTTP身份验证方案，它涉及称为承载令牌的安全令牌。名称承载身份验证可以理解为访问该令牌的承载。持卡令牌允许访问某个资源或访问某个资源URL和很可能是一个密码字符串，通常由服务器响应于登录请求而生成。当客户端必须在对受保护资源的请求时在授权标题中发送此令牌：  
授权：承载<令牌>  
与基本身份验证类似，只能使用HTTPS（SSL）。被创建有点修复了HTTP基本身份验证的早期认证问题和其他这样的系统。此方法，唯一生成的值被分配给每个第一次用户，表示已知道用户。当用户尝试重新开始时 - 输入系统，它们的唯一密钥（有时由其硬件组合和IP数据生成，以及所知道的服务器随机生成的其他时间）用于证明它们与之前的用户相同。在查询字符串中作为URL的一部分，这使得能够更容易发现不得访问它的人。请勿在查询字符串参数中放置任何API密钥或敏感信息！更好的选择是PU授权标题中的API键。事实上，这是拟议的标准：授权：apikey 1234567890abcdef.outh（2.0）：此规格的先前版本，OAuth 1.0和1.0a，比OAuth 2.0更复杂。最大最新版本的变更是，使用键控哈希签署每个调用不再需要。OAuth的最常见实现使用这些令牌中的一个或两个：  
访问令牌：发送像API键，它允许应用程序访问a  
用户的数据;可选地，访问令牌可以expired.refresh令牌：可选择的OAuth流量的一部分，刷新令牌检索a  
新访问如果它们已过期.oauth2组合身份验证和  
授权允许更复杂的范围和有效性控制.oauth 2.0是识别个人用户帐户并授予适当的权限的最佳选择。此方法，用户登录系统。然后系统将要求身份验证，通常以a的形式请求身份验证。令牌。然后，用户将将此请求转发给身份验证服务器，该服务器将拒绝或允许此身份验证。从此处提供令牌，然后向用户提供令牌，然后向请求者提供令牌。然后可以随时检查令牌。然后可以随时检查令牌。然后可以随时检查令牌独立于用户由请求者进行验证，可以随着时间的推移使用严格限制的范围和validity .oauth 2.0流行流程：  
流程是API客户端执行以从授权服务器获取访问令牌的情况.oauth 2.0提供适合不同类型API客户端的多个流行流：  
●授权码 - 最常见的流量，主要用于服务器端和移动Web应用程序。本次流类似于用户使用他们的Facebook或Google帐户登录Web应用程序的流程。●隐式 - 此流程要求客户端检索直接访问令牌。在用户凭据无法存储在客户端代码中时，它很有用，因为它们可以通过第三方轻松访问.it适用于不包含任何服务器组件的Web，桌面和移动应用程序。●资源所有者密码 - 需要使用用户名和密码登录。  