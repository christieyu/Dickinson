# Christie Yu, Oct 31 2019

from bs4 import BeautifulSoup
import requests
# boilerplate from https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486


page_link = 'https://en.wikipedia.org/wiki/List_of_Emily_Dickinson_poems'
page_response = requests.get(page_link, timeout=5)
soup1 = BeautifulSoup(page_response.content, "html.parser")

textContent = []
output = []

table = soup1.find('table')
fields = ["title", "fasc", "pubdate", "first_ID", "collect_ID", "J_ID", "F_ID"]
# print(fields[:6])

for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 7:
        data = {}
        for i in range(6):
            data[fields[i]] = tds[i].text.strip()

        ahref = tr.find('a')
        if ahref != None:
            poem_link = ahref['href']
            poem_response = requests.get(poem_link, timeout=5)
            soup2 = BeautifulSoup(poem_response.content, "html.parser")

            poemdivs = soup2.find_all('div', {'class':'poem'})

            poem_list = []

            for poem in poemdivs:
                poem_version = poem.find('p').text.strip()
                poem_list.append(poem_version)

            data["poems"] = poem_list

        else:
            data["poems"] = None

        output.append(data)
        print(data)

# print(output)

# You can access a list of dicts (one dict per row entry) with "output"
# The field names are: "title", "fasc", "pubdate", "first_ID", "collect_ID", "J_ID", "F_ID", "poems"
# "poems" is a list of poem versions given by Wikipedia
