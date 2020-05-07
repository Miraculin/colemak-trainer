import printer
import textFilter
from scoring import scoreAbsouluteWordDifference as errorFun
import time

if __name__ == "__main__":
    printer.printColemakLayout()
    numWords = 10
    wordsToType = textFilter.generateNWordsByLength(numWords, 0, True)
    displayText = " ".join(wordsToType)
    t = time.time()
    print(displayText)
    typed = input()
    print("Errors: " + str(errorFun(displayText, typed)))
    timeTaken = time.time()-t
    print("Time Taken: " + str(timeTaken) + "s")
    print("Uncorrected WPM: " + str(numWords/timeTaken*60))
    printer.printCorrectIncorrect(displayText, typed)
