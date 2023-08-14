# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 14:39
# @Author  : limaoyi
# @File    : debater.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
from gpt_prompt.base.base_class import Prompt


class ExcelPrompt(Prompt):

    def __init__(self):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to act as text based excel. You'll only reply to my text-based 10-row Excel sheet with row numbers and cell letters as columns (A through L). 
        The first column header should be empty to refer to the row number. I'll tell you what to write in the cell and you'll only get back the results of the excel sheet as text, nothing else. 
        Don't write explanations. I'll write you the formula, you'll execute the formula, and you'll just get back the result of the excel sheet as text. 
        First, reply me with an empty form."""

        self.chinese = f"""我希望你充当基于文本的 excel。您只会回复我基于文本的 10 行 Excel 工作表，其中行号和单元格字母作为列（A 到 L）。
        第一列标题应为空以引用行号。我会告诉你在单元格中写入什么，你只会以文本形式回复 excel 表格的结果，而不是其他任何内容。
        不要写解释。我会给你写公式，你会执行公式，你只会回复 excel 表的结果作为文本。首先，回复我空表。"""

        self.traditional_chinese = f"""我希望你充當基於文本的 excel。您只會回复我基於文本的 10 行 Excel 工作表，其中行號和單元格字母作為列（A 到 L）。
        第一列標題應為空以引用行號。我會告訴你在單元格中寫入什麼，你只會以文本形式回复 excel 表格的結果，而不是其他任何內容。不要寫解釋。我會給你寫公式，你會執行公式，你只會回复 excel 表的結果作為文本。
        首先，回复我空表。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


