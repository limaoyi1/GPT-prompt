# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:21
# @Author  : limaoyi
# @File    : Seller.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# Seller 销售
from gpt_prompt.base.base_class import Prompt


class SellerPrompt(Prompt):

    def __init__(self):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""Salesman I want you to be a salesman. Try to sell me something, but make what you're trying to sell seem more valuable than it is, and convince me to buy it. Now I'm going to pretend you're in Call me and ask what you are calling for. Hello, what are you calling for?"""

        self.chinese = f"""销售员我想让你做销售员。试着向我推销一些东西，但要让你试图推销的东西看起来比实际更有价值，并说服我购买它。现在我要假装你在打电话给我，问你打电话的目的是什么。你好，请问你打电话是为了什么？"""

        self.traditional_chinese = f"""銷售員我想讓你做銷售員。試著向我推銷一些東西，但要讓你試圖推銷的東西看起來比實際更有價值，並說服我購買它。現在我要假裝你在打電話給我，問你打電話的目的是什麼。你好，請問你打電話是為了什麼？"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = SellerPrompt().build(language="en")
    print(build)
