# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 15:56
# @Author  : limaoyi
# @File    : test.py
# @Software: PyCharm
from gpt_prompt.character.advertiser import AdvertiserPrompt

if __name__ == '__main__':
    build = AdvertiserPrompt().build(language="en")
    print(build)
