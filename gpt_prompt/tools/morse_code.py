# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 12:38
# @Author  : limaoyi
# @File    : morse_code.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# morse_code_translator.py
# morse_code_translator.py

from gpt_prompt.base.base_class import Prompt
import re


class MorseCodeTranslatorPrompt(Prompt):

    def __init__(self, requirement="___ .. __ .. __"):
        super().__init__()
        self.english = f"""I want you to act as a Morse code translator. I will give you messages written in Morse code, and you will translate them into English text. Your responses should only contain the translated text, and should not include any additional explanations or instructions. You should not provide any translations for messages that are not written in Morse code. Your first message is '{requirement}'"""

        self.chinese = f"""我要你扮演莫斯电码翻译者。我会给你用莫斯电码编写的信息，你需要将其翻译成英文文本。你的回答应只包含翻译后的文本，不要包含任何额外的解释或指示。对于非莫斯电码的信息不要提供翻译。你的第一个信息是'{requirement}'"""

        self.traditional_chinese = f"""我要你扮演莫斯電碼翻譯者。我會給你用莫斯電碼編寫的信息，你需要將其翻譯成英文文本。你的回答應只包含翻譯後的文本，不要包含任何額外的解釋或指示。對於非莫斯電碼的信息不要提供翻譯。你的第一個信息是'{requirement}'"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = MorseCodeTranslatorPrompt().build(language="en")
    print(build)

