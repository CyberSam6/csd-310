import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "pysports_password",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# connect to the database 
db = mysql.connector.connect(**config)

# get the cursor
cursor = db.cursor()

# INSERT a new player record
insert_query = "INSERT INTO player(first_name, last_name, team_id) VALUES ('Gandalf', 'The Grey', 1)"
cursor.execute(insert_query)
db.commit()
print("New player record has been inserted.")

# SELECT query to display player records with team names
select_query = "SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
cursor.execute(select_query)
players = cursor.fetchall()

# print the player records with team names
print("-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
    print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam Name: {player[3]}\n")

# UPDATE the newly inserted player record
update_query = "UPDATE player SET team_id = 2 WHERE first_name = 'Gandalf'"
cursor.execute(update_query)
db.commit()
print("New player record has been updated.")

# SELECT query to display updated player record with team name
select_query = "SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id WHERE player.first_name = 'Gandalf'"
cursor.execute(select_query)
player = cursor.fetchone()

# print the updated player record with team name
print("-- DISPLAYING UPDATED PLAYER --")
print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam Name: {player[3]}\n")

# DELETE the updated player record
delete_query = "DELETE FROM player WHERE first_name = 'Gandalf'"
cursor.execute(delete_query)
db.commit()
print("New player record has been deleted.")