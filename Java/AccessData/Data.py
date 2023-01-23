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
driver.get("https://octane.gg/stats/teams?mode=3&minGames=50&group=rlcs2122fall")

content = driver.page_source
soup = BeautifulSoup('features = "lxml"')
for a in soup.findAll('div', href=True, attrs={'class': 'chakra-stack css-8g1510'}):
    name = a.find('a', attrs={'class': 'chakra-link css-1r88v6v'})
    image = a.find('img', attrs={'class': 'chakra-image css-10xqgwl'})
    teamName.append(name.text)
    teamImage.append(image.text)

teamName.append(1)
teamImage.append(1)
df = pd.DataFrame({'Team Name:': teamName, 'Image:': teamImage})
df.to_csv('Teams.csv', index=False, encoding='utf-8')
