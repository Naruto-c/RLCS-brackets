import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options

webdriver_service = Service("./chromedriver")  # Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service)
url = 'https://octane.gg/stats/teams?mode=3&region=NA&region=EU&region=OCE&region=SAM&region=ASIA&region=ME&region=AF&region=INT&minGames=250'
driver.get(url)
driver.maximize_window()
time.sleep(3)
table = BeautifulSoup(driver.page_source, 'lxml')
df = pd.read_html(str(table))[0]
print(df)
df.to_csv('Teams.csv', index=False, encoding='utf-8')
