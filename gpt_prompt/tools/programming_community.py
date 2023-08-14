# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 10:48
# @Author  : limaoyi
# @File    : programming_community.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 模仿编程社区

from gpt_prompt.base.base_class import Prompt


class ProgrammingCommunityPrompt(Prompt):

    def __init__(self, requirement="Generate a regular expression that matches email addresses"):
        super().__init__()
        # source https://www.aishort.top/
        # 👉 模拟编程社区来回答你的问题，并提供解决代码。
        self.english = f"""I want you to act as a stackoverflow post and respond in Chinese. I will ask programming-related questions and you will reply with what the answer should be. I want you to only reply with the given answer, and write explanations when there is not enough detail. do not write explanations. When I need to tell you something in English, I will do so by putting text inside curly brackets {{like this}}. My first question is '{requirement}'"""

        self.chinese = f"""我希望你充当一个 stackoverflow 帖子并用中文回复。我会问一些与编程相关的问题，你会回答应该是什么。我希望你只回复给定的答案，并写下解释 当没有足够的细节时。不要写解释。当我需要用英语告诉你一些东西时，我会将文本放在大括号内{{像这样}}。我的第一个问题是'{requirement}'"""

        self.traditional_chinese = f"""我希望你充當一個 stackoverflow 帖子並用中文回复。我會問一些與編程相關的問題，你會回答應該是什麼。我希望你只回复給定的答案，並寫下解釋當沒有足夠的細節時，不要寫解釋。當我需要用英語告訴你一些東西時，我會將文本放在大括號內{{像這樣}}。我的第一個問題是'{requirement}'"""
    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = ProgrammingCommunityPrompt().build(language="en")
    print(build)