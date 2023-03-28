import checkLevel, checkWoordenlijst, csv
import dataclasses
from entry import RawEntry, DictEntry, getFormattedForms
from wiktionaryparser import WiktionaryParser
from checkIpa import getIpa

def getInfo(entry: DictEntry) -> list[RawEntry]:
    if DictEntry.cefr != '': level = DictEntry.cefr
    else: level = checkLevel.getLevel(entry.lemma)
    words = checkWoordenlijst.checkWoordenlijst(entry.lemma)
    if words == None: return None
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
        dict1.lemma = dict2.lemma + "*"
    if dict1.cefr == "":
        dict1.cefr = dict2.cefr + "*"
    if dict1.pos == "":
        dict1.pos = dict2.pos + "*"
    if dict1.forms == "":
        dict1.forms = dict2.forms + "*"

def findBestMatch(dict: DictEntry, dicts: list[DictEntry]):
    bestMatch = None
    bestScore = 0
    for dict2 in dicts:
        score = 0
        if dict.cefr == dict2.cefr:
            score += 1
        if dict.pos == dict2.pos:
            score += 1
        if dict.lemma == dict2.lemma:
            score += 1
        if dict.article == dict2.article:
            score += 1
        if dict.pos == dict2.pos:
            score += 1
        if score > bestScore:
            bestScore = score
            bestMatch = dict2
    return bestMatch

def formatPos(dicts: list[DictEntry]):
    return '; '.join([findBestMatch(dict, dicts).pos for dict in dicts])

def processLetter(letter: str):
    tab = []
    with open(f'testdata/{letter}_ORIGINAL.tsv', 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        tab = [row[:-1] for row in reader][1:]

    allEntries = [DictEntry(*row) for row in tab]
    newEntries = [['', 'Lemma', 'Fonetisch', 'Woordsoort', 'Vormen','Erk', 'Synoniem of definitie', 'Voorbeeldzin']]
    for entry in allEntries:
        rawTest = getInfo(entry)
        if rawTest != None:
            scrapedEntries = [rawToDict(entry) for entry in rawTest]
            bestMatch = findBestMatch(entry, scrapedEntries)
            bestMatch.pos = formatPos(scrapedEntries) + "*"
            addIfEmpty(entry, bestMatch)
            entry.pos = bestMatch.pos
        print(entry)
        newEntries.append(
            [entry.article, 
            entry.lemma, 
            entry.ipa, 
            entry.pos, 
            entry.forms, 
            entry.cefr, 
            entry.definition, 
            entry.example]
        )

    with open(f'testdata/{letter}_FINAL.tsv', 'w') as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(newEntries)

def processIpa(filename: str):
    tab = []
    with open(f'testdata/{filename}', 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        tab = [row[:-1] for row in reader][1:]
    
    allEntries = [DictEntry(*row) for row in tab]
    IPAs = []
    parser = WiktionaryParser()
    parser.set_default_language('dutch')
    for entry in allEntries:
        rawTest = getIpa(parser, entry.lemma)
        transcription = rawTest+"*"
        print(entry.lemma, transcription)
        IPAs.append(transcription+"\n")

    with open(f'testdata/{filename}_JUSTIPA.txt', 'w') as f:
        f.writelines(IPAs)

if __name__ == "__main__":
    #for letter in ["E"]: processLetter(letter)        
    processIpa("A_PREIPA.tsv")