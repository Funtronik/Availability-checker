# Availability checker

# External classes
import requests
import time
from urllib.parse import urlparse

# My classes
from switcher import domainProcessor as dp
from colours import  bcolors

availableToday = {}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
Processor = dp()

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
            if x == '\n':
                continue

            domain = urlparse(x).netloc
            html = requests.get(x, headers=headers)
            Processor.processAccordingly(domain, html.text)

            if Processor.available == 'available':
                printToConsole(domain, Processor.prodName, 1, Processor.price, Processor.vendCode)
                if Processor.vendCode in availableToday:
                    current = availableToday[Processor.vendCode] + 1
                    updateObj = {Processor.vendCode: current}
                    availableToday.update(updateObj)
                else:
                    updateObj = {Processor.vendCode: 1}
                    availableToday.update(updateObj)
            else:
                printToConsole(domain, Processor.prodName, 0, None, None)

            time.sleep(5)

        print(availableToday)


if __name__ == "__main__":
    main()
