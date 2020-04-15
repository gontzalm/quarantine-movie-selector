import os
import json
from random import choice

def clear():
    """Clear terminal on Windows system."""
    os.system("cls")


def show_header(disp_width=79):
    """Show the program header."""
    program_name = "QUARANTINE Movie Selector"
    author = "Gontz"
    version = "1.1"
    header = f"[{program_name} v{version} by {author}]"
    print(header.center(disp_width, "_"))
    print()


def user_menu(users):
    """Show the main menu."""
    prompt = "User number:"
    while True:
        clear()
        show_header()
        print("Select a user (type 'exit' to quit):\n")
        for num, user in users.items():
            print(f"\t{num}. {user}")
        opt = input(f"\n{prompt} ")
        if opt in users.keys() or opt.lower() == "exit":
            break
        else:
            continue
    return opt


def show_login(user, disp_width=79):
    """Show login info."""
    login_info = f"Logged in as {user}."
    print(login_info.center(disp_width))
    print()

def database_menu(user):
    """Show database menu to the specified user"""
    prompt = "Option number:"
    while True:
        clear()
        show_header()
        show_login(user)
        print("Select an option (type 'exit' to log out):\n")
        print("\t1. Show your database")
        print("\t2. Add a movie to your database")
        print("\t3. Remove a movie from your database")
        print("\t4. Select a random movie from your database")
        opt = input(f"\n{prompt} ")
        if opt.lower() in ["1", "2", "3", "4", "exit"]:
            break
        else:
            continue
    return opt


def show_database(user, disp_width=79):
    """Show a user's database"""
    clear()
    show_header()
    show_login(user)
    opt_info = "[SHOW DATABASE]" 
    print(opt_info.center(disp_width, "-"))
    print()
    filename = "database_" + user.lower() + ".json"
    error_msg = "ERROR: There is no database file available."
    try:
        with open(filename) as f:
            database = json.load(f)
    except FileNotFoundError:
            print(error_msg)
    else:
        print("Movie list:\n")
        for movie in database["available"]:
            print(f"- {movie.title()}")
        film_count = len(database["available"])
        print(f"\nNº of films: {film_count}")
    input("\nPress ENTER key to continue.")

    
def add_movie(user, disp_width=79):
    """Add a movie to a user's database"""
    clear()
    show_header()
    show_login(user)
    opt_info = "[ADD MOVIE]"
    print(opt_info.center(disp_width, "-"))
    print()
    filename = "database_" + user.lower() + ".json"
    prompt = "Enter the title:"
    movie = input(f"{prompt} ")
    movie = movie.lower()
    try: 
        with open(filename) as f:
            database = json.load(f)
    except FileNotFoundError:
        database = {"available": [movie], "removed": []}
        with open(filename, "w") as f:
            json.dump(database, f)
        print(f"\nMovie {repr(movie.title())} added succesfully.")
    else:
        if movie not in database["available"] and movie not in database["removed"]:
            database["available"].append(movie)
            database["available"].sort()
            with open(filename, "w") as f:
                json.dump(database, f)
            print(f"\nMovie {repr(movie.title())} added succesfully.")
        else:
            if movie in database["available"]:
                print(f"\nThe movie {repr(movie.title())} is already in your database.")
            if movie in database["removed"]:
                print(f"\nThe movie {repr(movie.title())} has already been watched or removed previously.")
    input("\nPress ENTER key to continue.")


def rm_movie(movie, database, filename):
    """Remove a movie from a database in filename"""
    database["available"].remove(movie)
    database["removed"].append(movie)
    database["removed"].sort()
    with open(filename, "w") as f:
        json.dump(database, f)


def remove_movie(user, disp_width=79):
    """Remove a movie from a user's database"""
    clear()
    show_header()
    show_login(user)
    opt_info = "[REMOVE MOVIE]"
    print(opt_info.center(disp_width, "-"))
    print()
    filename = "database_" + user.lower() + ".json"
    prompt = "Enter the title:"
    error_msg = "ERROR: There is no database file available."
    try: 
        with open(filename) as f:
            database = json.load(f)
    except FileNotFoundError:
        print(error_msg)
    else:
        movie = input(f"{prompt} ")
        movie = movie.lower()
        if movie in database["available"]:
            rm_movie(movie, database, filename)
            print(f"\nMovie {repr(movie.title())} removed succesfully.")
        else:
            print(f"\nThe movie {repr(movie.title())} is not in your database.")
    input("\nPress ENTER key to continue.")


def select_movie(user, disp_width=79):
    """Select a random movie from a user's database"""
    clear()
    show_header()
    show_login(user)
    opt_info = "[SELECT RANDOM MOVIE]"
    print(opt_info.center(disp_width, "-"))
    print()
    filename = "database_" + user.lower() + ".json"
    error_msg_1 = "ERROR: There is no database file available."
    error_msg_2 = "ERROR: There is no available movies in your database."
    try:
        with open(filename) as f:
            database = json.load(f)
    except FileNotFoundError:
        print(error_msg_1)
    else:
        if database["available"]:
            selection = choice(database["available"])
            print(f"The selected movie is: {repr(selection.title())}")
            print("\nAre you going to watch it? (y/n): ")
            while True:
                answer = input()
                if answer.lower() in ["y", "n"]:
                    break
            if answer == "y":
                print(f"\nI'm glad you liked my selection!\nThis movie will be removed from {user}'s database.")
                rm_movie(selection, database, filename)
            else:
                print(f"\nI'm sorry you didn't like my selection!\n{user}, try to add better movies to your database.")
        else:
            print(error_msg_2)
    input("\nPress ENTER key to continue.")