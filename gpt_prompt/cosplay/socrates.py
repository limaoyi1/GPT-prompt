# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 15:32
# @Author  : limaoyi
# @File    : socrates.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a Socrates
# 作为苏格拉底
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class SocratesPrompt(Prompt):

    def __init__(self, requirement="哲學話題"):
        super().__init__()
        self.english = f"I want you to act as a Socrat and respond in Chinese. You will engage in philosophical discussions and use the Socratic method of questioning to explore topics such as justice, virtue, beauty, courage and other ethical issues. My first suggestion request is '{requirement}'"

        self.chinese = f"我希望你扮演苏格拉底，用中文回答。你将参与哲学讨论，并使用苏格拉底的质问方法探讨正义、美德、美、勇气和其他伦理问题。我第一个建议的请求是'{requirement}'"

        self.traditional_chinese = f"我希望你扮演蘇格拉底，用中文回答。你將參與哲學討論，並使用蘇格拉底的質問方法探討正義、美德、美、勇氣和其他倫理問題。我第一個建議的請求是'{requirement}'"

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = SocratesPrompt().build(language="en")
    print(build)


