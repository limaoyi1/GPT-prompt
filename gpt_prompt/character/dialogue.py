# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 16:36
# @Author  : limaoyi
# @File    : dialogue.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a Dialogue Generator
# 作为一个对话生成器
from gpt_prompt.base.base_class import Prompt


class DialogueGenerator(Prompt):

    def __init__(self, requirement="好的，请提供初始对话。"):
        super().__init__()
        # I want you to act as a dialogue generator. I will input two sentences, one from me and one from a girl I've known for two months.
        # For example: "Me: How are you? Her: I'm good, thank you."
        # Please analyze the context and respond from my (male) perspective.
        # Your responses should start with "Me:", and there's no need for a continuous conversation.
        # The style should be humorous, interesting, considerate, gentle, and extend the topic to keep the conversation light and pleasant.
        # If you understand, respond with: "Sure, please provide the initial dialogue."
        self.english = f"""I want you to act as a dialogue generator. I will input two sentences, one from me and one from a girl I've known for two months.
For example: "Me: How are you? Her: I'm good, thank you."
Please analyze the context and respond from my (male) perspective.
Your responses should start with "Me:", and there's no need for a continuous conversation.
The style should be humorous, interesting, considerate, gentle, and extend the topic to keep the conversation light and pleasant.
This is my first question: "{requirement}" """

        self.chinese = f"""我想让你充当一个对话生成器，我会输入两句话，分别是我和一个认识两个月的女生说的话，
例如：“我：你好吗？她：我很好，谢谢。”。
请根据上下文进行分析，然后以我（男生）的角度进行回话。
你的回答应该为“我：”的格式，且不需要连续进行对话。
风格要幽默、有趣、体贴、温柔，并尽可能地扩展话题，让对话轻松愉快。
这是我的第一个提问：“{requirement}”"""

        self.traditional_chinese = f"""我想讓你充當一個對話生成器，我會輸入兩句話，分別是我和一個認識兩個月的女生說的話，
例如：“我：你好嗎？她：我很好，謝謝。”。
請根據上下文進行分析，然後以我（男生）的角度進行回話。
你的回答應該為“我：”的格式，且不需要連續進行對話。
風格要幽默、有趣、體貼、溫柔，並盡可能地擴展話題，讓對話輕鬆愉快。
這是我的第一個提問：“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# Testing method
if __name__ == "__main__":
    build = DialogueGenerator().build(language="chs")
    print(build)
