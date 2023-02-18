import mysql.connector

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="QwEr#45%",
    database="pysports"
)

# Create cursor
cursor = db.cursor()

# Inner join query
query = """
SELECT player.player_id, player.first_name, player.last_name, team.team_name 
FROM player 
INNER JOIN team 
ON player.team_id = team.team_id
"""

# Execute query
cursor.execute(query)

# Fetch results
results = cursor.fetchall()

# Display results
for result in results:
    print("Player ID: {}".format(result[0]))
    print("First Name: {}".format(result[1]))
    print("Last Name: {}".format(result[2]))
    print("Team Name: {}".format(result[3]))
    print()
