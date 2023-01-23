from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Accessing octane.gg's stats on all the RLCS teams
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

teamName = []  # Gets the team name
teamImage = []  # Ges the image of the team
winPercentage = []  # Win percentage of each team
goalsPerGame = []  # Average goals per game of each team
assistsPerGame = []  # Average assists per game of each team
savesPerGame = []  # Average saves per game of each team
shotsPerGame = []  # Average shots per game of each team
shootingPercentage = []  # Shooting percentrage of each team
driver.get("https://octane.gg/stats/teams?mode=3&region=NA&region=EU&region=OCE&region=SAM&region=ASIA&region=ME&region=AF&region=INT&minGames=250")

content = driver.page_source
num = 1
soup = BeautifulSoup(content, 'html.parser')
for a in soup.find_all('table'):
    name = a.find('div', attrs={'class': 'chakra-link css-1r88v6v'})
    image = a.find('img', attrs={'class': 'chakra-image css-10xqgwl'})
    print(name)
    print(image)

teamName.append("hi")
teamImage.append("hi")
df = pd.DataFrame({'Team Name:': teamName, 'Image:': teamImage})
df.to_csv('Teams.csv', index=False, encoding='utf-8')
