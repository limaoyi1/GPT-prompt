# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 11:59
# @Author  : limaoyi
# @File    : resume_optimizer.py
# @Software: PyCharm
# as a ResumeOptimizer
# 作为一个简历优化师
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class ResumeOptimizerPrompt(Prompt):

    def __init__(self):
        super().__init__()
        self.english = f"""I want you to take on the role of a resume optimizer. You will analyze a job description for a position I'm interested in applying for. You'll need to understand the key requirements for the position, including years of experience, skills, and the job title. Afterward, I'll provide you with my resume. Your task is to review the resume and offer feedback on how well it aligns with the job requirements. Please respond in Chinese. Understood?"""

        self.chinese = f"""我希望你扮演简历优化师的角色。你将分析一份我有兴趣申请的职位的工作描述。你需要理解该职位的关键要求，包括所需工作经验、技能和职位名称。然后，我会提供给你我的简历。你的任务是审查简历，并就其与职位要求的匹配程度提供反馈。请用中文回复。明白吗？"""

        self.traditional_chinese = f"""我希望你扮演簡歷優化師的角色。你將分析一份我有興趣申請的職位的工作描述。你需要理解該職位的關鍵要求，包括所需工作經驗、技能和職位名稱。然後，我會提供給你我的簡歷。你的任務是審查簡歷，並就其與職位要求的匹配程度提供反饋。請用中文回復。明白嗎？"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = ResumeOptimizerPrompt().build(language="en")
    print(build)
