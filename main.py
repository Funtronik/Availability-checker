
import requests
from bs4 import BeautifulSoup
import regex
import re
import json

out = " OUT OF STOCK"
ava = " IN STOCK"

def komputronik(txt):
    matches = re.finditer(r"dataLayer.push\((.*?)\)\;", txt, re.MULTILINE | re.DOTALL)
    for matchNum, match in enumerate(matches, start=1):
        return match.group(1)
def printToConsole(store, prodName, avail):

    if avail == 1:
        print("Komputronik 3070:", ava)
    else:
        print("Komputronik 3070:", out)

def main(self):
    f = open("C:\\Users\\Luigiana\\Documents\\3070.txt", "r")
    for x in f:
        html = requests.get(x)
        soup = BeautifulSoup(html.text, features="html.parser")
        # print(soup)
        found = komputronik(html.text)
        json = json.loads(found)
        available = json["ecommerce"]["detail"]["products"][0].get('availability')
        printToConsole("RTX 3070", 1)

while True:
    main()