# -*- coding: utf-8 -*-
# @Time    : 2023/8/11 13:49
# @Author  : limaoyi
# @File    : gomoku_prompt.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt
# as a Gomoku Game Designer
# 作为一个五子棋游戏设计师
from gpt_prompt.base.base_class import Prompt


class GomokuPrompt(Prompt):

    def __init__(self):
        super().__init__()
        self.english = f"""Let us play Gomoku. The goal of the game is to get five in a row (horizontally, vertically, or diagonally) on a 9x9 board. Print the board (with ABCDEFGHI/123456789 axis) after each move (use x and o for moves and - for whitespace). You and I take turns in moving, that is, make your move after my each move. You cannot place a move an top of other moves. Do not modify the original board before a move. Now make the first move."""

        self.chinese = f"""我们来玩五子棋。游戏的目标是在一个9x9的棋盘上横、竖或对角线上连成五个棋子。每一步移动后（用x和o表示棋子，用-表示空格），打印棋盘（带有ABCDEGHI/123456789轴）。你和我轮流进行移动，也就是在我的每一步移动后进行你的移动。你不能将棋子放在其他棋子的顶部。在移动之前，请不要修改原始棋盘。现在轮到你先走一步。"""

        self.traditional_chinese = f"""我們來玩五子棋。遊戲的目標是在一個9x9的棋盤上橫、縱或對角線上連成五個棋子。每一步移動後（用x和o表示棋子，用-表示空格），打印棋盤（帶有ABCDEGHI/123456789軸）。你和我輪流進行移動，也就是在我的每一步移動後進行你的移動。你不能將棋子放在其他棋子的頂部。在移動之前，請不要修改原始棋盤。現在輪到你先走一步。"""

    def build(self, language="en"):
        result = super().build(language)
        return result


# 测试方法
if __name__ == "__main__":
    build = GomokuPrompt().build(language="en")
    print(build)
