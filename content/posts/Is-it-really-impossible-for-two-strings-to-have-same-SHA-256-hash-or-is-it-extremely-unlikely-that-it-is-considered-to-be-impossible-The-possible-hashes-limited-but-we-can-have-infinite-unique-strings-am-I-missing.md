---

title: 两个字符串真的不可能拥有同样的SHA-256哈希，或者它是不太可能被认为是不可能的吗？可能的哈希有限公司，但我们可以拥有无限的独特字符串，我错过了什么？
date: 2022-01-23T22:08:12+08:00

---




## 两个字符串真的不可能拥有同样的SHA-256哈希，或者它是不太可能被认为是不可能的吗？可能的哈希有限公司，但我们可以拥有无限的独特字符串，我错过了什么？  
### 回答 1
哈希可能是如何逆转的？有证据吗？  
写入程序以反转任何散列函数是琐碎的。任何初学者程序员都可以编写该代码，并且该代码证明它可以完成。如果你困惑，你是对人们困惑的，为什么人们一直告诉你，他们是不可能的，他们是错误的（或者更准确，你可能误解了他们的观点）。  
哈希函数得到他们的加密力量不是不可能颠倒的，而是来自......  
### 回答 2
它当然不是不可能的。但是它非常不可能。  
由生日悖论，如果我们收集21282128哈希，我们在该集合中的两个散列之间有大约50％的碰撞。  
让我们说比特币网络每秒拉动1.7亿立陶宛。它接近这一点，这种选择使数学变得更简单。  
1.7亿特拉什人是1.7×10201.7×1020。同时，2128≈3.4×10382128≈3.4×1038。  
这意味着，如果我们在任务上设置了整个比特币网络，那么它将需要2×10182×1018秒才能找到碰撞。  
那是多久了？ theres近似  
它当然不是不可能的。但是它非常不可能。  
由生日悖论，如果我们收集21282128哈希，我们在该集合中的两个散列之间有大约50％的碰撞。  
让我们说比特币网络每秒拉动1.7亿立陶宛。它接近这一点，这种选择使数学变得更简单。  
1.7亿特拉什人是1.7×10201.7×1020。同时，2128≈3.4×10382128≈3.4×1038。  
这意味着，如果我们在任务上设置了整个比特币网络，那么它将需要2×10182×1018秒才能找到碰撞。  
那是多久了？在一年内大约Π×107π×107秒，所以约6.4×10106.4×1010年。  
如果我做了我的数学权利，那将需要整个目前的比特币网络约64亿多年来有50％的机会找到SHA 256碰撞。  
所以，是的，非常不可能。  
### 回答 3
两个字符串可能具有相同的存在，这是一个像你说的简单计数争论。  
它不太可能发生，很难构建具有相同的字符串。  
对于较旧的哈希，这已成功完成，例如，MD5，对于SHA256很难做到  
### 回答 4
A2A：不。  
没有考虑到它。两个字符串肯定有可能具有相同的哈希。但是，很难找到具有相同哈希码的不同字符串。  
鸽子校长：有“只有”22562256不同的哈希代码。但是，由于这些字符串不限于256位，您可以散列哈斯赫的大大不同的字符串。他们不能都有不同的哈希。  
### 回答 5
这不是不可能的。它非常不可能。而且，即使有两个字符串具有相同的哈希，它们也不会“看起来更像彼此。而且，这是这种散游的重要品质。您无法拍摄字符串，并轻松对其进行一些更改并修复虚假字符串以具有相同的哈希。您可能有另一个具有相同哈希的字符串，但它不会是第一个字符串的虚假。  
### 回答 6
有坏消息，有好消息。  
坏消息是，即使是说，只有1-kbit串，每一个都是22562256哈希分享27682768。所以，不仅碰撞不是不可能的;他们很丰富。添加更多潜在的长度，您有噩梦大量的哈希碰撞。  
好消息是你不能拥有这么多字符串。因此，逐个逐个逐个的理论，总数不同的字符串根本无关紧要。重要的是，您实际上可以在某种应用中拥有多少个不同的字符串。所以，即使对于21002100不同的弦数，也有足够的稀疏性，因此是非常，非常小的碰撞概率。  
### 回答 7
每个相同的两个字符串都具有相同的哈希。两个非相同字符串的哈希相同，概率约为2英寸，如上所述，有无限的串，因此存在具有相同哈希值的无限多条串。  
### 回答 8
两个字符串真的不可能拥有同样的SHA-256哈希，或者它是不太可能被认为是不可能的吗？可能的哈希有限公司，但我们可以拥有无限的独特字符串，我错过了什么？  
您错过了关于捕捉的数学课程，即非注射的或非注射形状功能。然后（IM）概率取决于输出的熵，256是指数的大数字，即在碰撞时偶然绊倒。  
### 回答 9
不，你没有错过任何东西。由于所有输入映射到固定尺寸的输出，它绝对是确切的是多个输入（实际上只要输入尺寸不受限量的无限数）都可以产生任何给定的输出。  
问题在于找到它们。  
### 回答 10
如果SHA-256中的位数（256，其中每十六进制字符可能为4位，如果散列在十六进制中输出）短于位中的字符串的长度（调用n），则有2 ^ 256可能的哈希，2 ^ n可能的字符串，并且由于2 ^ 256是小于2 ^ n的方式，必须有不同的划线，具有相同的哈希。  
如果它们可以具有无限长度，则只有无限数量的字符串，而不是限于每个尺寸，如每一个特定尺寸。  
找到具有相同哈希的第二个字符串，作为给定字符串可能会非常耗时。  
### 回答 11
它是极不可能的，但可能的。2个不同随机选择的字符串具有相同SHA256哈希的赔率约为2256.2256。  
### 回答 12
你已经有了一些好的答案。我只会补充一点，哈希必须有点碰撞。例如，您不应该能够通过更改法律文档，例如添加几个0s，然后补偿其他地方的消息以获取相同的哈希。因此，消息的小变化必须导致哈希的大变化。因此，当您建议向文档制定有意义的更改以产生相同的哈希值，所以不太可能被认为是不可能的。但是，安全始终是相对的，对于大量数据，人们可能想要增加散列大小。  
### 回答 13
不，这不是不可能的。事实上，正如您所建议的那样，必须有一个无限数量的字符串，它将映射到给定的256位哈希。它只是不太可能找到与哈希相匹配的。基本上只有一个22562256字符串将匹配给定密钥，并且由于散列函数的结构，没有已知的方法来找到这样的字符串而不逐个搜索它们。  
### 回答 14
我认为这是无益的，因为许多现有答案做了，使散列函数具有比输入更小的输出，所以不能颠倒，因为它不是一对一的。  
SHA-256提供了比这更强大的挑战：很难提出任何无限的许多投入，其中哈希到特定价值。  
函数f（x）= 0f（x）= 0是散列函数，但不是特别好的。在恢复原始输入的感觉中不可能逆转，因为XX的所有信息都被抛弃了。但是对FF进行预报攻击是微不足道的。  
要理解为什么SHA-256（和类似的加密哈希）抵抗预测攻击，我们依赖于不同的属性，这是改变一点输入影响输出位的一半。这是通过将输入和中间状态混合在一起多次，以自身不可逆的方式来实现。使SHA-256类似于随机函数，其输入或输出之间没有可利用连接。  
例如，如果我们使用XOR作为散列算法的最后一步，并且我们知道输出位是一个，那么输入位可以是0和1，或者1和0.这为我们提供了两种需要考虑的可能性。如果这些输入位也是其他XOR或添加或非注射替换功能或其他任何可能的结果，那么我们有更多的可能性来考虑我们走的计算中的进一步回报。  
因此，即使我们将自己限制为256位输入和256位输出，逆转SHA-256也是困难的，这是一个基数参数不适用的制度。 （虽然SHA-256即使在这种情况下也不太可能是注射的。）  
您可能会查看答案，您如何解释为什么Sha-256是一个单向哈希函数，而不是进入其数学推导的非极客？或标记小家敲击答案是关于一个使它们不可逆转的单向哈希算法是什么？  
但这不是不可能的。我们可以在字典中取出所有单词，每个通过SHA-256喂食，并记录所有结果。然后，如果有人给了我们一个SHA-256哈希，我们可以看出它是否是我们的名单，如果是这样，那么这个词产生了它。您甚至可以在线找到此类网站，例如  
解码器：反向查找SHA256使用此工具在线哈希  
为每种可能的256位输入执行此操作是不可能的。为每6个字母的文本密码执行它是完全可行的。  
### 回答 15
SHA-256不是加密算法。它是一个加密强大的单向散列函数。如果您注意到，它没有与其关联的密钥.Cryptography强，一种方式意味着它对原始源输入来反转散列的计算方式不可行，或者任何其他输入，散列到相同的值。没有解密SHA-256哈希，因为没有加密。没有反转它。这是一个重要的特征。这篇文章的其余部分并不特定于任何特定的哈希特定。当你挑选一个加密的强大的哈希来说，那么你好。镜头，就像我的雨衣一样！让我们假设我们有一个哈希函数h（x）h（x），它不可行地找到任何功能h-1h- 1使这些属性中的任何一个都为任意输入xx：  
在第一种情况下，H-1H-1REVERSESSSSETH.ORDINGINALLINALLY，哈希值损失。但是，密码通常比我们用于密码的哈希值短（至少现在）。这意味着它可能实际上可以完全可以完全扭转哈希对于广泛的密码。我们必须避免在所有成本上。在第二种情况下，H-1H-1找到任何值，当提供给HH时，产生H（x）H（x）。碰撞（除非该值完全是XX）。我们必须避免容易找到的碰撞。[编辑：第二种情况下的H-1H-1返回的技术术语是逆图像，或者预测。试图确定h的行为-1h-1被称为预报攻击。我们正在寻找的哈希属性是预测阻力。]找到一个仅生成碰撞的输入可能不会像真正的反向那样糟糕，因为你不学习原始密码。您可能无法使用该输入登录使用相同密码的任何其他网站。此但是没有帮助我们使用我们的主要目标。我们失败了攻击者发现任何可以工作的输入的那一刻。因此，我们想要一个散列hh，其中找到了任何类型的h-1h-1是不可行的。对于方便起见，我将称之为哈希不可逆转。散列密码  
鉴于不可逆转的哈希，您可以通过将Salt值连接到密码，然后散列散列，即散列值。  
Hi = h（pi | si）hi = h（pi | si）  
hh是哈希函数.pipi，sisi和hihi分别是用户II的密码，盐和哈希值。垂直条表示连接。密码数据库直接存储哈希和盐（Hihi和Sisi）清楚。我们依靠事实没有一个可行的H-1H-1来保持PIPI秘密.Salts应该是随机的，独特的，最好的大。Salts确保当两个或两个以上的人有相同的密码时，他们都得到了不同的哈希。这是，即使pi = pjpi = pj，很好，嗨hi≠hjhi≠hj，只要si〗sjsi≠sj.so，如果你不能解密哈希，你不能自由地反转哈希，那么你怎么样验证密码吗？它容易！唯一一个  
当您计算存储的密码时，您将所有相同的步骤应用于用户输入。他们进入了正确的密码。我们永远不会将清晰的文件密码与清单密码尝试进行比较。我们将哈希密码与散列密码尝试进行比较。如果我们调用用户输入qiqi，那么您可以写出什么是尝试的：  
h（pi | si）=？h（qi | si）h（pi | si）=Δh（qi | si）  
因为依靠以下物业有效地是真的，即使它不严格：  
h（pi | si）= h（qi | si）⟹pi = qih（pi | si）= h（qi | si）⟹pi = qi  
脚步：  
仔细看看：一切都仍然是单向。我们总是从（密码|盐）到哈希，而不是反向方向。目的是好，因为我们选择了计算H-1H-1是不可行的。哈希是不可逆转的，但是我们仍然可以测试对它的任意密码尝试。当我们检查密码时，我们只学习一个细节：它是否匹配存储的密码？存储的密码不是，无法透露，没有任何昂贵的计算。为什么盐密码哈希被认为是基本的最佳实践。如果有人窃取密码数据库，他们就无法做到很多东西。他们不能反向回到原始密码。最好的他们可以做的是尝试散列密码猜测.Rainbow表盐  
现在，有攻击，如彩虹表，可能有助于攻击密码数据库。  
### 回答 16
这个问题误解了（我在第一次回答它时也是如此）SHA职能的用途。它们不是加密方法本身。你不发送某人哈希哈希，并希望他们能够重建消息。这不是它如何使用的。  
Sha Hash是一种签署消息的方式。每条消息都有一个SHA哈希，与其他附近的其他消息不同，即略微修改）消息。所以，当您发送消息时（加密（或以明文，无关紧要），此人可以运行SHA-256散列算法并获得结果哈希，并且应该匹配他们发送给您的值，如果它不起作用这条消息已被篡改。（顺便说一下，由于HA为SHA代表散列算法，因此，散列算法是多余的。）但是，对于合理的文本，SHA-256结果基本上是独一无二的攻击者无法用它篡改，并且很容易提出一个产生相同哈希的文本。  
但是，这类似于密码遍布的方式。您不会解密哈希密码的文件。您在密码和哈希上拍摄密码或猜测。如果密码与哈希匹配，则找到了有效的密码来访问该帐户。它可能实际上不是该人正在使用的密码，但它并不重要，因为哈希是正确的。现在，如果密码是一个可读的字符串，而且你的是一堆垃圾字符一起被扔在一起，你实际上并不知道他们的密码，但就访问他们的帐户而言，它无关紧要。  
同样，如果一个人找到一些与给定的SHD-256哈希碰撞的文本，则可以替换该消息的文本，因为哈希匹配，用户不知道它不是消息（除非用户知道某事）关于消息本身，例如它用英语编写或有点编程语言。您的随机文本可能无法成为英语或法律程序。  
所以，即使有人可以dcecrypt sha-256哈希，那是一个哈希生成一些产生所需哈希的文本。它们不太可能使用它来发送假消息，因为大多数匹配哈希的文本不是合理的消息。  
非常感谢Joe Zbiciak，提醒我真正使用了SHA系列的功能。  
现在，如果SHA系列的功能被用作加密机制，它们不是。然后我的原始邮件包括在下。但是，由于它们不是一个很好的加密机制，询问有人可以解密它们不是明智的问题。  
因此，如果SHA 256一直是加密，而不是哈希方法，则以下答案会有意义，但由于它们不是，它没有（这只是我不称呼自己的小部分）：  
绝对可能。这是否意味着它发生了？只要他们保持秘密，他们有（并且没有以一种使他们解密使用它的方法，我们可能永远不会知道。当然，在这种情况下，它可能没关系。  
如果有足够的数据，任何加密技术（除了一次性焊盘除外）必然会被损坏，并且通过足够的数据并通过足够的时间。加密只会为您购买时间，而不是实际保密..  
### 回答 17
哈希函数得到他们的加密力量不是不可能反转，而是从反转哈希的代码来看，需要很长时间才能运行并找到答案  
哈希可能是如何逆转的？有证据吗？  
写入程序以反转任何散列函数是琐碎的。任何初学者程序员都可以编写该代码，并且该代码证明它可以完成。如果你困惑，你是对人们困惑的，为什么人们一直告诉你，他们是不可能的，他们是错误的（或者更准确，你可能误解了他们的观点）。  
哈希函数获得了他们的加密力量不是不可能逆变，但从反转哈希的代码来看，需要很长时间才能运行并找到答案 - 说一百万年。  
哈希函数是不可能倒转的，他们是不切实际的颠倒。  
它们是一类程序，具有迷人的财产，以便在向前方向上计算它们非常快，但对计算逆口非常缓慢。  
这种类型的代码利用了破坏信息的所有计算机中存在基本功能的事实。这意味着当我们试图扭转它们时，我们发现前锋可能会达到答案的许多可能的路径。如果将两个二进制数字添加在一起并只占用结果的一个二进制数字，我们已启动了两位数据，并以一位结束。我们在过程中销毁或丢失了一点数据。我们如何扭转该代码？  
0 + 0 = 0  
1 + 1 = 0  
一个输出有两个不同的输入0.这两个输入中的哪一个是前进的代码，以获得0的输出？如果我们所知道的是输出为0，我们无法讲述。但如果任何一个输入产生相同的输出，您可能会认为我们不需要关心。  
但是，要使哈希函数工作，他们以两种不同的方式使用相同的技术，使您的反向答案选项仅适用，如果所有反向选项映射回相同的输入。  
所以说你有两位你想要哈希，a和b，并且输出具有作为散列输出的一个位的单个比特添加，以及作为输出的另一个比特的一个或b。因此，如果输入是A = 0，B = 0，则输出为00。如果输入是A = 1，B = 1，则输出为01。  
如果我们看出0的第一个输出位，我们无法判断输入是否为00或11.如果我们查看第二个输出位，则不能判断输入是否为01,10或11.如果单个步骤可以直接逆转。我们必须反转它们两个，生成所有可能输入的列表，然后搜索找到一个匹配的输入，为两个位产生正确的输出。要找到逆，我们必须扫描3x2或6个可能的路径，前向算法可以拍摄。如果我们不使用查找表即可快速地运行，则此简单函数大约为6倍。  
通过将像这样的大量操作组合在一起，反向路径可能会变得如此难以转换，你不能欺骗一个简单的反向查找表，唯一已知的解决方案是搜索所有可能的路径 - 我们可以制作它这需要一百万年。  
这一切都来自于计算机有许多丢失信息的原始函数（比如添加），因此具有多种可能的反转。  
哈希函数和其他这样的程序来逆转所有杠杆杠杆这种面对面使得颠倒散列的唯一方法是搜索一棵非常大的树的树，以找到正确的逆。  
到目前为止，没有已知的捷径来使逆键快速，但它从未证明过短削减不存在。那是你可能已经听说过的p vs np问题的一部分。  
### 回答 18
编号。  
假设你的车有一个只有2位数的里程表。它将在00，然后01开始，最终升至99，然后，稍后1公里，它会再次读00。  
假设这个里程表目前读了86.你在车里旅行了多远？  
你可能已经旅行了86公里。或186公里，或3086公里，或244,786公里。对于您的实际旅行有多远，它应该非常清楚，只考虑到86。  
因此，由于这种原因，不可能确定哪些文件产生给定的哈希H，因为有无数的文档tha  
编号。  
假设你的车有一个只有2位数的里程表。它将在00，然后01开始，最终升至99，然后，稍后1公里，它会再次读00。  
假设这个里程表目前读了86.你在车里旅行了多远？  
你可能已经旅行了86公里。或186公里，或3086公里，或244,786公里。对于您的实际旅行有多远，它应该非常清楚，只考虑到86。  
因此，由于这种原因，不确定确定哪些文件产生给定的哈希H，因为有无数的文档可以占据相同的值（尽管您可能永远无法找到2种这些文件 - 称为哈希碰撞。）  
SHA-256散列是32字节（256位），因此共2 ^ 256可能的SHA-256散列。这是大约1×10 ^ 77，a 1，后跟77零。  
即使我们仅限于普通的1页文档（例如，大小的1000个字符），即使每个这样的1页文档也是8000位，因此总共存在总共2 ^ 8000可能的1000字节文档。 （在基础10中，大致为1，然后是2,400零。）由于只有2 ^ 256可能的SHA-256哈希，我们可以减去8000-256 = 7744，并确定每个可能的SHA-256哈希，有2 ^ 7744可能的1页文件，必须所有确切的哈希值共享。  
当然，对于给定的SHA-256哈希H，即使有两个1页的文件，也只有两个1页的文件实际上是零的，即使有2 ^ 7744个可能的文件，也可以共享相同的哈希H.  
所以，解密SHA-256哈希H，将采用h（所有32字节的IT），并产生具有该哈希的2 ^ 7744一页消息。然后是所有的2页，3页。 。 。  
通过文档或消息采取的哈希值并不是该消息的加密，就像2位数尺上的第86次，这不是您驱动的距离的加密。它是文档或消息的减少的具体形式，不能逆转。  
### 回答 19
虽然Rubiks Cube类比在某些地区持有，但它失败了。 Rubiks Cube实际上是一种Trapdoor单向功能。除非是已知的，除非是众所周知，否则难以逆转，在这种情况下释放它。置换实际上是一个对称的键 - 如果我窃取它，我可以轻松返回解决状态。从这个意义上讲，Rubiks立方体对于加密方案来说是一种更好的类比，这通常与散列混淆。  
哈希函数（或一般函数一般）没有这个属性。无论您对这个过程所了解的信息如何，它们都是不可逆转的。 SHA256算法是公知的。这就是Rubiks Cube类比分开的地方 - 扰扰机制也将公开知名并逆转它变得微不足道。  
也许一个更好的类比是混合涂料。你用颜色开始。应用哈希的过程是您选择其他颜色的一个（每次是哈希确定性的每次），并将其与原始颜色混合。所得到的混合物（一些其他颜色）是散列的输出。请注意，即使我告诉您常常混合的颜色，即使是哪种颜色，您难以解锁它并将颜色分开。  
### 回答 20
是的。两个不同的字符串绝对可以提供相同的SHA256。如果您知道哈希需要2 ^ 256个评估，以查找给出相同哈希的另一个字符串。  
让我们说这需要1微秒来进行一次评估。  
确定第二个字符串的确定性需要3.6 x 10 ^ 63岁。赔率是它比这更快的。注意普遍接受的宇宙历史为138亿年，只需1.38 x 10 ^ 10。  
这是假设具有完美分布的完美哈希。 SHA256并不完美。如果可以利用该缺陷以减少解决方案空间的大小，因此您将获得更快的哈希值。  
或者，它是平行化的一个容易的问题。让我们说你有十亿台电脑。 3.6 x 10 ^ 54岁。让我们为每亿核来提供每一百亿计算机。 3.6x10 ^ 45岁。让我们一起与十亿个行星一起工作，每个行星都有10亿台核心的电脑。 3.6 x 10 ^ 36年。  
显然，我们需要更快的计算机。 1每个微秒的Eval是太慢的。让我们每一个纳秒做一个。地狱，让他们每一个纳秒都做十亿。  
2 ^ 256纳秒/ 10亿^ 3多年= 3.6x10 ^ 24  
即：2 ^ 256是非常非常非常大的数字。每个Bruce Schneier（这些数字......）强烈意味着，直到电脑从事以外的东西构建并占用空间以外的东西，强烈攻击对抗256位钥匙的攻击将是不可行的。  
### 回答 21
是的，如果哈希函数是安全的，那么对于任何给定的输入A，应该有一个无限数的输入b，使得散列（b）=散列（a）。如果不是这种情况，那么一些其他哈希值将超重并找到碰撞将更容易。  
您可以在运行中考虑像状态机（每个块的一个状态转换）。 。这可用于创建无限的碰撞序列，因为QA，QRA，QRRA等都将具有相同的输出。因此，我们可以创建一个无限的此表单输入，所有这些表单都有一个无限的碰撞。然而，它不保证存在这样的序列，使得A和QA对于给定A的输出是相同的输出，或者a是一些重复输入的前缀。  
我们也可以推理概率。如果哈希函数随机分配NN位输出，则给出序列A，则存在与另一输入的碰撞概率2-N2-n。如果我们尝试所有2n2n位输出，如果非常低（我们会发现的预期数字是2n2n的预期数量，则无法发现碰撞的概率，实际上我们可以尝试所有3n3n位输出，4n4n位输出等。创建具有空值的概率0的无限序列。  
但是，真实世界的哈希函数可能具有恰好的限制，使得分布比完全随机的位数。可能没有输入返回SHA-256到其初始状态的输入，或者某些输出仅通过短输入来达到，但不限于长输入。但只有很多这样的案例就可以了。  
### 回答 22
SHA512或技术上SHA2是当今最安全的哈希功能之一。虽然SHA有相当几种攻击，但它们都没有完全成功。  
实际上，从哈希函数解密输出并不是那么容易。使用不同类型的攻击来解密沙。以下是最着名的。  
2 ^ 240 * 2 ^ -2 = 2 ^ 238〜10 ^ 72s〜3,17 * 10 ^ 64年  
2.碰撞攻击  
3.伪碰撞  
使用256位的SHA-1被认为被破坏，因此凝结在2 ^ 69操作中识别得多小于2 ^ 80。  
上述攻击中的任何一个都不能用SHA-1或SHA-2 ALGO产生的哈希，并在地球上提供最佳的硬件。  
关于在线解密的工具的其他问题。他们实际上并没有破解你给出的哈希。该工具只需将其数据库中提供的哈希值进行比较。他们维护一个数据库，有一些字符串的哈希。当您尝试在任何网站上进行加密字符串时，它们会保存数据库中的哈希和纯文本。因此，当您尝试解密哈希时，您将获得结果。  
尝试这个简单的练习来确保SHA2没有被打破。  
所以，要得出结论，他们实际上向你展示了计算的结果，但不会破解哈希。  
SHA2仍然是安全的。  
干杯!  
### 回答 23
取决于你的意思更好。如果您的目标是具有更高水平的碰撞电阻，则任何具有大于512位输出的密码良好的散列函数都会比SHA-512更好。在这方面，Keccak（SHA-3指定）肯定会更好。但是，较大的输出尺寸为价格。 Keccak的速度比SHA-512慢。  
转移到Keccak的原因需要被理解为完全掌握潜在的问题。由于SHA-512的前辈X的精彩密码攻击（即MD4，MD5，SHA-0和SHA-1），许多在Crypto社区中，包括NIST中的人开始感受需要更换对于SHA-2家族（SHA-224,256,384和512），因为SHA-2的设计原则与其前辈相同。精确地，所有这些都由Davies-Meyer模式中的块密码组成，Merkle-Damgaard加强。正是由于这个原因，NIST开始对SHA-3的竞争。虽然，大多数加密人士认为SHA-512将在未来30  -  40年内确保，我们仍然有SHA-3竞争。  
有关Keccak的更多信息，带有SHA-512：Keccak海绵功能系列。在本网站上遍历，您可以获得有关Keccak的新设计的大量信息。  
最后，一个很好的加密设计必须承受时间的考验，而顶级密码分析师则试图在设计中找到弱点。 Keccak（或任何SHA-3入围者）在这种意义上是新的。在对他们的小说攻击将被审判和（可能）失败之前需要几年时间。我个人找到了Keccak成为一个伟大的哈希函数。  
