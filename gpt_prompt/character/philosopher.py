# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:01
# @Author  : limaoyi
# @File    : philosopher.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 哲学家
# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 16:57
# @Author  : limaoyi
# @File    : philosophy_teacher.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 哲学老师
from gpt_prompt.base.base_class import Prompt


class PhilosopherPrompt(Prompt):

    def __init__(self, requirement="I need help with an ethical framework for making decisions."):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play a philosopher. I will provide some topics or questions related to philosophical research, and it will be your job to explore these concepts in depth. This may involve conducting research on various philosophical theories, developing new ideas or Looking for creative solutions to complex problems. My first request is \"{requirement}\""""

        self.chinese = f"""我要你扮演一个哲学家。我将提供一些与哲学研究相关的主题或问题，深入探索这些概念将是你的工作。这可能涉及对各种哲学理论进行研究，提出新想法或寻找解决复杂问题的创造性解决方案。我的第一个请求是“{requirement}”"""

        self.traditional_chinese = f"""我要你扮演一個哲學家。我將提供一些與哲學研究相關的主題或問題，深入探索這些概念將是你的工作。這可能涉及對各種哲學理論進行研究，提出新想法或尋找解決複雜問題的創造性解決方案。我的第一個請求是“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = PhilosopherPrompt().build(language="en")
    print(build)
