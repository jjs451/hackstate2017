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
    matchup_data = tables[1]
    return matchup_data

def populate_csv(year, team, teamname):
    csv = open("data.csv", "a")
    msu = get_team_data(year, team).find_all("tr")
    for i in range(1, len(msu)-1):
        rows = msu[i].find_all("td")
        try:
            opponent = rows[1].a.next_element
            print(rows[1].a.next_element)
        except AttributeError:
            opponent = rows[1].next_element
            print(rows[1].next_element)
        score_str = rows[2].next_element[1:].split("-")
        score1 = score_str[0].strip()
        score2 = score_str[1].strip()
        print(rows[2].next_element)
        output_str = teamname + "," + str(opponent).strip() + "," + score1 + "," + score2 + "\n"
        csv.write(output_str)

    csv.close()

populate_csv("2016", MISSISSIPPI_STATE, "Mississippi St.")
populate_csv("2016", ALABAMA, "Alabama")
populate_csv("2016", ARKANSAS, "Arkansas")
populate_csv("2016", AUBURN, "Auburn")
populate_csv("2016", FLORIDA, "Florida")
populate_csv("2016", GEORGIA, "Georgia")
populate_csv("2016", KENTUCKY, "Kentucky")
populate_csv("2016", LSU, "LSU")
populate_csv("2016", TSUN, "Mississippi")
populate_csv("2016", MISSOURI, "Missouri")
populate_csv("2016", SOUTH_CAROLINA, "South Carolina")
populate_csv("2016", TENNESEE, "Tennesee")
populate_csv("2016", TEXAS, "Texas A&M")
populate_csv("2016", VANDERBILT, "Vanderbilt")

csv = open("data.csv", "r")
data = csv.readlines()
csv.close()
csv = open("data.csv", "w")
csv.seek(0)
csv.truncate()
for row in data:
    line1 = row.split(",")
    dupe_found = False
    for row in data:
        line2 = row.split(",")
        if (line1[0] == line2[1]) and (line1[1] == line2[0]) and (line1[2]+"\n" == line2[3]) and (line1[3] == line2[2]+"\n"):
            dupe_found = True
            data.remove(",".join(line2))
            break
            
    csv.write(",".join(line1))
    print(line1)
csv.close()