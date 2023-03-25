import checkLevel, checkWoordenlijst

def getInfo(word: str):
    level = checkLevel.getLevel(word)
    words = checkWoordenlijst.checkWoordenlijst(word)
    return word, level, words

def test(woord: str):
    word, level, words = getInfo(woord)
    print(word, level, words)

if __name__ == "__main__":
    testWords = [
        "woord", 
        "vracht", 
        "triestig"
    ]
    for word in testWords:
        test(word)