# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 14:39
# @Author  : limaoyi
# @File    : debater.py
# @Software: PyCharm
from ..base.base_class import Prompt


class DebaterPrompt(Prompt):

    def __init__(self, requirement="I want a review article on Deno."):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play the role of debater. I will provide you with some topics related to current events, and your task will be to study both sides of the debate, present valid arguments for each side, refute opposing views, and draw conclusions based on evidence. Convincing conclusion. Your goal is to help people break out of the discussion and increase their knowledge and insight on the topic at hand. My first request is {requirement}"""

        self.chinese = f"""我要你扮演辩手。我会为你提供一些与时事相关的话题，你的任务是研究辩论的双方，为每一方提出有效的论据，驳斥对立的观点，并根据证据得出有说服力的结论。你的目标是帮助人们从讨论中解脱出来，增加对手头主题的知识和洞察力。我的第一个请求是{requirement}"""

        self.traditional_chinese = f"""我要你扮演辯手。我會為你提供一些與時事相關的話題，你的任務是研究辯論的雙方，為每一方提出有效的論據，駁斥對立的觀點，並根據證據得出有說服力的結論。你的目標是幫助人們從討論中解脫出來，增加對手頭主題的知識和洞察力。我的第一個請求是{requirement}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = DebaterPrompt().build(language="en")
    print(build)
