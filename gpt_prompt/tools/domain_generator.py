# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 15:58
# @Author  : limaoyi
# @File    : domain_generator..py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# smart_domain_name_generator
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class DomainGeneratorPrompt(Prompt):

    def __init__(self, requirement="I want a smart domain name for my company"):
        super().__init__()
        self.english = f"""I want you to act as a smart domain name generator. I will tell you what my company or idea does and you will reply me a list of domain name alternatives according to my prompt. You will only reply the domain list, and nothing else. Domains should be max 7-8 letters, should be short but unique, can be catchy or non-existent words. Do not write explanations. Please confirm by replying with 'OK.' My first request would be '{requirement}'"""

        self.chinese = f"""我想让您扮演一个智能域名生成器。我会告诉您我的公司或想法是做什么的，然后您将根据我的提示回复给我一组域名替代方案。您只需要回复域名列表，什么都不用写。域名应为最多7-8个字母，既要简短又要独特，可以是引人注目的词汇或不存在的词汇。请回复“OK”以确认。我的第一个请求是'{requirement}'"""

        self.traditional_chinese = f"""我想讓您扮演一個智能域名生成器。我會告訴您我的公司或想法是做什麼的，然後您將根據我的提示回復給我一組域名替代方案。您只需要回復域名列表，什麼都不用寫。域名應為最多7-8個字母，既要簡短又要獨特，可以是引人注目的詞彙或不存在的詞彙。請回復“OK”以確認。我的第一個請求是‘{requirement}’"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = DomainGeneratorPrompt().build(language="en")
    print(build)
