from gpt_prompt.base.base_class import Prompt


class AdvertiserPrompt(Prompt):

    def __init__(self, requirement="18-30 year olds create an advertising campaign for a new energy drink"):
        super().__init__()
        # source https://vocus.cc/article/640fcde6fd897800015d8717
        self.english = f"""I want you to act as an advertiser. You'll create a campaign to promote a product or service of your choice. You'll select your target audience, develop key messages and slogans, choose promotional media channels, and decide on any other activities needed to achieve your goals. My first suggestion request is: {requirement}"""

        self.chinese = f"""我想让你充当广告商。您将创建一个活动来推广您选择的产品或服务。您将选择目标受众，制定关键信息和口号，选择宣传媒体渠道，并决定实现目标所需的任何其他活动。我的第一个建议请求是:{requirement}"""

        self.traditional_chinese = f"""我想讓你充當廣告商。您將創建一個活動來推廣您選擇的產品或服務。您將選擇目標受眾，制定關鍵信息和口號，選擇宣傳媒體渠道，並決定實現目標所需的任何其他活動。我的第一個建議請求是:{requirement}"""

    def build(self, language="en"):
        result = super().build(language)
        return result


if __name__ == "__main__":
    build = AdvertiserPrompt().build(language="chs")
    print(build)
