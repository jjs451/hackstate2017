"""Scrapes cfbstats.com for html tables with team stats"""
MISSISSIPPI_STATE = 430
ALABAMA = 8
ARKANSAS = 31
AUBURN = 37
FLORIDA = 235
GEORGIA = 257
KENTUCKY = 334
LSU = 365
TSUN = 433
MISSOURI = 434
SOUTH_CAROLINA = 648
TENNESEE = 694
TEXAS = 697
VANDERBILT = 736

from bs4 import BeautifulSoup 
import requests
import Team

# gets stats from MSU's 2016 football season
year = "2016"
team = MISSISSIPPI_STATE
url = "http://www.cfbstats.com/" + year + "/team/" + team + "/index.html"
response = requests.get(url)
data = response.text

souped_data = BeautifulSoup(data, "html.parser")
tables = souped_data.find_all("table")
team_stats = Team.Team(tables[0], tables[1], tables[2])
print(team_stats)