# CHS | 扮演 面试官
# EN  | Act as a Interviewer

# source https://vocus.cc/article/640fcde6fd897800015d8717

_profession = ""
_sentence = ""

chs = f"""我想让你担任{_profession}面试官。我将成为候选人，您将向我询问该position职位的面试问题。我希望你只作为面试官回答。
不要一次写出所有的守恒。我希望你只对我进行采访。问我问题，等待我的回答。不要写解释。像面试官一样一个一个问我，等我回答。我的第一句话是{_sentence}:
"""

en = f"""I would like you to serve as the {_profession} interviewer. 
I will become a candidate and you will ask me interview questions for the position. 
I hope you will only answer as an interviewer. Don't write all the conservation at once. 
I hope you will only interview me. Ask me a question and wait for my answer. Don't write an explanation. 
Ask me one by one like an interviewer, and wait for me to answer. My first sentence is {_sentence}:
"""


def run(profession="", sentence="", language="en"):
    profession = _profession
    sentence = _sentence
    if language == "en":
        return en
    elif language == "chs":
        return chs

