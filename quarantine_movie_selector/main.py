import functions as fn

users_dict = {"1": "USER_1", "2": "USER_2"}

while True:
    opt = fn.user_menu(users_dict)
    if opt == "exit":
        break
    user = users_dict[opt]
    while True:
        opt = fn.database_menu(user)
        if opt == "exit":
            break
        elif opt == "1":
            fn.show_database(user)
        elif opt == "2":
            fn.add_movie(user) 
        elif opt == "3":
            fn.remove_movie(user)
        elif opt == "4":
            fn.select_movie(user)