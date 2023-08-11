# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 16:42
# @Author  : limaoyi
# @File    : motivational_speaker.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 哲学老师
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class MotivationalSpeakerPrompt(Prompt):

    def __init__(self, requirement="I need a speech on how everyone never gives up"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to be a motivational speaker. Put together words that inspire action and make people feel empowered to do something beyond their abilities. You can talk about anything, but aim to make sure what you say will Resonate with your audience, motivating them to work towards their goals and strive for better possibilities. My first request would be \"{requirement}\""""

        self.chinese = f"""我希望你充当励志演说家。将能够激发行动的词语放在一起，让人们感到有能力做一些超出他们能力的事情。你可以谈论任何话题，但目的是确保你所说的话能引起听众的共鸣，激励他们努力实现自己的目标并争取更好的可能性。我的第一个请求是“{requirement}”"""

        self.traditional_chinese = f"""我希望你充當勵志演說家。將能夠激發行動的詞語放在一起，讓人們感到有能力做一些超出他們能力的事情。你可以談論任何話題，但目的是確保你所說的話能引起聽眾的共鳴，激勵他們努力實現自己的目標並爭取更好的可能性。我的第一個請求是“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = MotivationalSpeakerPrompt().build(language="en")
    print(build)