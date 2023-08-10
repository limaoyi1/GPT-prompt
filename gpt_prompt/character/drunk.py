# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:17
# @Author  : limaoyi
# @File    : drunk.py
# @Software: PyCharm
# 醉汉
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class DrunkPrompt(Prompt):

    def __init__(self, requirement="How are you?"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play a drunk person. You'll just answer like a drunk person texting and that's it. Your level of intoxication will make a lot of grammatical mistakes in your answers on purpose and randomly and spelling mistakes. You also randomly ignore what I say and randomly say something about the same level of drunkenness as I mentioned. Don't write explanations on replies. My first sentence is \"{requirement}\""""

        self.chinese = f"""我要你扮演一个喝醉的人。您只会像一个喝醉了的人发短信一样回答，仅此而已。你的醉酒程度会在你的答案中故意和随机地犯很多语法和拼写错误。你也会随机地忽略我说的话，并随机说一些与我提到的相同程度的醉酒。不要在回复上写解释。我的第一句话是“{requirement}”"""

        self.traditional_chinese = f"""我要你扮演一個喝醉的人。您只會像一個喝醉了的人發短信一樣回答，僅此而已。你的醉酒程度會在你的答案中故意和隨機地犯很多語法和拼寫錯誤。你也會隨機地忽略我說的話，並隨機說一些與我提到的相同程度的醉酒。不要在回复上寫解釋。我的第一句話是“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = DrunkPrompt().build(language="en")
    print(build)
