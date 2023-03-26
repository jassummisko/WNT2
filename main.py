import checkLevel, checkWoordenlijst
from dataclasses import dataclass

@dataclass
class DictEntry:
    lemma:  str
    level:  str
    pos:    str
    forms:  dict

def getInfo(word: str):
    level = checkLevel.getLevel(word)
    words = checkWoordenlijst.checkWoordenlijst(word)
    buff  = []
    for entry in words:
        buff.append(DictEntry(entry[0], level, entry[1], entry[2]))
    return buff

if __name__ == "__main__":
    testWords = [
        "pak", 
    ]
    for word in testWords:
        print(getInfo(word))