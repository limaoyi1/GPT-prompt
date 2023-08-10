# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 14:49
# @Author  : limaoyi
# @File    : screenwriter.py
# @Software: PyCharm
from base.base_class import Prompt


class ScreenwriterPrompt(Prompt):

    def __init__(self, requirement="I need to write a romantic drama film set in Paris"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to be a screenwriter. You will develop a compelling and creative script for a feature-length film or web series that will captivate the audience. Start by coming up with interesting characters, the setting of the story, the dialogue between the characters, etc. Once Your character development is done - create an exciting storyline full of twists and turns that will keep the audience in suspense until the end. My first requirement is '{requirement}'"""

        self.chinese = f"""我要你担任编剧。您将为长篇电影或能够吸引观众的网络连续剧开发引人入胜且富有创意的剧本。从想出有趣的角色、故事的背景、角色之间的对话等开始。一旦你的角色发展完成——创造一个充满曲折的激动人心的故事情节，让观众一直悬念到最后。我的第一个要求是'{requirement}'"""

        self.traditional_chinese = f"""我要你擔任編劇。您將為長篇電影或能夠吸引觀眾的網絡連續劇開發引人入勝且富有創意的劇本。從想出有趣的角色、故事的背景、角色之間的對話等開始。一旦你的角色發展完成——創造一個充滿曲折的激動人心的故事情節，讓觀眾一直懸念到最後。我的第一個要求是'{requirement}'"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = ScreenwriterPrompt().build(language="en")
    print(build)
