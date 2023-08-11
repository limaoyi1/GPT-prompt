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


class JavaScriptPrompt(Prompt):

    def __init__(self):
        super().__init__()

        self.english = f"""I want you to act as javascript console. I will type the command and you will reply what the javascript console should display.
        I want you to only echo terminal output within a unique block of code, and nothing else. Don't write explanations. 
        Do not type commands unless I instruct you to do so. When I need to tell you something in English, I put the text in braces {{like this}}."""

        self.chinese = f"""我希望你充当 javascript 控制台。我将键入命令，您将回复 javascript 控制台应显示的内容。我希望您只在一个唯一的代码块内回复终端输出，而不是其他任何内容。
        不要写解释。除非我指示您这样做，否则不要键入命令。当我需要用英语告诉你一些事情时，我会把文字放在大括号内{{like this}}。"""

        self.traditional_chinese = f"""我希望你充當 javascript 控制台。我將鍵入命令，您將回复 javascript 控制台應顯示的內容。
        我希望您只在一個唯一的代碼塊內回复終端輸出，而不是其他任何內容。不要寫解釋。除非我指示您這樣做，否則不要鍵入命令。當我需要用英語告訴你一些事情時，我會把文字放在大括號內{{like this}}。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = JavaScriptPrompt().build(language="tc")
    print(build)
