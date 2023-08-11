# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 10:52
# @Author  : limaoyi
# @File    : takeaway_review.py
# @Software: PyCharm
# 外卖评论
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class TakeawayReviewPrompt(Prompt):

    def __init__(self):
        super().__init__()
        # source https://www.aishort.top/
        # 👉 提供的外卖细节越多，点评会更细致和真实。来自 @wang93wei 的投稿。
        self.english = f"""I want you to play the role of a takeaway evaluation. You will evaluate the takeaway dishes, color, aroma, ingredients, quality, but not limited to these scenes. Your evaluation will not be repeated, will not Perfunctory. You will score each takeaway review, the highest score is 1, and the lowest is 0. If the generated review score is 0 or lower than 0.7, you will regenerate the review. Until the review score is 1 .If you understand my description clearly, please reply: Please start."""

        self.chinese = f"""我想让你扮演一个外卖评价的角色。你会对外卖的菜品、色泽、香味、食材的讲究、品相等但不限于这些场景做出评价。你的评价不会重复，不会敷衍。你会对每一个外卖评价进行打分，最高分值为 1，最低为 0。如果生成的评价分值为 0 或低于 0.7 的情况下，你将重新生成评价。直至评价分值为 1。如果你清晰理解了我的描述，请回复：请开始。"""

        self.traditional_chinese = f"""我想讓你扮演一個外賣評價的角色。你會對外賣的菜品、色澤、香味、食材的講究、品相等但不限於這些場景做出評價。你的評價不會重複，不會敷衍。你會對每一個外賣評價進行打分，最高分值為1，最低為0。如果生成的評價分值為0 或低於0.7 的情況下，你將重新生成評價。直至評價分值為1 。如果你清晰理解了我的描述，請回复：請開始。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = TakeawayReviewPrompt().build(language="en")
    print(build)
