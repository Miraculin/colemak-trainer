from random import sample
GOOGLE_CORPUS = 'text/google-10000-english-no-swears.txt'
BIGRAM_CORPUS = 'text/2-letter.txt'

def generateNWordsByLength(n, length, homerow=False):
    '''
    Length Categories:
    0 - 0-4 letters
    1 - 5-7 letters
    2 - 8+ letters
    10 - 0-7 letters
    210 - every length

    homerow: if True, constrains words to letters in homerow only
    '''
    with open(GOOGLE_CORPUS, 'r') as corpus:
        filtered = filter(lambda x: lengthFilter(x, length), map(lambda y: y.rstrip(), corpus))
        if homerow:
            filtered = filter(homerowFilter, filtered)
        sampledWords = sample(list(filtered),k=max(n, len(list(filtered))))
        # print(sampledWords)
        return sampledWords

def lengthFilter(word, length):
    if length == 0:
        return 0 < len(word) < 5
    elif length == 1:
        return 4 < len(word) < 8
    elif length == 2:
        return 7 < len(word)
    elif length == 10:
        return 0 < len(word) < 8
    else:
        return True

def homerowFilter(word):
    homerowLetters = ['A', 'R' ,'S','T','D','H','N','E','I','O', '\n']
    homerowOnly = True
    for letter in word.upper():
        if letter not in homerowLetters:
            homerowOnly = False

    return homerowOnly

if __name__ == "__main__":
    generateNWordsByLength(10, 0)
    generateNWordsByLength(10, 1)
    generateNWordsByLength(10, 2)
    generateNWordsByLength(10, 10)
    generateNWordsByLength(10, 10, True)
