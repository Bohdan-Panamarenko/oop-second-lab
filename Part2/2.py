from typing import List

class ReadTextFile:
    """
    This class contains functionality to open text files and determine number of chars, words and sentences in it.
    Single instance contains only path to file
    """
    def __init__(self, path: str):
        self.path = path

    def calc(self):
        f = open(self.path, 'r')
        text = f.read()
        f.close()

        charsNum = len(text)

        words = text.split()
        wordsNum = len(words)
        if self._last_is_empty(words):
            wordsNum -= 1

        text = text.replace("!", ".")
        text = text.replace("?", ".")
        sentences = text.split(".")
        sentencesNum = len(sentences)
        if self._last_is_empty(sentences):
            sentencesNum -= 1

        return f"In file {self.path} there are {charsNum} characters, {wordsNum} words and {sentencesNum} sentences"

    def _last_is_empty(self, strings: List[str]) -> bool:
        lastString = strings[len(strings) - 1].replace(" ", "")
        if lastString == "":
            return True

        return False



rtf = ReadTextFile("text.txt")

print(rtf.calc())

