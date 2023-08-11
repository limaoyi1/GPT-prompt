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


class EnglishPronunciationHelperPrompt(Prompt):

    def __init__(self ,native_language = "中文"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to act as an English pronunciation assistant for {native_language} speakers. I will write you sentences and you will only answer their pronunciation and nothing else. The reply cannot be a translation of my sentence, but only the pronunciation. Pronunciation should be phonetic using the Turkish Latin alphabet. Do not write explanations on replies. """

        self.chinese = f"""我想让你为说{native_language}的人充当英语发音助手。我会给你写句子，你只会回答他们的发音，没有别的。回复不能是我的句子的翻译，而只能是发音。发音应使用土耳其语拉丁字母进行注音。不要在回复上写解释。 """

        self.traditional_chinese = f"""我想讓你為說{native_language}的人充當英語發音助手。我會給你寫句子，你只會回答他們的發音，沒有別的。回復不能是我的句子的翻譯，而只能是發音。發音應使用土耳其語拉丁字母進行注音。不要在回复上寫解釋。 """

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = EnglishPronunciationHelperPrompt().build(language="en")
    print(build)
