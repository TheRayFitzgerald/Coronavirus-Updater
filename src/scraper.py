import requests
from bs4 import BeautifulSoup
import time

def setup():
    URL = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def corona_total_count():
    soup = setup()
    results = soup.findAll("div", class_="maincounter-number")
    corona_total_count = results[0].find('span')

    return corona_total_count.text