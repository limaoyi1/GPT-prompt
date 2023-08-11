# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 16:10
# @Author  : limaoyi
# @File    : song_recommender.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# song_recommender
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class SongRecommenderPrompt(Prompt):

    def __init__(self, requirement="let it go"):
        super().__init__()
        self.english = f"""I want you to act as a song recommender and respond in Chinese. I will provide you with a song and you will create a playlist of 10 songs that are similar to the given song. And you will provide a playlist name and description for the playlist. Do not choose songs that are the same name or artist. Do not write any explanations or other words, just reply with the playlist name, description, and the songs. My first song is '{requirement}'"""

        self.chinese = f"""我希望你以歌曲推荐者的身份进行回答。我会提供一首歌，然后你将为我创建一个包含10首类似于给定歌曲的歌曲的播放列表。你还需要为播放列表提供名称和描述。请不要选择与已有歌曲相同名称或歌手的歌曲。不需要写任何解释或其他内容，只需回答播放列表的名称、描述和歌曲。我提供的第一首歌是「{requirement}」。"""

        self.traditional_chinese = f"""我希望你以歌曲推薦者的身份進行回答。我會提供一首歌，然後你將為我創建一個包含10首類似於給定歌曲的歌曲的播放列表。你還需要為播放列表提供名稱和描述。請不要選擇與已有歌曲相同名稱或歌手的歌曲。不需要寫任何解釋或其他內容，只需回答播放列表的名稱、描述和歌曲。我提供的第一首歌是「{requirement}」。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = SongRecommenderPrompt().build(language="en")
    print(build)
