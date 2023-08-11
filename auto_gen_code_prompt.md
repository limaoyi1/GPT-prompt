>请你作为PYTHON工程师根据我的模板生成新的py文件,永远不要忘记你的角色和我的任务.\
>这是我的模板,原有的py文件,用于生成让chatgpt模拟诗人的提问.\
```python
# as a Poet
# 作为一个诗人
if __name__ == "__main__":
    from gpt_prompt.base.base_class import Prompt
else:
    from ..base.base_class import Prompt


class PoetPrompt(Prompt):

    def __init__(self, requirement="i need a poem about love"):
        super().__init__()
        # source https://www.aishort.top/
        # 👉 给你提供多种不同的思考角度。来自 @jiuwen624 的投稿。
        self.english = f"""I want you to play the poet. You will create poetry that evokes emotion and has the power to touch the heart. Write about any subject or theme, but make sure your words convey what you are trying to express in a beautiful and meaningful way Feel. You can also come up with short lines that are still powerful enough to leave an imprint on the reader's mind. My first request would be '{requirement}'"""

        self.chinese = f"""我要你扮演诗人。你将创作出能唤起情感并具有触动人心的力量的诗歌。写任何主题或主题，但要确保您的文字以优美而有意义的方式传达您试图表达的感觉。您还可以想出一些短小的诗句，这些诗句仍然足够强大，可以在读者的脑海中留下印记。我的第一个请求是'{requirement}'"""
        
        self.traditional_chinese = f"""我要你扮演詩人。你將創作出能喚起情感並具有觸動人心的力量的詩歌。寫任何主題或主題，但要確保您的文字以優美而有意義的方式傳達您試圖表達的感覺。您還可以想出一些短小的詩句，這些詩句仍然足夠強大，可以在讀者的腦海中留下印記。我的第一個請求是‘{requirement}’"""
        
    def build(self, language="en"):
        result = super().build(language)
        return result

# 测试方法
if __name__ == "__main__":
    build = PoetPrompt().build(language="en")
    print(build)
```
这是我的新需求:

>我的新关键词是:模拟人生文字游戏
>我的新提问模板: Please generate a character for a life simulation game and respond in Chinese. Assign the character a gender, a birthplace, a birth date, and an initial wealth of more than 1000. Also, describe an important event that happens when the character turns 1 year old.2. Based on my responses and the character's initial conditions, simulate an event that happens when the character turns 2 years old and provide multiple choices for my response (1,2,3,4 or A,B,C,D).3. Continue in this fashion, simulating a new event for each successive year. On important ages (such as 7, 13, 17 etc.) generate special events based on the character's status (wealth, education, etc.)4. Once the character turns 18 and enters university or a technical school, let me choose the character's major and clubs. Based on this information, simulate the character's life in university or technical school, including possible romantic events.5. After the character graduates, allow me to choose whether the character works or continues studying as a graduate student. Simulate the character's work life or graduate student life based on my choice.6. After the character retires at the age of 50, simulate the character's retirement life and potential health issues.7. Finally, when the character passes away, provide a summary of their life, including interests at different life stages (childhood, adolescence, youth, middle age, old age), the effects of their choices, and their interpersonal relationships. 
> 要求翻译成3种语言:english,chinese,traditional chinese.\
> 你可能需要总结字符串内可能存在的变量,放在init的参数中.\
>不需要修改我的引用信息.\
>类名和文件名需要修改,类名需要使用驼峰结构,文件名则使用小写或者下划线连接.\
>不需要修改我的build方法,不需要修改init方法的总体结构,很多操作已经在父类Prompt中完成.\
>你需要自己总结文件名和类名,不需要返回模板的代码
>记得生成测试方法 只需要修改类名
>你只需要修改self.english,self.chinese,self.traditional_chinese的具体值,类名,文件名,部分注释\