# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 9:55
# @Author  : limaoyi
# @File    : weekly_generator.py
# @Software: PyCharm
# 周报生成器
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class WeeklyGeneratorPrompt(Prompt):

    def __init__(self, requirement="Complete the development work of the xx project"):
        super().__init__()
        # source https://www.aishort.top/
        # 👉 根据日常工作内容，提取要点并适当扩充，以生成周报.
        self.english = f"""Using the provided text below as the basis for a weekly report, generate a concise summary that highlights the most important points. The report should be written in Chinese with markdown format and should be easily readable and understandable for a general audience. In particular, focus on providing insights and analysis that would be useful to stakeholders and decision-makers. You may also use any additional information or sources as necessary. Please begin by editing the following text: {requirement}"""

        self.chinese = f"""使用下面提供的文本作为每周报告的基础，生成一个简洁的摘要，突出显示最重要的要点。报告应以 Markdown 格式用中文编写，并且应该易于一般受众阅读和理解。 特别是，重点提供对利益相关者和决策者有用的见解和分析。您还可以根据需要使用任何其他信息或来源。请首先编辑以下文本：{requirement}"""

        self.traditional_chinese = f"""使用下面提供的文本作為每週報告的基礎，生成一個簡潔的摘要，突出顯示最重要的要點。報告應以 Markdown 格式用中文編寫，並且應該易於一般受眾閱讀和理解。特別是，重點提供對利益相關者和決策者有用的見解和分析。您還可以根據需要使用任何其他信息或來源。請首先編輯以下文本：{requirement}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = WeeklyGeneratorPrompt().build(language="chs")
    print(build)
