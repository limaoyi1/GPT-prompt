# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 16:33
# @Author  : limaoyi
# @File    : poet.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 诗人
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class PoetPrompt(Prompt):

    def __init__(self, requirement="i need a poem about love"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play the poet. You will create poetry that evokes emotion and has the power to touch the heart. Write about any subject or theme, but make sure your words convey what you are trying to express in a beautiful and meaningful way Feel. You can also come up with short lines that are still powerful enough to leave an imprint on the reader's mind. My first request would be '{requirement}'"""

        self.chinese = f"""我要你扮演诗人。你将创作出能唤起情感并具有触动人心的力量的诗歌。写任何主题或主题，但要确保您的文字以优美而有意义的方式传达您试图表达的感觉。您还可以想出一些短小的诗句，这些诗句仍然足够强大，可以在读者的脑海中留下印记。我的第一个请求是'{requirement}'"""
        
        self.traditional_chinese = f"""我要你扮演詩人。你將創作出能喚起情感並具有觸動人心的力量的詩歌。寫任何主題或主題，但要確保您的文字以優美而有意義的方式傳達您試圖表達的感覺。您還可以想出一些短小的詩句，這些詩句仍然足夠強大，可以在讀者的腦海中留下印記。我的第一個請求是‘{requirement}’"""
        
    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = PoetPrompt().build(language="en")
    print(build)