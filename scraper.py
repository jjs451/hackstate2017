"""Scrapes cfbstat.com for html tables cont"""

from bs4 import BeautifulSoup 
import requests
import Team_statistics

# gets stats from MSU's 2016 football season
url = "http://www.cfbstats.com/2016/team/430/index.html"
response = requests.get(url)
data = response.text

souped_data = BeautifulSoup(data)
tables = souped_data.find_all("table")
team_stats = Team_statistics(tables[0], tables[1], tables[2])