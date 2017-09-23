class Team:
    """Holds all the stats for a particular team
    Author: Joseph Sommer
    Date: 8/23/17
    """
    def __init__(self, stats_html, schedule_html, record_html):
        # stats_rows gives us all the <tr> tags 
        stats_rows = stats_html.find_all("tr")
        record_rows = record_html.find_all("tr")
        # <table>
        #   <tr> (index here)
        #       <td> (index here)
        #           next_element
        # pick a table row, column by indexing the list
        self.scoring_points_game = stats_rows[1].find_all("td")[1].next_element
        self.total_first_down = stats_rows[3].find_all("td")[1].next_element
        self.rushing_yards_attempt = stats_rows[5].find_all("td")[1].next_element
        self.passing_yards = stats_rows[7].find_all("td")[1].next_element
        self.total_offense_yards_play = stats_rows[10].find_all("td")[1].next_element        
        self.record = record_rows[1].find_all("td")[1].next_element
        self.wins = self.record.split("-")[0]
        self.losses = self.record.split("-")[1]

    def __str__(self):
        return "Points/game: " + str(self.scoring_points_game) + "\nTotal first downs: " + str(self.total_first_down) + \
                "\nRushing yards/attempt: " + str(self.rushing_yards_attempt) + "\nTotal passing yards: " + str(self.passing_yards) + \
                "\nTotal offense yards/play: " + str(self.total_offense_yards_play) + "\nRecord for season: " + str(self.record) + \
                "\nWins: " + str(self.wins) + "\nLosses: " + str(self.losses)