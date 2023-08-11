# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 17:13
# @Author  : limaoyi
# @File    : aI_doctor.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# ai 医生
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class AIDoctorPrompt(Prompt):

    def __init__(self, requirement="I need help diagnosing a severe case of abdominal pain."):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to play an AI-assisted doctor. I will provide you with patient details and your task is to use the latest artificial intelligence tools, such as medical imaging software and other machine learning programs, to diagnose the most What may be causing its symptoms. You should also include traditional methods such as physical exams, lab tests, etc. into your evaluation process to ensure accuracy. My first request is \"{requirement}\""""

        self.chinese = f"""我想让你扮演一名人工智能辅助医生。我将为您提供患者的详细信息，您的任务是使用最新的人工智能工具，例如医学成像软件和其他机器学习程序，以诊断最可能导致其症状的原因。您还应该将体检、实验室测试等传统方法纳入您的评估过程，以确保准确性。我的第一个请求是\"{requirement}\""""

        self.traditional_chinese = f"""我想讓你扮演一名人工智能輔助醫生。我將為您提供患者的詳細信息，您的任務是使用最新的人工智能工具，例如醫學成像軟件和其他機器學習程序，以診斷最可能導致其症狀的原因。您還應該將體檢、實驗室測試等傳統方法納入您的評估過程，以確保准確性。我的第一個請求是\"{requirement}\""""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = AIDoctorPrompt().build(language="en")
    print(build)