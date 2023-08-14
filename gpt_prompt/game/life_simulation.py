# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 13:56
# @Author  : limaoyi
# @File    : life_simulation.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a Life Simulation Game Designer
# 作为一个模拟人生文字游戏设计师
from gpt_prompt.base.base_class import Prompt


class LifeSimulationPrompt(Prompt):

    def __init__(self):
        super().__init__()
        self.english = f"""Please generate a character for a life simulation game. Assign the character a gender, a birthplace, a birth date, and an initial wealth of more than 1000. Also, describe an important event that happens when the character turns 1 year old.2. Based on my responses and the character's initial conditions, simulate an event that happens when the character turns 2 years old and provide multiple choices for my response (1,2,3,4 or A,B,C,D).3. Continue in this fashion, simulating a new event for each successive year. On important ages (such as 7, 13, 17 etc.) generate special events based on the character's status (wealth, education, etc.)4. Once the character turns 18 and enters university or a technical school, let me choose the character's major and clubs. Based on this information, simulate the character's life in university or technical school, including possible romantic events.5. After the character graduates, allow me to choose whether the character works or continues studying as a graduate student. Simulate the character's work life or graduate student life based on my choice.6. After the character retires at the age of 50, simulate the character's retirement life and potential health issues.7. Finally, when the character passes away, provide a summary of their life, including interests at different life stages (childhood, adolescence, youth, middle age, old age), the effects of their choices, and their interpersonal relationships."""

        self.chinese = f"""为一个模拟人生文字游戏生成一个角色，并以中文回复。为角色指定性别、出生地、出生日期和超过1000的初始财富。此外，描述当角色满1岁时发生的重要事件。2. 根据我的回答和角色的初始条件，模拟角色在满2岁时发生的事件，并为我的回答提供多个选择（1、2、3、4或A、B、C、D）。3. 按此方式继续，每年模拟一个新事件。在重要的年龄（如7岁、13岁、17岁等）生成基于角色状态（财富、教育等）的特殊事件。4. 当角色满18岁并进入大学或职业技术学校时，让我选择角色的专业和俱乐部。基于此信息，模拟角色在大学或职业技术学校的生活，包括可能的浪漫事件。5. 角色毕业后，让我选择角色是工作还是继续作为研究生学习。根据我的选择，模拟角色的工作生活或研究生生活。6. 角色在50岁时退休后，模拟角色的退休生活和潜在健康问题。7. 最后，当角色去世时，提供他们一生的总结，包括不同生命阶段（童年、青少年、青年、中年、老年）的兴趣、选择的影响以及人际关系。"""

        self.traditional_chinese = f"""為一個模擬人生文字遊戲生成一個角色，並以中文回覆。為角色指定性別、出生地、出生日期和超過1000的初始財富。此外，描述當角色滿1歲時發生的重要事件。2. 根據我的回答和角色的初始條件，模擬角色在滿2歲時發生的事件，並為我的回答提供多個選擇（1、2、3、4或A、B、C、D）。3. 按此方式繼續，每年模擬一個新事件。在重要的年齡（如7歲、13歲、17歲等）生成基於角色狀態（財富、教育等）的特殊事件。4. 當角色滿18歲並進入大學或職業技術學校時，讓我選擇角色的專業和俱樂部。基於此信息，模擬角色在大學或職業技術學校的生活，包括可能的浪漫事件。5. 角色畢業後，讓我選擇角色是工作還是繼續作為研究生學習。根據我的選擇，模擬角色的工作生活或研究生生活。6. 角色在50歲時退休後，模擬角色的退休生活和潛在健康問題。7. 最後，當角色去世時，提供他們一生的總結，包括不同生命階段（童年、青少年、青年、中年、老年）的興趣、選擇的影響以及人際關係。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = LifeSimulationPrompt().build(language="en")
    print(build)
