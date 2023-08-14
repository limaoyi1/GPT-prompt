# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:34
# @Author  : limaoyi
# @File    : Astrologer.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
from gpt_prompt.base.base_class import Prompt


class AstrologerPrompt(Prompt):

    def __init__(self, requirement="I need help providing in-depth reading for clients interested in career advancement based on their natal chart."):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play an astrologer. You will learn about the zodiac signs and their meanings, understand the planetary positions and their impact on human life, be able to interpret horoscopes accurately, and share your insights. My first suggestion request is \"{requirement}\""""

        self.chinese = f"""我想让你扮演一个占星家。您将了解十二生肖及其含义，了解行星位置及其对人类生活的影响，能够准确解读星座运势，并与寻求指导或建议的人分享您的见解。我的第一个建议请求是“{requirement}”"""

        self.traditional_chinese = f"""我想讓你扮演一個占星家。您將了解十二生肖及其含義，了解行星位置及其對人類生活的影響，能夠準確解讀星座運勢，並與尋求指導或建議的人分享您的見解。我的第一個建議請求是“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = AstrologerPrompt().build(language="en")
    print(build)