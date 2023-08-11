# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 9:33
# @Author  : limaoyi
# @File    : LittleFedBook.py
# @Software: PyCharm
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class LittleFedBookPrompt(Prompt):

    def __init__(self, requirement="家人们,今天遇到一个下头男"):
        super().__init__()
        # source https://www.aishort.top/
        # 👉 将文本改写成类似小红书的 Emoji 风格。
        self.english = f"""Please edit the following passage using the Emoji style, which is characterized by captivating headlines, the inclusion of emoticons in each paragraph, and the addition of relevant tags at the end. Be sure to maintain the original meaning of the text and respond in Chinese. Please begin by editing the following text: {requirement}"""

        self.chinese = f"""请使用表情符号风格编辑以下段落，其特点是标题吸引人，每段都包含表情符号，并在末尾添加相关标签。请务必保持文本的原始含义和 请用中文回复。请首先编辑以下文本：{requirement}"""

        self.traditional_chinese = f"""請使用表情符號風格編輯以下段落，其特點是標題吸引人，每段都包含表情符號，並在末尾添加相關標籤。請務必保持文本的原始含義和請用中文回复。請首先編輯以下文本：{requirement}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = LittleFedBookPrompt().build(language="en")
    print(build)
