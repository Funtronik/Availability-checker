
import requests
from bs4 import BeautifulSoup
import regex
import re
import json
import time
from urllib.parse import urlparse
from colours import  bcolors

availableToday = {}

def komputronik(txt):
    matches = re.finditer(r"dataLayer.push\((.*?)\)\;", txt, re.MULTILINE | re.DOTALL)
    for matchNum, match in enumerate(matches, start=1):
        return match.group(1)
def printToConsole(store, prodName, avail, price, prodCode):
    out = "OUT OF STOCK"
    ava = "IN STOCK"

    if avail == 1:
        print(bcolors.OKCYAN + store + bcolors.ENDC, prodName, bcolors.OKGREEN + ava + bcolors.ENDC, bcolors.WARNING+ price + "zł" + bcolors.ENDC, prodCode)
    else:
        print(bcolors.OKCYAN + store + bcolors.ENDC, prodName, bcolors.FAIL + out + bcolors.ENDC)

def main():
    while True:
        f = open("C:\\Users\\Luigiana\\Documents\\3070.txt", "r")
        for x in f:
            domain = urlparse(x).netloc
            html = requests.get(x)
            found = komputronik(html.text)
            j = json.loads(found)
            available = j["ecommerce"]["detail"]["products"][0].get('availability')
            prodName = j["ecommerce"]["detail"]["products"][0].get('name')
            vendCode = j["ecommerce"]["detail"]["products"][0].get('vendorCode')
            price = j["ecommerce"]["detail"]["products"][0].get('price')

            if available == 'available':
                printToConsole(domain, prodName, 1, price, vendCode)
                if vendCode in availableToday:
                    current = availableToday[vendCode] + 1
                    updateObj = {vendCode: current}
                    availableToday.update(updateObj)
                else:
                    updateObj = {vendCode: 1}
                    availableToday.update(updateObj)
            else:
                printToConsole(domain, prodName, 0, None, None)

            time.sleep(10)

        print(availableToday)


if __name__ == "__main__":
    main()
