import mysql.connector

# connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="QwEr#45%",
    database="pysports"
)

# create a cursor
cursor = db.cursor()

# select query for the team table
team_query = "SELECT team_id, team_name, mascot FROM team"
cursor.execute(team_query)
teams = cursor.fetchall()

# iterate over the cursor and display the results
print("Teams:")
for team in teams:
    print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

# select query for the player table
player_query = "SELECT player_id, first_name, last_name, team_id FROM player"
cursor.execute(player_query)
players = cursor.fetchall()

# iterate over the cursor and display the results
print("Players:")
for player in players:
    print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

# close the cursor and database connection
cursor.close()
db.close()
