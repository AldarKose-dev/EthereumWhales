import cloudscraper
from bs4 import BeautifulSoup
import re


def parser():
    accounts = []
    balance = []
    scraper = cloudscraper.create_scraper()
    url = scraper.get("https://etherscan.io/accounts/1?ps=100")
    soup = BeautifulSoup(url.text, 'html.parser')
    cells = soup.findAll("td")
    links = soup.findAll("a")

    for i in links:
        if(i.text.startswith("0x")):
            accounts.append(i.text)

    for i in cells:
        if i.find('span') and i.text.startswith("0x") != 1:
            result = float(i.text.rpartition("Ether")[0].replace(',', ''))
            balance.append(result)
        elif any(c.isdigit() for c in i.text) and i.find(text=re.compile("Ether")):
            result = float(i.text.rpartition("Ether")[0].replace(',', ''))
            balance.append(result)

    return balance, accounts
