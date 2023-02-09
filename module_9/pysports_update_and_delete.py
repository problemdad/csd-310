# Joshua Hammerling
# CYBR410-T303
# Assignment 9.3
# 2/8/2023

# Connection Code That We Are Reusing

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):


    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    

    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:

    db = mysql.connector.connect(**config) # connect to the pysports database 

    # get the cursor object
    cursor = db.cursor()

    # insert player 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # Smeagol data
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert the new player record
    cursor.execute(add_player, player_data)

    # commit the insertion
    db.commit()

    # Display After Insert
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # update the new record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # execute the update
    cursor.execute(update_player)

    # show all records after update
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete gollum 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    # show records after delete
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()

    # END PROGRAM