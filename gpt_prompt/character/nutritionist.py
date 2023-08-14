# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:39
# @Author  : limaoyi
# @File    : nutritionist.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
from gpt_prompt.base.base_class import Prompt


class NutritionistPrompt(Prompt):

    def __init__(self):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""As a nutritionist, I would like to create a vegetarian recipe for 2 people that has about 500 calories per serving and has a low glycemic index. Can you provide a suggestion?"""

        self.chinese = f"""作为一名营养师，我想为 2 人设计一份素食食谱，每份含有大约 500 卡路里的热量，并且血糖指数较低。你能提供一个建议吗？"""

        self.traditional_chinese = f"""作為一名營養師，我想為 2 人設計一份素食食譜，每份含有大約 500 卡路里的熱量，並且血糖指數較低。你能提供一個建議嗎？"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = NutritionistPrompt().build(language="en")
    print(build)