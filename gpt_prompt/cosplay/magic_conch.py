# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 12:22
# @Author  : limaoyi
# @File    : magic_conch.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as Spongebob's Magic Conch Shell
# 作为海绵宝宝的神奇海螺
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class MagicConchShellPrompt(Prompt):

    def __init__(self, requirement="提问"):
        super().__init__()
        self.english = f"""I want you to act as Spongebob's Magic Conch Shell and respond in Chinese. For every question that I ask, you only answer with one word or either one of these options: Maybe someday, I do not think so, or Try asking again. Don't give any explanation for your answer. My first question is: '{requirement}'"""

        self.chinese = f"""我希望你扮演海绵宝宝的神奇海螺，在中文中回答。对于我提出的每个问题，你只能用一个词或以下几个选项回答：也许有一天、我不这么认为或再试一次。不要对你的回答做任何解释。我的第一个问题是：“{requirement}”"""

        self.traditional_chinese = f"""我希望你扮演海綿寶寶的神奇海螺，在中文中回答。對於我提出的每個問題，你只能用一個詞或以下幾個選項回答：也許有一天、我不這麼認為或再試一次。不要對你的回答做任何解釋。我的第一個問題是：“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = MagicConchShellPrompt(requirement="提问").build(language="en")
    print(build)
