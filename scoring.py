def scoreAbsouluteWordDifference(refText, inputText):
    refSplit = refText.split()
    inputSplit = inputText.split()

    errors = 0
    for ref, input in zip(refSplit, inputSplit):
        if ref != input:
            errors += 1

    num_words_diff = abs(len(refSplit)-len(inputSplit))

    return errors+num_words_diff


if __name__ == "__main__":
    print(scoreAbsouluteWordDifference("Victor is Right", "Victor is Wrong"))
    print(scoreAbsouluteWordDifference("Victor is Right", "Victor is Wrong 1 2 3"))
    print(scoreAbsouluteWordDifference("Victor is Right", "Victor"))
