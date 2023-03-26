from dataclasses import dataclass

@dataclass
class RawEntry:
    lemma:  str
    level:  str
    pos:    str
    forms:  dict

def returnIfExisting(dict: dict, str: str):
    if str in dict: return dict[str]
    return "/"

def formatForms(dictEntry: RawEntry, forms: list[str], formatting: str) -> str:
    return formatting.format(
        *[returnIfExisting(dictEntry.forms, form) for form in forms]
    )

def getFormattedForms(dictEntry: RawEntry) -> str:
    if dictEntry.pos == "znw": 
        return formatForms(dictEntry, ["pl", "dim"], "{}; {}")
    if dictEntry.pos == "ww":  
        return formatForms(dictEntry, ["1prs", "1pst", "part"], "{}, {}, {}")
    if dictEntry.pos == "bnw": 
        return formatForms(dictEntry, ["vbg", "com", "sup"], "{}; {}, {}")
    return ""

@dataclass
class DictEntry:
    article:    str = ''
    lemma:      str = ''
    ipa:        str = ''
    pos:        str = ''
    forms:      str = ''
    cefr:       str = ''
    definition: str = ''
    example:    str = ''