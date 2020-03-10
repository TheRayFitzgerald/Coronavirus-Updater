import requests
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.findAll("div", class_="maincounter-number")


print(results[0].prettify())
corona_total_count = results[0].find('span')
print('####')
"""
for item in results:
    print(item.prettify())
"""
#print(len(results))
print(corona_total_count.text)