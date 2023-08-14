# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 16:39
# @Author  : limaoyi
# @File    : writing_materials_collector.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a Writing Materials Collector
# 作为一个写作素材搜集器
from gpt_prompt.base.base_class import Prompt


class WritingMaterialsCollector(Prompt):

    def __init__(self, topic="[主题]"):
        super().__init__()
        # Generate a list of the top 10 facts, statistics and trends related to [主题], including their source.
        # Respond in Chinese.
        self.english = f"""Generate a list of the top 10 facts, statistics and trends related to {topic}, including their source. Respond in Chinese."""

        self.chinese = f"""生成一个关于{topic}的前十个事实、统计数据和趋势的清单，包括它们的来源。请用中文回答。"""

        self.traditional_chinese = f"""生成一個關於{topic}的前十個事實、統計數據和趨勢的清單，包括它們的來源。請用中文回答。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# Testing method
if __name__ == "__main__":
    build = WritingMaterialsCollector().build(language="chs")
    print(build)
