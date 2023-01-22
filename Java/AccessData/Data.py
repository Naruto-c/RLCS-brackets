from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Accessing octane.gg's stats on all the RLCS teams
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

winPercentage = []  # Win percentage of each team
goalsPerGame = []  # Average goals per game of each team
assistsPerGame = []  # Average assists per game of each team
savesPerGame = []  # Average saves per game of each team
shotsPerGame = []  # Average shots per game of each team
shootingPercentage = []  # Shooting percentrage of each team
driver.get("<a class="chakra-link css-ajrch1" href="/stats/players?mode=3 & amp
           minGames=50 & amp
           group=rlcs2122fall"><div class="chakra-stack css-84zodg"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" height="1em" width="1em" xmlns="http: // www.w3.org/2000/svg"><path d="M104 496H72a24 24 0 01-24-24V328a24 24 0 0124-24h32a24 24 0 0124 24v144a24 24 0 01-24 24zm224 0h-32a24 24 0 01-24-24V232a24 24 0 0124-24h32a24 24 0 0124 24v240a24 24 0 01-24 24zm112 0h-32a24 24 0 01-24-24V120a24 24 0 0124-24h32a24 24 0 0124 24v352a24 24 0 01-24 24zm-224 0h-32a24 24 0 01-24-24V40a24 24 0 0124-24h32a24 24 0 0124 24v432a24 24 0 01-24 24z"></path></svg><p class="chakra-text css-0">Stats</p></div></a>")
