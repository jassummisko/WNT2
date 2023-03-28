from wiktionaryparser import WiktionaryParser
import re

def getIpa(parser: WiktionaryParser, word: str) -> str:
    testIpa = ""
    try:
        test = parser.fetch(word)[0]['pronunciations']['text'][0]
        testIpa : str = re.findall("\/.*?\/", test)[0] \
            .removesuffix("/") \
            .removeprefix("/") \
            .replace(".", "")
    except: pass
    return testIpa