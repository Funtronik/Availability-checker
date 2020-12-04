import json
import re

class domainProcessor:

    def processAccordingly(self, domain, txt):
        self.domain = domain
        self.txt = txt

        fun = self.switcher.get(domain, lambda: "Invalid domain argument")
        ret = fun(self, self.txt)

    def komputronik(self,txt):
        matches = re.finditer(r"dataLayer.push\((.*?)\)\;", txt, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches, start=1):
            properties = match.group(1)
            continue

        j = json.loads(properties)
        self.available = j["ecommerce"]["detail"]["products"][0].get('availability')
        self.prodName = j["ecommerce"]["detail"]["products"][0].get('name')
        self.vendCode = j["ecommerce"]["detail"]["products"][0].get('vendorCode')
        self.price = j["ecommerce"]["detail"]["products"][0].get('price')

    def xkom(self,txt):
        # "availabilityCode":"temporary_unavailable"
        matches = re.finditer(r"availabilityCode\":\"(.*?)\"", txt, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches, start=1):
            self.available = match.group(1)
            continue

        # "mpn": "DUAL-RTX3070-8G"
        matches = re.finditer(r"mpn\":\"(.*?)\"", txt, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches, start=1):
            self.vendCode = match.group(1)
            continue

        # "@type":"Product","name":"ASUS GeForce RTX 3070 DUAL 8GB GDDR6"
        matches = re.finditer(r"\"@type\":\"Product\",\"name\":\"(.*?)\"", txt, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches, start=1):
            self.prodName = match.group(1)
            continue

        # ,"price":2879}
        matches = re.finditer(r",\"price\":(.*?)}", txt, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches, start=1):
            self.price = match.group(1)
            continue

    def __init__(self):
        self.available = None
        self.prodName = None
        self.vendCode = None
        self.price = None
        self.domain = None
        self.txt = None

    switcher = {
            "www.komputronik.pl": komputronik,
            "www.x-kom.pl": xkom
        }