import checkLevel, checkWoordenlijst, csv
from entry import RawEntry, DictEntry, getFormattedForms

def getInfo(word: str):
    level = checkLevel.getLevel(word)
    words = checkWoordenlijst.checkWoordenlijst(word)
    return [RawEntry(entry[0], level, entry[1], entry[2]) for entry in words]

def rawToDict(raw: RawEntry):
    dict = DictEntry()
    if 'art' in raw.forms: dict.article = raw.forms['art']
    dict.lemma   = raw.lemma
    dict.cefr    = raw.level
    dict.pos     = raw.pos
    dict.forms   = getFormattedForms(raw)
    return dict

def addIfEmpty(dict1: DictEntry, dict2: DictEntry):
    if dict1.lemma == "":
        dict1.lemma = dict2.lemma
    if dict1.cefr == "":
        dict1.cefr = dict2.cefr
    if dict1.pos == "":
        dict1.pos = dict2.pos
    if dict1.forms == "":
        dict1.forms = dict2.forms

if __name__ == "__main__":
    tab = []
    with open('J_ORIGINAL.csv', 'r') as f:
        reader = csv.reader(f)
        tab = [row[:-1] for row in reader][1:]

    allEntries = [DictEntry(*row) for row in tab]

    rawTest = getInfo('kopen')[0]
    print(rawToDict(rawTest))

    #testWords = [
        #"pak", 
    #]
    #for word in testWords:
        #w = getInfo(word)
        #print(w)
        #for entry in w:
            #print(
                #entry.lemma,            
                #entry.level,
                #getFormattedForms(entry)
            #)