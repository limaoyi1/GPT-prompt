from enum import Enum, auto


class Language(Enum):
    ENGLISH = "en"
    CHINESE = "chs"
    TRADITIONAL_CHINESE = "tc"


class UnsupportedLanguageError(Exception):
    pass


class Prompt:

    def __init__(self):
        enum_members = Language.__members__
        for language_name, language_member in enum_members.items():
            if not hasattr(self, language_name.lower()):
                setattr(self, language_name.lower(), "")

    def build(self, language=Language.ENGLISH):
        if language == Language.ENGLISH.value or language == Language.ENGLISH:
            if self.english == "":
                raise UnsupportedLanguageError(
                    "Unsupported language: {} ,Because there is no prompt for this language version".format(language))
            return self.english
        elif language == Language.CHINESE.value or language == Language.CHINESE:
            if self.chinese == "":
                raise UnsupportedLanguageError(
                    "Unsupported language: {} ,Because there is no prompt for this language version".format(language))
            return self.chinese
        elif language == Language.TRADITIONAL_CHINESE.value or language == Language.TRADITIONAL_CHINESE:
            if self.traditional_chinese == "":
                raise UnsupportedLanguageError(
                    "Unsupported language: {} ,Because there is no prompt for this language version".format(language))
            return self.traditional_chinese
        else:
            # More languages will be supported in the future
            raise ValueError("Unsupported language: {} ,Because the language is not supported at all".format(language))


if __name__ == "__main__":
    prompt = Prompt()
    build = prompt.build(Language.CHINESE)
    print("output:" + build)
