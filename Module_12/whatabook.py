# Joshua Hammerling
# CYBR410-T303
# Module 12 What-A-Book Submission

""" THIS IS IN DRAFT STAGE, I STILL NEED TO WORK ON THE VALIDATION FOR INPUTS AS THE PROGRAM ERRORS OUT WHEN ALPHA CHARACTERS ARE ENTERED."""

# IMPORT STATEMENTS HERE
from errno import errorcode
import sys
import mysql.connector
from  mysql.connector import errorcode

# CONFIGURE DATABASE / USER
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

# CONNECT TO THE DATABASE

db = mysql.connector.connect(**config)

# DEBUG CODE USED FOR DATABASE ACCESS ERRORS / TESTING
"""
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid Username or Password")

    elif err.errno == errorcode.BAD_DB_ERROR:
        print("The selected database does not exist")

    else:
        print(err)
"""


# DISPLAY THE MAIN MENU
def show_menu():
    print("\n-- MAIN MENU --\n1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program\n")
  

# DISPLAY ALL BOOKS IN INVENTORY
def show_book(_cursor):
    cursor = db.cursor()
    cursor.execute("SELECT book_id, book_name, author, details from book")  # THIS LINE OF CODE WAS UTILIZED FROM COURSE FILE
    books = cursor.fetchall()
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2])) # THIS LINE OF CODE WAS UTILIZED FROM COURSE FILE
    show_menu() # ADDED 3/3/2023
    menu_selection() # ADDED 3/3/2023
 


# SHOW LOCATIONS
def show_locations(_cursor):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM store")
    stores = cursor.fetchall()
    for store in stores:
        print("\nStore Address: {}".format(store[1]))
    show_menu()  # ADDED 3/3/2023
    menu_selection() # ADDED 3/3/2023 you

# VALIDATE USER ID
def validate_user(_user_id):
    if _user_id == "1":
        return True
    elif _user_id == "2":
       return True
    elif _user_id == "3":
      return True
    else:
      return False    
      
# USER ACCOUNT MENU
def show_account_menu():
    print("\n-- ACCOUNT MENU --\n1. Show wishlist\n2. Add book\n3. Main menu")

# SHOW WISHLIST - CODE USED FROM CLASS FILE

def show_wishlist(_cursor, _user_id):
    
    cursor = db.cursor()
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = cursor.fetchall()
    print("\n        -- DISPLAYING WISHLIST ITEMS --\n")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

# DISPLAY BOOKS NOT IN USER WISHLIST
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    cursor = db.cursor()
    cursor.execute(query)

    books_to_add = cursor.fetchall()

    for book in books_to_add:
        print("\n  Book Id: {}      \n  Book Name: {}".format(book[0], book[1]))

# ADD BOOKS TO WISHLIST
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    cursor = db.cursor()
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))



def menu_selection():   # ADDED MENU SELECTION FUNCTION ON 3/3/2023
    selection = input("Please enter a selection: ")   # CHANGED INPUT TYPE FROM INT TO STRING TO HANDLE ALPHA-CHARACTER ERRORS - 3/3/2023

# DEFINE VARIABLES
    acctSelection = 0
    user_id = 0

    # ON SELECT 1, SHOW BOOKS
    if selection == "1":
        cursor = db.cursor
        show_book(cursor)

    # ON SELECT 2, DISPLAY LOCATIONS
    elif selection == "2":
        cursor = db.cursor
        show_locations(cursor)

    # ON SELECT 3, RECEIVE USER ID INPUT
    elif selection == "3":
        user_id = input("\nPlease enter your user ID: ")

    # SHOW ACCOUNT MENU IF INPUT IS VALID
        if validate_user(user_id):
            show_account_menu()
            account_selection(user_id)
    
    # ON INVALID USER ID INPUT, RETURN TO MAIN MENU
        else:
             print("The user ID is not valid.  Returning to main menu. \n")
             show_menu()
             menu_selection()

    elif selection == "4":
        print("\nThank you for using the WhatABook Application!\n") # ADDED LINE BREAKS 3/23/2023
        exit()

    else:     
        print("\nInvalid selection.  Please try again.\n")
        show_menu()
        menu_selection()

def account_selection(user_id):            
    acctSelection = input("\nPlease enter a selection: ")

    if acctSelection == "1":
        cursor = db.cursor
        show_wishlist(cursor, user_id)
        show_account_menu()
        account_selection(user_id)

     # SHOW BOOKS AND ADD BOOKS
    elif acctSelection == "2":
        cursor = db.cursor
        show_books_to_add(cursor, user_id)
        book_id = int(input("\nEnter a book ID to add it to the wishlist: "))
        add_book_to_wishlist(cursor, user_id, book_id)
        show_account_menu()
        account_selection(user_id)

     # RETURN TO MAIN MENU 
    elif acctSelection == "3":
        print("\nReturning to main menu.\n")
        show_menu()
        menu_selection()

    # ERROR HANDLING    
    else:    
        print("Invalid option. Please make a selection from the menu")
        show_account_menu()
        acctSelection = int(input("Enter a selection: "))

        print("\nReturning to main menu.") # ADDED LINE 3/23/2023
        show_menu()
        menu_selection()

    

# START PROGRAM
print("\nWelcome to WhatABook!\n")
show_menu()
menu_selection()