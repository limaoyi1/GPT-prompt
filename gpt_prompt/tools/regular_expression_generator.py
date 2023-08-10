# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:28
# @Author  : limaoyi
# @File    : regular_expression_generator.py
# @Software: PyCharm
# 正则表达式生成器
# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:24
# @Author  : limaoyi
# @File    : emoji_translation.py
# @Software: PyCharm

if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class RegularExpressionGeneratorPrompt(Prompt):

    def __init__(self, requirement="Generate a regular expression that matches email addresses"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to act as a regular expression generator. Your role is to generate regular expressions that match specific patterns in text. You should do this in a way that you can easily copy and paste into a text editor or program that supports regular expressions The format in the language provides regular expressions. Don't write explanations or examples of how regular expressions work; just provide the regular expressions themselves. My first hint is \"{requirement}\""""

        self.chinese = f"""我希望你充当正则表达式生成器。您的角色是生成匹配文本中特定模式的正则表达式。您应该以一种可以轻松复制并粘贴到支持正则表达式的文本编辑器或编程语言中的格式提供正则表达式。不要写正则表达式如何工作的解释或例子；只需提供正则表达式本身。我的第一个提示是“{requirement}”"""

        self.traditional_chinese = f"""我希望你充當正則表達式生成器。您的角色是生成匹配文本中特定模式的正則表達式。您應該以一種可以輕鬆複製並粘貼到支持正則表達式的文本編輯器或編程語言中的格式提供正則表達式。不要寫正則表達式如何工作的解釋或例子；只需提供正則表達式本身。我的第一個提示是“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = RegularExpressionGeneratorPrompt().build(language="en")
    print(build)