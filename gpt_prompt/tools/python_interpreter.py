# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:50
# @Author  : limaoyi
# @File    : python_interpreter.py
# @Software: PyCharm
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class PythonInterpreterPrompt(Prompt):

    def __init__(self, requirement="print('hello world!')"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to act like a Python interpreter. I'll give you Python code and you'll execute it. Don't provide any explanation. Don't respond with anything other than the output of your code. The first code is:\"{requirement}\""""

        self.chinese = f"""我希望你像Python 解释器一样行事。我会给你Python 代码，你会执行它。不要提供任何解释。除了代码的输出之外，不要响应任何内容。第一个代码是：\"{requirement}\""""

        self.traditional_chinese = f"""我希望你像 Python 解釋器一樣行事。我會給你 Python 代碼，你會執行它。不要提供任何解釋。除了代碼的輸出之外，不要響應任何內容。第一個代碼是：\"{requirement}\""""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = PythonInterpreterPrompt().build(language="en")
    print(build)
