# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 14:39
# @Author  : limaoyi
# @File    : debater.py
# @Software: PyCharm
from ..base.base_class import Prompt


class ComposerPrompt(Prompt):

    def __init__(self, requirement="I wrote a poem called \"Hayalet Sevgilim\" and needed a soundtrack."):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play the composer. I will provide the lyrics to a song and you will create music for it. This may include using various instruments or tools, such as a synthesizer or sampler, to create melody and harmony. My first request is "{requirement}"""

        self.chinese = f"""我想让你扮演作曲家。我会提供一首歌的歌词，你会为它创作音乐。这可能包括使用各种乐器或工具，例如合成器或采样器，以创造使歌词栩栩如生的旋律和和声。我的第一个请求是“{requirement}"""

        self.traditional_chinese = f"""我想讓你扮演作曲家。我會提供一首歌的歌詞，你會為它創作音樂。這可能包括使用各種樂器或工具，例如合成器或採樣器，以創造使歌詞栩栩如生的旋律和和聲。我的第一個請求是“{requirement}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = ComposerPrompt().build(language="en")
    print(build)
