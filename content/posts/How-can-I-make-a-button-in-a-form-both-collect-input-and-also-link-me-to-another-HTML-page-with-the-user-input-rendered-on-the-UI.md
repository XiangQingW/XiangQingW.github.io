---

title: 如何将表格中的按钮收集输入，并将我链接到另一个HTML页面，用户输入呈现在UI上？
date: 2022-01-23T22:08:09+08:00

---




## 如何将表格中的按钮收集输入，并将我链接到另一个HTML页面，用户输入呈现在UI上？  
### 回答 1
嗯，理想情况下，提交的表格将带您到一个页面，该页面使用您可以在表单上使用的操作值来显示此用户输入。  
<ol> <form action = take_me_to_next_page> </ ol>  
<li> <form action = take_me_to_next_page> </ li>  
否则，JS要在页面上执行某些内容并禁用提交按钮的默认行为  
### 回答 2
您没有提供非常多的信息继续，但首先要做的就是确保您的JavaScript实际加载，并且它在您的文档完全加载之前不会执行。最简单的方法是通过在正文标签的末尾包括脚本标记。  
接下来，检查JavaScript控制台。在浏览器中打开页面，然后打开开发人员工具。在Windows上的Chrome中，它是Ctrl + Shift + I。如果您包含外部JavaScript文件，请在文件的路径不正确后检查404错误。检查控制台中显示的任何JavaScript错误。把它们拿一个。复制第一个错误的文本，并搜索它，或对我的答案进行评论，我将编辑它来解决错误。 :-)  
### 回答 3
如果将提交按钮放在表单中，然后管理该表单的操作，则提交按钮将带您到该页面并使用它传输任何数据。  
<ol> <form action = yourpage.com / sitepage> <按钮类型=提交>单击</ button> </ form> </ ol>  
<li> <form action = yespage.com / sitepage> </ li>  
<li> <按钮类型=提交>单击</按钮> </ li>  
<li> </ form> </ li>  
如果您只需要一个看起来像提交按钮的链接，请创建一个元素并将样式应用于它。  
<ol> <a href=yourpage.com/sitepage class=button--tyle -red>点击！</a> </ ol>  
<li> <a href=yourpage.com/sitepage class=button--tyle -red>点击！</a> </ li>  
### 回答 4
用jquery.  
：  
<ol> <html> <head> <script src = jquery.js> </ script> <script> $（function（）{$（#lactultContent）.load（b.html）;}）;</ script> </ head> <body> <div id =包括content> </ div> </ body> </ html> </ ol>  
<li> <html> </ li>  
<li> <head> </ li>  
<li> <script src = jQuery.js> </ script> </ li>  
<li> <script> </ li>  
<li> $（function（）{</ li>  
<li> $（#lound附带的content）.load（b.html）;</ Li>  
<li>}）;</ Li>  
<li> </ script> </ li>  
<li> </ head> </ li>  
<li> <body> </ li>  
<li> <div id =包括content> </ div> </ li>  
<li> </ body> </ li>  
<li> </ html> </ li>  
b.html：<p>这是我的包含文件</ p>  
用javascript.  
 如果没有jQuery，以避免必须加载jQuery库，如果您关注最大化您的网站的最小化......  
### 回答 5
*您有语法错误*您在代码中有错误您正在寻找不在页面*您使用的语言不是JavaScript *您使用的是jQuery功能，但从不包括库甚至注意到它是必需的*您在浏览器中禁用了JavaScript *您无法访问属性和ite ...  
### 回答 6
我会添加到我的左边缘，或者在某些情况下，我可能会添加左填充。通过向左侧添加空间，您将内容推向右侧。  
边距为元素的外部添加空间，而填充添加元素内的空间。如果添加左边缘，则将整个div移动到右侧。  
.myclass {位置：相对;边缘：0px 0px 0px 10px}  
.myclass {位置：相对;边缘 - 左：10px}  
如果您在左侧添加填充，则会将Div的内容转移到右侧，但它将留在DIV内。  
.myclass {位置：相对;填充：0px 0px 0px 10px}  
或者  
<ol> .myclass {p </ ol>  
<li> .myclass {p </ li>  
我会添加到我的左边缘，或者在某些情况下，我可能会添加左填充。通过向左侧添加空间，您将内容推向右侧。  
边距为元素的外部添加空间，而填充添加元素内的空间。如果添加左边缘，则将整个div移动到右侧。  
.myclass {位置：相对;边缘：0px 0px 0px 10px}  
.myclass {位置：相对;边缘 - 左：10px}  
如果您在左侧添加填充，则会将Div的内容转移到右侧，但它将留在DIV内。  
.myclass {位置：相对;填充：0px 0px 0px 10px}  
或者  
<ol> .myclass {位置：相对;填充左：10px} </ ol>  
<li> .myclass {位置：相对;填充左：10px} </ li>  
边缘和填充包含在下面说明的CSS框模型中。阅读CSS框模型的简介以了解更多信息。  
### 回答 7
您可以使用这样的标准HTML链接：  
<ol> <a href=link-to-your-page类= mybtn> link </a> </ ol>  
<li> <a href=link-to-your-page类= mybtn> link </a> </ li>  
使用CSS将按钮拟合。您还可以定义按钮的悬停效果。  
例如：  
<ol> a.mybtn {显示：内联块;边缘：0 0.2em;填充：填充：0.5EM 1.2EM;字体大小：1.4EM;字体重量：600;文本装饰：无;文字阴影：0 0.04EM 0.04EM RGBA（0,0,0.0.35）;文字对齐：中心;背景：＃b00;颜色：#fff;过渡：所有0.15s;边框：0.1EM实心＃000;边界半径：0.5em;盒子尺寸：边界盒; a.mybtn：悬停{文本阴影：0 0 2EM RGBA（255,255,255,1）;背景</ ol>  
<li> a.mybtn {</ li>  
<li>显示：内联块; </ Li>  
<li>边际：0 0.2em; </ Li>  
<LI>填充：填充：0.5EM 1.2EM; </ Li>  
<li>字体大小：1.4EM; </ Li>  
<li>字体重量：600; </ Li>  
<li>文本装饰：无; </ Li>  
<li>文字阴影：0 0.04em 0.04em RGBA（0,0,0.0.35）; </ Li>  
<li>文字对齐：中心; </ Li>  
<li>背景：＃b00; </ Li>  
<li>颜色：#fff; </ Li>  
<li>转型：所有0.15s; </ Li>  
<li>边框：0.1EM实心＃000; </ Li>  
<li>边界半径：0.5em; </ Li>  
<li>盒式尺寸：边框盒; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> a.mybtn：悬停{</ li>  
<li>文字阴影：0 0 2EM RGBA（255,255,255,1）; </ Li>  
<li>背景</ li>  
您可以使用这样的标准HTML链接：  
<ol> <a href=link-to-your-page类= mybtn> link </a> </ ol>  
<li> <a href=link-to-your-page类= mybtn> link </a> </ li>  
使用CSS将按钮拟合。您还可以定义按钮的悬停效果。  
例如：  
<ol> a.mybtn {显示：内联块;边缘：0 0.2EM;填充：填充：0.5EM 1.2EM;字体大小：1.4EM;字体重量：600;文本装饰：无;文字阴影：0 0.04EM 0.04EM RGBA（0,0,0.0.35）;文字对齐：中心;背景：＃b00;颜色：#fff;过渡：所有0.15s;边框：0.1EM实心＃000;边界半径：0.5em;盒子尺寸：边界盒; a.mybtn：悬停{文本阴影：0 0 2EM RGBA（255,255,255,1）;背景：＃e00;颜色：#ccc; } </ OL>  
<li> a.mybtn {</ li>  
<li>显示：内联块; </ Li>  
<li>边际：0 0.2em; </ Li>  
<LI>填充：填充：0.5EM 1.2EM; </ Li>  
<li>字体大小：1.4EM; </ Li>  
<li>字体重量：600; </ Li>  
<li>文本装饰：无; </ Li>  
<li>文字阴影：0 0.04em 0.04em RGBA（0,0,0.0.35）; </ Li>  
<li>文字对齐：中心; </ Li>  
<li>背景：＃b00; </ Li>  
<li>颜色：#fff; </ Li>  
<li>转型：所有0.15s; </ Li>  
<li>边框：0.1EM实心＃000; </ Li>  
<li>边界半径：0.5em; </ Li>  
<li>盒式尺寸：边框盒; </ Li>  
<li>} </ li>  
<li> </ li>  
<li> a.mybtn：悬停{</ li>  
<li>文字阴影：0 0 2EM RGBA（255,255,255,1）; </ Li>  
<li>背景：＃e00; </ Li>  
<li>颜色：#ccc; </ Li>  
<li>} </ li>  
我建议使用<ul>和<li>来构建垂直或水平导航栏的链接列表。  
### 回答 8
在最后？如果它最终，它通常不会做任何事情，但如果它是example.com/blog/article-123.html#section-01的东西，它只是链接到ID的该页面上的部分=第01节“。  
英镑标志可以用于JavaScript中的许多东西，所以它取决于。  
### 回答 9
<script>  
$（文件）.ready（function（）{  
$（第一个输入类型的＃id）.change（function（）{  
$（第二输入类型的＃id）.val（$（此）。val（））;  
}）;  
</ script>  
### 回答 10
谢谢你的A2A。  
在四种方式中，您可以将价值从一页传递到另一个页面。  
使用javascript设置cookie  
document.cookie = Username = John Doe;  
对于长篇描述，请阅读以下文章  
JavaScript Cookie.  
在本地存储LocalStorage.setItem（LastName，Smith）中设置值;  
获取本地存储值localstorage.getItem（LastName）;  
删除本地存储值localstorage.removeItem（LastName）;  
在本地存储会话中设置值.SetItem（LastName，Smith）;  
获取本地存储值Sessage.getItem（LastName）;  
删除  
谢谢你的A2A。  
在四种方式中，您可以将价值从一页传递到另一个页面。  
使用javascript设置cookie  
document.cookie = Username = John Doe;  
对于长篇描述，请阅读以下文章  
JavaScript Cookie.  
在本地存储LocalStorage.setItem（LastName，Smith）中设置值;  
获取本地存储值localstorage.getItem（LastName）;  
删除本地存储值localstorage.removeItem（LastName）;  
在本地存储会话中设置值.SetItem（LastName，Smith）;  
获取本地存储值Sessage.getItem（LastName）;  
删除本地存储值会话serage.removeItem（LastName）  
介绍Web SQL数据库  
window.postmessage（）  
### 回答 11
你好呀，  
您可以使用2种方式实现 -   
让我解释你们两种方式。  
以下是内联CSS的示例  
<ol> <！doctype html> <html> <head> </ head> <body> <p>这是第1段-1 </ p> <p>这是第2段-2 </ p> <p style =颜色：红色;>这是第3段</ p> <p>这是第4段</ p> <p>这是第5段-5 </ p> </ body> </ html> </ ol>  
<li> <！doctype html> </ li>  
<li> <html> </ li>  
<li> <head> </ li>  
<li> </ head> </ li>  
<li> <body> </ li>  
<li> <p>这是第1段-1 </ p> </ li>  
<li> <p>这是第2段-2 </ p> </ li>  
<li> <p style =颜色：红色;>这是第3段-3 </ p> </ li>  
<li> <p>这是第4段-4 </ p> </ li>  
<li> <p>这是第5段-5 </ p> </ li>  
<li> </ body> </ li>  
<li> </ html> </ li>  
上面给出了上述代码的输出 -   
2.内部CSS-此CSS在使用中写入<head>标记内  
你好呀，  
您可以使用2种方式实现 -   
让我解释你们两种方式。  
以下是内联CSS的示例  
<ol> <！doctype html> <html> <head> </ head> <body> <p>这是第1段-1 </ p> <p>这是第2段-2 </ p> <p style =颜色：红色;>这是第3段</ p> <p>这是第4段</ p> <p>这是第5段-5 </ p> </ body> </ html> </ ol>  
<li> <！doctype html> </ li>  
<li> <html> </ li>  
<li> <head> </ li>  
<li> </ head> </ li>  
<li> <body> </ li>  
<li> <p>这是第1段-1 </ p> </ li>  
<li> <p>这是第2段-2 </ p> </ li>  
<li> <p style =颜色：红色;>这是第3段-3 </ p> </ li>  
<li> <p>这是第4段-4 </ p> </ li>  
<li> <p>这是第5段-5 </ p> </ li>  
<li> </ body> </ li>  
<li> </ html> </ li>  
上面给出了上述代码的输出 -   
2.内部CSS-此CSS使用<style>标记写入<head>标记内。在这里，我们还有2个选项 - 类和ID标识符。  
下面我将使用ID标识符显示内部CSS  
<ol> <！doctype html> <html> <head> <style> #paintred {color：红色; </ style> </ head> <body> <p>这是第1段-1 </ p> <p>这是第2段</ p> <p>这是第3段-3 </ p> <p id =绘制>这是第4段-4 </ p> <p>这是第5段-5 </ p> </ body> </ html> </ ol>  
<li> <！doctype html> </ li>  
<li> <html> </ li>  
<li> <head> </ li>  
<li> <style> </ li>  
<li> #paintred {</ li>  
<li>颜色：红色; </ Li>  
<li>} </ li>  
<li> </ style> </ li>  
<li> </ head> </ li>  
<li> <body> </ li>  
<li> <p>这是第1段-1 </ p> </ li>  
<li> <p>这是第2段-2 </ p> </ li>  
<li> <p>这是第3段-3 </ p> </ li>  
<li> <p id = paintred>这是第4段 -  4 </ p> </ li>  
<li> <p>这是第5段-5 </ p> </ li>  
<li> </ body> </ li>  
<li> </ html> </ li>  
上面给出了上述代码的输出 -   
在这里，“绘制”是ID，它在<style>标记中使用之前使用'＃'符号。  
我们已经给了ID到第4个<p>标签，所以第4段具有红色。  
现在，到了“类”标识符。与'ID'标识符不同，而是在这里我们使用关键字类代替ID和CSS，我们使用“。”（点）符号代替＃'（哈希）符号。  
3.外部CSS-此CSS在单独的CSS文件中写入HMTL文档中的导入。此文件使用.css扩展名保存，并链接为<link rel = styleSheet href = html文档的<head>标记中的css.css>的路径。  
这些CSS彼此具有不同的优先级。现在它的作业来了解哪种类型的CSS具有更高/较低的优先级。  
我希望它有所帮助。  
快乐的学习。  
