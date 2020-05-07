ANSI_BLACK = "\033[0;30m"
ANSI_RED = "\033[0;31m"
ANSI_GREEN = "\033[0;32m"
ANSI_BROWN = "\033[0;33m"
ANSI_BLUE = "\033[0;34m"
ANSI_PURPLE = "\033[0;35m"
ANSI_CYAN = "\033[0;36m"
ANSI_RESET = "\033[0m"

def printCorrectIncorrect(refText, inputText):
    refSplit=refText.split()
    inputSplit = inputText.split()

    outputStr = ""
    for correctWord, inputWord in zip(refSplit, inputSplit):

        if inputWord != correctWord:
            currWord = ""
            for correctLetter,inputLetter in zip(correctWord, inputWord):
                if correctLetter!=inputLetter:
                    currWord += ANSI_RED
                else:
                    currWord += ANSI_GREEN
                currWord += inputLetter
            if len(correctWord) > len(inputWord):
                currWord += ANSI_RED
                currWord += correctWord[len(inputWord):]
            else:
                currWord += ANSI_RED
                currWord += inputWord[len(correctWord):]
            outputStr += currWord
        else:
            outputStr+= ANSI_GREEN
            outputStr+= correctWord
        outputStr += " "
    outputStr.strip()
    outputStr += ANSI_RESET
    print(outputStr)

def printColemakLayout():
    first_row = "Q  W  F  P  G  J  L  U  Y  ;  [  ]"
    second_row = " A  R  S  T  D  H  N  E  I  O  \""
    third_row = "  Z  X  C  V  B  K  M  ,  .  /"
    print(first_row)
    print(second_row)
    print(third_row)

if __name__ == "__main__":
    printCorrectIncorrect("star is cool", "star is kolo")
    printCorrectIncorrect("star is cool", "star is kasdf")
    printCorrectIncorrect("Victor Karen Fung", "Victor Karen Fung")
    printCorrectIncorrect("Victor Karen Fung", "V K F")
    printColemakLayout()
