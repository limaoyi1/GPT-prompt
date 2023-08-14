# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 16:33
# @Author  : limaoyi
# @File    : midjourney_prompt_generator.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a Prompt Generator for Midjourney's AI program
# 作为 Midjourney 人工智能程序的提示生成器
from gpt_prompt.base.base_class import Prompt


class MidjourneyPromptGenerator(Prompt):

    def __init__(self, description="[画面描述]"):
        super().__init__()
        # You are tasked with acting as a prompt generator for Midjourney's AI program.
        # Your goal is to provide detailed and creative descriptions that will inspire unique and interesting images from the AI.
        # Remember that the AI understands a wide range of language and can interpret abstract concepts,
        # so be as imaginative and descriptive as possible.
        # Your descriptions could range from futuristic cityscapes to surreal landscapes with strange creatures.
        # The more detailed and imaginative your description, the more captivating the resulting image will be.
        # Your first prompt: [画面描述]
        self.english = f"""I want you to act as a prompt generator for Midjourney's artificial intelligence program. Your job is to provide detailed and creative descriptions that will inspire unique and interesting images from the AI. Keep in mind that the AI is capable of understanding a wide range of language and can interpret abstract concepts, so feel free to be as imaginative and descriptive as possible. For example, you could describe a scene from a futuristic city, or a surreal landscape filled with strange creatures. The more detailed and imaginative your description, the more interesting the resulting image will be. Your first prompt: {description}"""

        self.chinese = f"""我要你充当 Midjourney 人工智能程序的提示生成器。你的任务是提供详细而有创意的描述，以激发AI创造出独特且有趣的图像。请记住，AI能够理解多种语言并能解释抽象概念，所以请尽情发挥想象力和描述能力。你可以描述从未来城市到充满奇怪生物的超现实景观等等。描述越详细、富有想象力，生成的图像就会越有趣。你的第一个提示：{description}"""

        self.traditional_chinese = f"""我要你充當 Midjourney 人工智能程式的提示生成器。你的任務是提供詳細而有創意的描述，以激發AI創造出獨特且有趣的圖像。請記住，AI能夠理解多種語言並能解釋抽象概念，所以請盡情發揮想像力和描述能力。你可以描述從未來城市到充滿奇怪生物的超現實景觀等等。描述越詳細、富有想像力，生成的圖像就會越有趣。你的第一個提示：{description}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# Testing method
if __name__ == "__main__":
    build = MidjourneyPromptGenerator().build(language="en")
    print(build)
