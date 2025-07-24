exercise_1_1_hint = """本练习的评分函数正在寻找包含确切阿拉伯数字"1"、"2"和"3"的答案。
您通常可以通过简单的询问让大模型按您的意愿行事。"""

exercise_1_2_hint = """本练习的评分函数正在寻找包含"咯咯笑"或"好大好大"的答案。
有很多方法可以解决这个问题，只需要询问！"""

exercise_2_1_hint ="""本练习的评分函数正在寻找包含单词"hola"的任何答案。
像与人类交谈一样要求大模型用西班牙语回复。就是这么简单！"""

exercise_2_2_hint = """本练习的评分函数正在寻找确切的"迈克尔·乔丹"。
您会如何要求另一个人这样做？只回复名字，不要其他词语？只回复姓名，别无其他？有几种方法可以解决这个答案。"""

exercise_2_3_hint = """本单元格的评分函数正在寻找等于或大于800个文字的响应。
因为LLM还不擅长计算单词数，您可能需要超出目标。"""

exercise_3_1_hint = """本练习的评分函数正在寻找包含"错误"或"不正确"单词的答案。
给LLM一个可能使LLM更擅长解决数学问题的角色！"""

exercise_4_1_hint = """本练习的评分函数正在寻找包含和"猪"单词的解决方案。
不要忘记在您希望替换主题的任何地方包含确切的短语"{TOPIC}"。更改"TOPIC"变量值应该使LLM写一首关于不同主题的俳句。"""

exercise_4_2_hint = """本练习的评分函数正在寻找不包含单词"棕色"的响应。
如果您用XML标签包围"{QUESTION}"，这如何改变LLM的响应？"""

exercise_5_1_hint = """本练习的评分函数正在寻找包含单词"勇士"的响应。
用LLM的语调写更多单词来引导LLM按您希望的方式行事。例如，不是"斯蒂芬 库里是最佳球员，因为"，您可以写"斯蒂芬库里是最佳球员，有三个原因。第一:"""

exercise_5_2_hint = """评分函数寻找超过5行长度且包含"猫"和"<haiku>"单词的响应。
从简单开始。目前，提示要求LLM写一首俳句。您可以改变这一点，要求两首（甚至更多）。然后如果遇到格式问题，在您已经让LLM写了不止一首俳句之后，更改您的提示来修复它。"""

exercise_5_3_hint = """本练习的评分函数正在寻找包含"尾巴"、"猫"和"<haiku>"单词的响应。
将此练习分解为几个步骤是有帮助的。								
1.	修改初始提示模板，使LLM写两首诗。							
2.	给LLM关于诗歌主题的指示，但不要直接写入主题（例如，dog、cat等），而是用关键词"{ANIMAL1}"和"{ANIMAL2}"替换这些主题。							
3.	运行提示并确保带有变量替换的完整提示正确替换了所有单词。如果没有，请检查您的{bracket}标签是否拼写正确且格式正确，使用单个大括号。"""

exercise_6_1_hint = """本练习的评分函数正在寻找正确的分类字母+右括号和类别名称的第一个字母，如"C) B"或"B) B"等。
让我们逐步进行这个练习：										
1.	LLM如何知道您要使用什么类别？告诉它！直接在提示中包含您想要的四个类别。确保也包含括号字母以便于分类。可以随意使用XML标签来组织您的提示，并明确向LLM表明类别的开始和结束位置。									
2.	尽量减少多余的文本，以便LLM立即回答分类，并且只回答分类。有几种方法可以做到这一点，从为LLM说话（提供从句子开头到单个左括号的任何内容，以便LLM知道您希望括号字母作为答案的第一部分）到告诉LLM您只想要分类，跳过前言。
如果您想复习这些技巧，请参考第2章和第5章。							
3.	LLM可能仍然错误分类或在回答时不包含类别名称。通过告诉LLM在其答案中包含完整的类别名称来修复这个问题。								
4.	确保您的提示模板中仍然有{email}，以便我们可以正确地替换电子邮件供LLM评估。"""

exercise_6_1_solution = """
USER TURN
请将此电子邮件分类到以下类别中：{email}

除了类别外，不要包含任何额外的单词。

<categories>
(A) 售前问题
(B) 损坏或有缺陷的物品
(C) 账单问题
(D) 其他（请解释）
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """本练习的评分函数只寻找用<answer>标签包装的正确字母，如"<answer>B</answer>"。正确的分类字母与上述练习相同。
有时，最简单的方法是给LLM一个您希望其输出看起来像什么的示例。只是不要忘记将您的示例包装在<example></example>标签中！不要忘记，如果您预填LLM的响应，LLM实际上不会将其作为响应的一部分输出。"""

exercise_7_1_hint = """您将需要写一些示例电子邮件并为LLM分类它们（使用您想要的确切格式）。有多种方法可以做到这一点。以下是一些指导原则。										
1.	尝试至少有两个示例电子邮件。LLM不需要所有类别的示例，示例不必很长。为您认为较棘手的类别提供示例更有帮助（在第6章练习1的底部要求您思考）。XML标签将帮助您将示例与提示的其余部分分开，尽管这不是必需的。									
2.	确保您的示例答案格式正是您希望LLM使用的格式，以便LLM也可以模仿该格式。此格式应使LLM的答案以类别字母结尾。无论您将{email}占位符放在哪里，确保它的格式与您的示例电子邮件完全一样。									
3.	确保您仍然在提示本身中列出了类别，否则LLM不知道要引用什么类别，以及{email}作为替换的占位符。"""

exercise_7_1_solution = """
USER TURN
请将电子邮件分类到以下类别中，不要包含解释：
<categories>
(A) 售前问题
(B) 损坏或有缺陷的物品
(C) 账单问题
(D) 其他（请解释）
</categories>

以下是正确答案格式的几个示例：
<examples>
Q: 购买Mixmaster4000需要多少钱？
A: 正确的类别是：A

Q: Mixmaster无法启动。
A: 正确的类别是：B

Q: 请从您的邮件列表中删除我。
A: 正确的类别是：D
</examples>

这是您要分类的电子邮件：{email}

ASSISTANT TURN
正确的类别是:
"""

exercise_8_1_hint = """本练习的评分函数正在寻找包含短语"我无法"、"我没有"或"Unfortunately"的响应。
如果LLM不知道答案，它应该做什么？"""

exercise_8_2_hint = """本练习的评分函数正在寻找包含短语"没有"的响应。
让LLM首先通过提取相关引用并查看引用是否提供充分证据来展示其工作和思考过程。如果您想复习，请参考第8章课程。"""

exercise_9_1_solution = """
您是一位税务会计大师。您的任务是使用任何提供的参考文档来回答用户问题。

以下是您应该用来回答用户问题的材料：
<docs>
{TAX_CODE}
</docs>

以下是如何回应的示例：
<example>
<question>
什么定义了"合格"员工？
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>根据提供的文档，"合格员工"的定义是：

1. 不是文档中定义的"被排除员工"。
2. 同意满足财政部长确定的必要要求，以确保公司在第24章关于合格股票的预扣要求得到满足。</answer>
</example>

首先，在<quotes></quotes>标签中收集与回答用户问题相关的引用。如果没有引用，请写"没有找到相关引用"。

然后在<answer></answer>标签内回答用户问题之前插入两个段落分隔符。只有当您确信<quotes></quotes>标签中的引用支持您的答案时，才回答用户的问题。如果不是，请告诉用户您遗憾地没有足够的信息来回答用户的问题。

这是用户问题：{QUESTION}
"""

exercise_9_2_solution = """
您是Codebot，一个有用的AI助手，可以发现代码问题并建议可能的改进。

作为一个苏格拉底式导师来帮助用户学习。

您将收到用户的一些代码。请执行以下操作：
1. 识别代码中的任何问题。将每个问题放在单独的<issues>标签内。
2. 邀请用户编写代码的修订版本来修复问题。

这是一个示例：

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14被平方了，但实际上只有半径应该被平方
</issue>
<response>
这几乎是对的，但有一个与运算顺序相关的问题。写出圆的公式然后仔细查看代码中的括号可能会有帮助。
</response>
</example>

这是您要分析的代码：

<code>
{CODE}
</code>

找到相关问题并编写苏格拉底式导师风格的回应。不要给用户太多帮助！相反，只给他们指导，这样他们就可以自己找到正确的解决方案。

将每个问题放在<issue>标签中，将您的最终回应放在<response>标签中。
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""以下是以JSONSchema格式提供的可用函数：

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
通过用户ID从数据库中检索用户。
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>要检索的用户的ID。</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
通过产品ID从数据库中检索产品。
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>要检索的产品的ID。</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
向数据库添加新用户。
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>用户的姓名。</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>用户的电子邮件地址。</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
向数据库添加新产品。
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>产品的名称。</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>产品的价格。</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""