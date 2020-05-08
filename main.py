import printer
import textFilter
from scoring import scoreAbsouluteWordDifference as errorFun
import time
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Starts colemak trainer')

    parser.add_argument('-n', dest='numWords', type=int,
                        default=10, help='number of words to type')

    parser.add_argument('-d', metavar='difficulty', type=int,
                        default=0, dest='difficulty',
                        help='Word length settings:\n 0 - 0-4 letters \n 1 - 5-7 letters \n 2 - 8+ letters \n 10 - 0-7 letters \n 210 - any length')

    parser.add_argument('--homerow', dest='homerow', action='store_true',
                        help='Use home row letters only')

    args = parser.parse_args()

    printer.printColemakLayout()

    numWords = args.numWords
    difficulty = args.difficulty
    homerow = args.homerow

    print(numWords)
    print(difficulty)
    print(homerow)
    wordsToType = textFilter.generateNWordsByLength(numWords, difficulty, homerow)
    displayText = " ".join(wordsToType)

    for i in range(0, 3):
        print(str(3-i))
        time.sleep(1)

    print(displayText)
    t = time.time()
    typed = input()
    print("Errors: " + str(errorFun(displayText, typed)))
    timeTaken = time.time()-t
    print("Time Taken: " + str(timeTaken) + "s")
    print("Uncorrected WPM: " + str(numWords/timeTaken*60))
    printer.printCorrectIncorrect(displayText, typed)
