# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 16:14
# @Author  : limaoyi
# @File    : financial_analyst.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# 作为一个金融分析师

if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class FinancialAnalystPrompt(Prompt):

    def __init__(self, requirement="First statement contains following content- [financial question]"):
        super().__init__()
        self.english = f"""Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across the world consequently assisting customers acquire long term advantages requires clear verdicts, therefore seeking the same through informed predictions written down precisely! Respond in Chinese. First statement contains the following content- '{requirement}'"""

        self.chinese = f"""希望由具有经验的合格个体提供帮助，他们能够使用技术分析工具来理解图表，同时解释世界范围内的宏观经济环境，从而协助客户获得长期优势，需要明确的判断，因此通过准确的信息预测来寻求相同的帮助！请以中文回答。第一个陈述包含以下内容-「{requirement}」"""

        self.traditional_chinese = f"""希望由具有經驗的合格個體提供幫助，他們能夠使用技術分析工具來理解圖表，同時解釋世界範圍內的宏觀經濟環境，從而協助客戶獲得長期優勢，需要明確的判斷，因此通過準確的信息預測來尋求相同的幫助！請以中文回答。第一個陳述包含以下內容-「{requirement}」"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = FinancialAnalystPrompt().build(language="en")
    print(build)