class Team_statistics:
    """Holds all the stats for a particular team
    Author: Joseph Sommer
    Date: 8/23/17
    """
    def __init__(self, stats_html, schedule_html, record_html):
        # stats_rows gives us all the <tr> tags 
        stats_rows = stats_html.find_all("tr")
        # <table>
        #   <tr>
        #       <td>
        #           next_element
        # pick a table row, column by indexing the list
        scoring_points_game = stats_rows[1].find_all("td")[1].next_element