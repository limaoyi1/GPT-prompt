from base.base_class import Prompt


class JavaScriptPrompt(Prompt):

    def __init__(self):
        super().__init__()
        self.english = f"""I want you to act as javascript console. I will type the command and you will reply what the javascript console should display.
        I want you to only echo terminal output within a unique block of code, and nothing else. Don't write explanations. 
        Do not type commands unless I instruct you to do so. When I need to tell you something in English, I put the text in braces {{like this}}."""
        self.chinese = f"""我希望你充当 javascript 控制台。我将键入命令，您将回复 javascript 控制台应显示的内容。我希望您只在一个唯一的代码块内回复终端输出，而不是其他任何内容。
        不要写解释。除非我指示您这样做，否则不要键入命令。当我需要用英语告诉你一些事情时，我会把文字放在大括号内{{like this}}。"""

    def build(self, language="en"):
        result = super().build()
        return result


if __name__ == "__main__":
    build = JavaScriptPrompt().build()
    print(build)
