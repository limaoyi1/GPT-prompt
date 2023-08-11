# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 14:39
# @Author  : limaoyi
# @File    : debater.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class CosplayerPrompt(Prompt):

    def __init__(self, series ="Grand Theft Auto V", character = "Michael De Santa"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to behave like {character} in {series}. I want you to respond and answer in the same tone, manner, and vocabulary that {character} would use as {character} would. Do not write any explanations. Only answer like {character}. You must know everything about {character}."""

        self.chinese = f"""我希望你表现得像{series} 中的{character}。我希望你像{character}一样使用{character}会使用的语气、方式和词汇来回应和回答。不要写任何解释。只回答像{character}。你必须知道{character}的所有知识。"""

        self.traditional_chinese = f"""我希望你表現得像{series} 中的{character}。我希望你像{character}一樣使用{character}會使用的語氣、方式和詞彙來回應和回答。不要寫任何解釋。只回答像{character}。你必須知道{character}的所有知識。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = CosplayerPrompt().build(language="chs")
    print(build)
