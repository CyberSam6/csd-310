import sys
import mysql.connector
from mysql.connector import errorcode

DB_CONFIG = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n  -- Main Menu --")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")

    try:
        choice = int(input('<Example enter: 1 for book listing>: '))
        return choice
    except ValueError:
        print("\n Invalid number, program terminated...\n")
        sys.exit(0)

def show_books(cursor):
    """Display all books"""
    cursor.execute("SELECT book_id, book_name, author, details from book")
    books = cursor.fetchall()

    print("\n -- DISPLAYING BOOK LISTING --")
    for book in books:
        print("Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

def show_locations(cursor):
    """Display all store locations"""
    cursor.execute("SELECT locale from store")
    locations = cursor.fetchall()

    print("\n -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("Locale: {}\n".format(location[0]))

def validate_user():
    """Validate the user's ID"""
    try:
        user_id = int(input('\n Enter a customer id <Example 1 for user_id 1>: '))
        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n Invalid number, program terminated...\n")
        sys.exit(0)

def show_account_menu():
    """Display the user's account menu"""
    print("\n  -- Customer Menu --")
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")

    try:
        account_option = int(input('<Example enter: 1 for wishlist>: '))
        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

def show_wishlist(cursor, user_id):
    """Display the user's wishlist"""
    query = (
        "SELECT user.first_name, user.last_name, book.book_name, book.author " 
        "FROM wishlist " 
        "INNER JOIN user ON wishlist.user_id = user.user_id " 
        "INNER JOIN book ON wishlist.book_id = book.book_id " 
        "WHERE user.user_id = %s"
    )
    cursor.execute(query, (user_id,))
    wishlist = cursor.fetchall()

    print("\n -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print("Book Name: {}\n     Author: {}\n".format(book[2], book[3]))

def show_books_to_add(cursor, user_id):
    """Display the books that are not in the user's wishlist"""
    query = (
        "SELECT book_id, book_name " 
        "FROM book " 
        "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = %s)"
    )
    cursor.execute(query, (user_id,))
    books_to_add = cursor.fetchall()