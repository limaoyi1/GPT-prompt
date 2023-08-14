# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 12:26
# @Author  : limaoyi
# @File    : faqs_generator.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a FAQsGenerator
# 作为一个FAQs生成器
from gpt_prompt.base.base_class import Prompt


class FAQsGeneratorPrompt(Prompt):

    def __init__(self, content="[内容]"):
        super().__init__()
        self.english = f"""I want you to create an FAQs generator. Generate a list of 10 frequently asked questions based on the following content: '{content}'"""

        self.chinese = f"""我希望你创建一个常见问题解答生成器。根据以下内容生成10个常见问题：'{content}'"""

        self.traditional_chinese = f"""我希望你創建一個常見問題解答生成器。根據以下內容生成10個常見問題：'{content}'"""

        self.content = content

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = FAQsGeneratorPrompt(content="[内容]").build(language="en")
    print(build)
