from dataclasses import dataclass

def returnIfExisting(dict: dict, str: str):
    if str in dict: return dict[str]
    return "/"

@dataclass
class RawEntry:
    lemma:  str
    level:  str
    pos:    str
    forms:  dict

def formatForms(rawEntry: RawEntry, forms: list[str], formatting: str) -> str:
    return formatting.format(
        *[returnIfExisting(rawEntry.forms, form) for form in forms]
    )

def getFormattedForms(rawEntry: RawEntry) -> str:
    if rawEntry.pos == "znw": 
        return formatForms(rawEntry, ["pl", "dim"], "{}; {}")
    if rawEntry.pos == "ww":  
        return formatForms(rawEntry, ["1prs", "1pst", "part"], "{}, {}, {}")
    if rawEntry.pos == "bnw": 
        return formatForms(rawEntry, ["vbg", "com", "sup"], "{}; {}, {}")
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