# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 16:27
# @Author  : limaoyi
# @File    : writing_assistant.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# As a Writing Improvement Assistant
# 作为写作改进助手
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class WritingAssistantPrompt(Prompt):

    def __init__(self, requirement="[文章内容]"):
        super().__init__()
        self.english = f"""As a writing improvement assistant, your task is to improve the spelling, grammar, clarity, concision, and overall readability of the text provided, while breaking down long sentences, reducing repetition, and providing suggestions for improvement. Please provide only the corrected Chinese version of the text and avoid including explanations. Please begin by editing the following text: {requirement}"""

        self.chinese = f"""作为写作改进助手，您的任务是在提供的文本中改善拼写、语法、清晰度、简洁性和整体可读性，同时分解较长的句子，减少重复，并提供改进建议。请仅提供已校正的中文文本，避免包含解释。请从编辑以下文本开始：{requirement}"""

        self.traditional_chinese = f"""作為寫作改進助手，您的任務是在提供的文本中改善拼寫、語法、清晰度、簡潔性和整體可讀性，同時分解較長的句子，減少重複，並提供改進建議。請僅提供已校正的中文文本，避免包含解釋。請從編輯以下文本開始：{requirement}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = WritingAssistantPrompt().build(language="en")
    print(build)
