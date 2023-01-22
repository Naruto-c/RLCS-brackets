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
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': 'css-8d3ssv'}):
