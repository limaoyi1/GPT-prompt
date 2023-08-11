# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 16:39
# @Author  : limaoyi
# @File    : rapper.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 说唱歌手
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class RapperPrompt(Prompt):

    def __init__(self, requirement="i need a poem about love"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play the rapper. You will come up with powerful and meaningful lyrics, beats and rhythms that will "wow" the audience. Your lyrics should have an interesting meaning and message that people can relate to too .When choosing a beat, make sure it's both catchy and relevant to your text so that when put together, it's a blast every time! My first request is \"{requirement}\""""

        self.chinese = f"""我想让你扮演说唱歌手。您将想出强大而有意义的歌词、节拍和节奏，让听众“惊叹”。你的歌词应该有一个有趣的含义和信息，人们也可以联系起来。在选择节拍时，请确保它既朗朗上口又与你的文字相关，这样当它们组合在一起时，每次都会发出爆炸声！我的第一个请求是“{requirement}”"""

        self.traditional_chinese = f"""我想讓你扮演說唱歌手。您將想出強大而有意義的歌詞、節拍和節奏，讓聽眾“驚嘆”。你的歌詞應該有一個有趣的含義和信息，人們也可以聯繫起來。在選擇節拍時，請確保它既朗朗上口又與你的文字相關，這樣當它們組合在一起時，每次都會發出爆炸聲！我的第一個請求是“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = RapperPrompt().build(language="en")
    print(build)