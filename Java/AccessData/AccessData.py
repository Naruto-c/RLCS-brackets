import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://octane.gg/stats/teams?mode=3&region=NA&region=EU&region=OCE&region=SAM&region=ASIA&region=ME&region=AF&region=INT&minGames=250"

page = requests.get(url)
soup = BeautifulSoup(page.text)

row = soup.find('tr')
print(soup)
