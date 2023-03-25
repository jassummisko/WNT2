import requests
from bs4 import BeautifulSoup

def checkZoekeenvoudigewoorden(woord: str, niveau: str):
    woord = woord.lower()
    niveau = niveau.upper()
    data = {
        'search-term': woord,
        'taalniveau': niveau,
    }
    response = requests.post('https://www.zoekeenvoudigewoorden.nl/index.php', data=data)
    processed = BeautifulSoup(response.text, features="html.parser").find("p")
    res = processed['class'][0]
    if res == "correct": return True
    if res == "wrong": return False
    return None

def checkIshetb1(woord: str):
    woord = woord.lower()
    response = requests.get('https://www.ishetb1.nl/search', params={"word": woord})
    processed = BeautifulSoup(response.text, features="html.parser"
        ).find("div", {"class": "ishetb1-verdict"}).find("h1").text.strip()
    if processed == "JA": return True
    if processed == "NEE": return False
    if processed == "?": return None

def getLevel(word: str):
    if checkZoekeenvoudigewoorden(word, "A2"): return "A2"
    if checkZoekeenvoudigewoorden(word, "B1"): return "B1"
    if checkIshetb1(word): return "B1"
    return "B2"