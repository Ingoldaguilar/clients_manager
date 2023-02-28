# ---- Menu Documentation ----
"""
GUI to connect the database.py with run.py in a friendly way for a user.
"""
# ---- Menu Documentation ----

# ---- Imports ----
import os
# ---- End Imports ----

def init():
    while True:
        os.system('cls')  # clean screen

        print("==================================")
        print("  Welcome to the Clients Manager  ")
        print("==================================")
        print("[1] Display the clients           ")
        print("[2] Search a client               ")
        print("[3] Add a client                  ")
        print("[4] Modify a client               ")
        print("[5] Delete a client               ")
        print("[6] Exit                          ")
        print("==================================")

        option = input("> ")
        os.system("cls")

        if option == '1':
            print("Displaying the clients...\n")
            # TODO List clients in the menu
        elif option == '2':
            print("Searching the client...\n")
            # TODO
        elif option == '3':
            print("Adding the client...\n")
            # TODO
        elif option == '4':
            print("Modifying the client...\n")
            # TODO
        elif option == '5':
            print("Deleting the client...\n")
            # TODO
        elif option == '6':
            print("Bye!\n")
            break
        else:
            print("Invalid option!")

        input("\nPress Enter to continue...")