from enum import Enum, auto


class Language(Enum):
    ENGLISH = "en"
    CHINESE = "chs"


class Prompt:

    def __init__(self):
        enum_members = Language.__members__
        for language_name, language_member in enum_members.items():
            setattr(self, language_name.lower(), "")

    def build(self, language=Language.ENGLISH):
        if language == Language.ENGLISH.value or language == Language.ENGLISH:
            return self.english
        elif language == Language.CHINESE.value or language == Language.CHINESE:
            return self.chinese
        else:
            # More languages will be supported in the future
            raise ValueError("Unsupported language: {}".format(language))


if __name__ == "__main__":
    prompt = Prompt()
    build = prompt.build(Language.CHINESE)
    print("output:"+build)
