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
soup = BeautifulSoup(content, 'html.parser')
for a in soup.find_all('tr'):
    name = a.find('a', attrs={'class': 'chakra-link css-1r88v6v'})
    image = a.find('img', attrs={'class': 'chakra-image css-10xqgwl'})

    # I literally have no idea why, but the first 'a' tag is none
    # Therefore, to call .get_text(), make sure that it's a tag element, not none
    if not (name is None):
        # Appending team name
        teamName.append(name.get_text())
    else:
        teamName.append("N/A")
    if not (image is None):
        data = image.get('src')
        print(data)
        teamImage.append(data)
    else:
        teamImage.append("N/A")


df = pd.DataFrame({'Team Name:': teamName, 'Image:': teamImage})
df.to_csv('Teams.csv', index=False, encoding='utf-8')
