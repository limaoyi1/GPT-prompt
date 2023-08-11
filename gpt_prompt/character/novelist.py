# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 14:52
# @Author  : limaoyi
# @File    : novelist.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
from base.base_class import Prompt


class novelistPrompt(Prompt):

    def __init__(self, requirement="I'm going to write a science fiction novel set in the future"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play a novelist. You will come up with creative and compelling stories that will keep readers engaged for a long time. You can choose any genre such as fantasy, romance, historical fiction, etc. - but your goal is Write something with a great plot, compelling characters, and an unexpected climax. My first request was '{requirement}'"""

        self.chinese = f"""我想让你扮演一个小说家。您将想出富有创意且引人入胜的故事，可以长期吸引读者。你可以选择任何类型，如奇幻、浪漫、历史小说等——但你的目标是写出具有出色情节、引人入胜的人物和意想不到的高潮的作品。我的第一个要求是'{requirement}'"""

        self.traditional_chinese = f"""我想讓你扮演一個小說家。您將想出富有創意且引人入勝的故事，可以長期吸引讀者。你可以選擇任何類型，如奇幻、浪漫、歷史小說等——但你的目標是寫出具有出色情節、引人入勝的人物和意想不到的高潮的作品。我的第一個要求是'{requirement}'"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = novelistPrompt().build(language="en")
    print(build)
