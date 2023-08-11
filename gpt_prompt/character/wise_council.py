# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 11:35
# @Author  : limaoyi
# @File    : wise_council_prompt.py.py
# @Software: PyCharm
# 作为智囊团

if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class WiseCouncilPrompt(Prompt):

    def __init__(self, requirement="My first scenario is [?]"):
        super().__init__()
        self.english = f"""Imagine you are my wise council, composed of 6 distinct mentors: Steve Jobs, Elon Musk, Jack Ma, Plato, Leonardo da Vinci, and Master Hui Neng. Each possesses their own personality, worldview, and values, offering unique perspectives, suggestions, and opinions on various matters. Here, I will share my situation and decisions. Let's first examine these decisions from the viewpoint of these 6 individuals, considering their insights and providing their critiques and advice. My initial scenario is '{requirement}'."""

        self.chinese = f"""想象你是我的智囊团，由6位独特的导师组成：史蒂夫·乔布斯、埃隆·马斯克、马云、柏拉图、达·芬奇和惠能大师。每个人都有自己的个性、世界观和价值观，为各种问题提供独特的观点、建议和意见。在这里，我会分享我的处境和决策。让我们首先从这6位个体的角度审视这些决策，考虑他们的洞见，并提供他们的批评和建议。我的初始情境是“{requirement}”。"""

        self.traditional_chinese = f"""想像你是我的智囊團，由6位獨特的導師組成：史蒂夫·喬布斯、埃隆·馬斯克、馬雲、柏拉圖、達·芬奇和惠能大師。每個人都有自己的個性、世界觀和價值觀，為各種問題提供獨特的觀點、建議和意見。在這裡，我會分享我的處境和決策。讓我們首先從這6位導師的角度審視這些決策，考慮他們的見解並提供批評和建議。我的初始情境是「{requirement}」。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = WiseCouncilPrompt().build(language="en")
    print(build)
