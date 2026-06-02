#SCATTER PLOT 

import matplotlib.pyplot as ken 

team_years = [4, 5, 6, 8, 9, 10, 2, 7, 1, 12 ]
team_scores = [200, 100, 400, 300, 600, 800, 700, 900, 650, 850]

ken.scatter(team_years, team_scores, color="red", marker="o")

ken.title("Team Data")
ken.ylabel(" Teams's overall scores")
ken.xlabel("Team's years Experience")

ken.show()