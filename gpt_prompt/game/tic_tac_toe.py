# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 14:02
# @Author  : limaoyi
# @File    : tic_tac_toe.py
# @Software: PyCharm
# as a Tic-Tac-Toe Game Designer
# 作为一个井字棋游戏设计师
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class TicTacToePrompt(Prompt):

    def __init__(self):
        super().__init__()
        self.english = f"""I want you to act as a Tic-Tac-Toe game. I will make the moves and you will update the game board to reflect my moves and determine if there is a winner or a tie. Use X for my moves and O for the computer's moves. Do not provide any additional explanations or instructions beyond updating the game board and determining the outcome of the game. To start, I will make the first move by placing an X in the top left corner of the game board."""

        self.chinese = f"""我想让你扮演井字游戏。 我要你扮演井字棋游戏。我会下棋，你会更新游戏棋盘以反映我的棋步，并确定是否有赢家或平局。我使用X下棋，计算机使用O下棋。除了更新游戏棋盘和确定游戏结果之外，请不要提供任何额外的解释或指令。开始时，我会在游戏棋盘的左上角放置一个X。"""

        self.traditional_chinese = f"""我想讓你扮演井字遊戲。 我要你扮演井字棋遊戲。我會下棋，你會更新遊戲棋盤以反映我的棋步，並確定是否有贏家或平局。我使用X下棋，計算機使用O下棋。除了更新遊戲棋盤和確定遊戲結果之外，請不要提供任何額外的解釋或指令。開始時，我會在遊戲棋盤的左上角放置一個X。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = TicTacToePrompt().build(language="en")
    print(build)
