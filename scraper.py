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

def get_team_data(year, team):
    """Fetches data for a given team and year, returns a Team object"""
    url = "http://www.cfbstats.com/" + year + "/team/" + str(team) + "/index.html"
    response = requests.get(url)
    data = response.text

    souped_data = BeautifulSoup(data, "html.parser")
    tables = souped_data.find_all("table")
    return Team.Team(tables[0], tables[1], tables[2])

year = "2016"
msu_2016 = get_team_data(year, MISSISSIPPI_STATE)
print(msu_2016)
print("")
lsu_2016 = get_team_data(year, LSU)
print(lsu_2016)

year = "2015"
msu_2015 = get_team_data(year, MISSISSIPPI_STATE)
print(msu_2015)
print("")
lsu_2015 = get_team_data(year, LSU)
print(lsu_2015)

year = "2014"
msu_2014 = get_team_data(year, MISSISSIPPI_STATE)
print(msu_2014)
print("")
lsu_2014 = get_team_data(year, LSU)
print(lsu_2014)

year = "2013"
msu_2013 = get_team_data(year, MISSISSIPPI_STATE)
print(msu_2013)
print("")
lsu_2013 = get_team_data(year, LSU)
print(lsu_2013)

year = "2012"
msu_2012 = get_team_data(year, MISSISSIPPI_STATE)
print(msu_2012)
print("")
lsu_2012 = get_team_data(year, LSU)
print(lsu_2012)