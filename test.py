# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 15:56
# @Author  : limaoyi
# @File    : test.py
# @Software: PyCharm
from gpt_prompt.tools.excel import ExcelPrompt

if __name__ == '__main__':
    build = ExcelPrompt().build(language="chs")
    print(build)
