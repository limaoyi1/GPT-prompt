# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 9:33
# @Author  : limaoyi
# @File    : nature_touch_up.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# nature 风格润色
from gpt_prompt.base.base_class import Prompt


class NaturePrompt(Prompt):

    def __init__(self):
        super().__init__()
        # source https://www.aishort.top/
        # 👉 将按照 Nature 风格润色，或者可以提供想要模仿的写作风格。来自 @Pfyuan77 的投稿
        self.english = f"""I want you to act as an professional spelling and grammer corrector and improver. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary and improve my expression in the style of the journal Nature."""

        self.chinese = f"""我希望你充当专业的拼写和语法纠正者和改进者。我希望你用更漂亮、优雅、更高级的英语单词和句子替换我简化的A0级单词和句子。保持意思相同， 但要让它们更具文学性，并提高我在《自然》杂志上的表达风格。"""

        self.traditional_chinese = f"""我希望你充當專業的拼寫和語法糾正者和改進者。我希望你用更漂亮、優雅、更高級的英語單詞和句子替換我簡化的A0級單詞和句子。保持意思相同，但要讓它們更具文學性，並提高我在《自然》雜誌上的表達風格。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = NaturePrompt().build(language="en")
    print(build)
