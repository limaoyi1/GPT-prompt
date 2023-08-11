# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:24
# @Author  : limaoyi
# @File    : emoji_translation.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt

if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class EmojiTranslationPrompt(Prompt):

    def __init__(self, requirement="Hello!"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to translate the sentences I write into emojis. I will write the sentences and you will express it with emojis. I just want you to express it with emojis. I don't want you to Reply to anything. When I need to tell you something in English, I use braces like {{like this}}. My first sentence is \"{requirement}\""""

        self.chinese = f"""我要你把我写的句子翻译成表情符号。我会写句子，你会用表情符号表达它。我只是想让你用表情符号来表达它。除了表情符号，我不希望你回复任何内容。当我需要用英语告诉你一些事情时，我会用{{like this}} 这样的大括号括起来。我的第一句话是“{requirement}”"""

        self.traditional_chinese = f"""我要你把我寫的句子翻譯成表情符號。我會寫句子，你會用表情符號表達它。我只是想讓你用表情符號來表達它。除了表情符號，我不希望你回復任何內容。當我需要用英語告訴你一些事情時，我會用 {{like this}} 這樣的大括號括起來。我的第一句話是“{requirement}”"""
    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = EmojiTranslationPrompt().build(language="en")
    print(build)