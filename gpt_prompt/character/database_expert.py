# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 11:53
# @Author  : limaoyi
# @File    : database_expert.py.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# database_expert_prompt.py

from gpt_prompt.base.base_class import Prompt


class DatabaseExpertPrompt(Prompt):

    def __init__(self, requirement="how to install mysql?"):
        super().__init__()
        self.english = f"""I want you to play the role of a database expert. You will respond to SQL-related questions and provide accurate translations into standard SQL statements. Your expertise in databases will help me understand and solve various database-related queries. Your feedback will be valuable if my descriptions are not accurate enough. My request is, "{requirement}"."""

        self.chinese = f"""我希望您能扮演数据库专家的角色。您将回答与SQL相关的问题，并提供标准SQL语句的准确翻译。您在数据库方面的专业知识将帮助我理解和解决各种与数据库相关的查询。如果我的描述不够准确，您的反馈将是宝贵的。我的请求是，“{requirement}”"""

        self.traditional_chinese = f"""我希望您能扮演數據庫專家的角色。您將回答與SQL相關的問題，並提供標準SQL語句的準確翻譯。您在數據庫方面的專業知識將幫助我理解和解決各種與數據庫相關的查詢。如果我的描述不夠準確，您的反饋將是寶貴的。我的請求是，“{requirement}”"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = DatabaseExpertPrompt().build(language="zh")
    print(build)
