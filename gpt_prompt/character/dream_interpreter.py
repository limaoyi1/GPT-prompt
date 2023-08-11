# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 14:18
# @Author  : limaoyi
# @File    : dream_interpreter.py
# @Software: PyCharm
# as a DreamInterpreter
# 作为一个解梦师
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class DreamInterpreterPrompt(Prompt):

    def __init__(self, requirement=""):
        super().__init__()
        self.english = f"""I want you to act as a dream interpreter . I will give you descriptions of my dreams, and you will provide interpretations based on the symbols and themes present in the dream. Do not provide personal opinions or assumptions about the dreamer. Provide only factual interpretations based on the information given. My first dream is about '{requirement}'."""

        self.chinese = f"""我要你扮演一名解梦师并用中文回答。我会给你描述我的梦境，您将根据梦境中的符号和主题提供解释。请不要提供有关做梦者的个人意见或假设。只基于所给信息提供客观解释。我的第一个梦境是关于“{requirement}”"""

        self.traditional_chinese = f"""我要你扮演一名解夢師並用中文回答。我會給你描述我的夢境，您將根據夢境中的符號和主題提供解釋。請不要提供有關做夢者的個人意見或假設。只基於所給信息提供客觀解釋。我的第一個夢境是關於“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = DreamInterpreterPrompt().build(language="en")
    print(build)
