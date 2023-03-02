# ---- Menu Documentation ----
"""
GUI to connect the database.py with run.py in a friendly way for a user.
"""
# ---- Menu Documentation ----

# ---- Imports ----
import helpers
import database as db
# ---- End Imports ----

def init():
    while True:
        helpers.clean_screen()  # clean screen

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
        helpers.clean_screen()

        if option == '1':
            print("Displaying the clients...\n")
            for client in db.Clients.l:
                print(client)

        elif option == '2':
            print("Searching the client...\n")
            ssn = helpers.read_text(3, 3, "DNI (2 numbers and 1 letter)").upper()
            client = db.Clients.search(ssn)
            print(client) if client else print("Client no found.")

        elif option == '3':
            print("Adding the client...\n")

            ssn = None
            while True:
                ssn = helpers.read_text(3, 3, "DNI (2 numbers and 1 letter)").upper()
                if helpers.valid_ssn(ssn, db.Clients.l):
                    # if the ssn introduced is valid.
                    break

            name = helpers.read_text(2,30, "Name (from 2 to 30 letters)").capitalize()
            last_name = helpers.read_text(2,30, "Last Name (from 2 to 30 letters)").capitalize()
            db.Clients.create(ssn, name, last_name)
            print("Client created successfully.")

        elif option == '4':
            print("Modifying the client...\n")
            ssn = helpers.read_text(3, 3, "DNI (2 numbers and 1 letter)").upper()
            client = db.Clients.search(ssn)
            if client:
                name = helpers.read_text(2, 30, f"Name (from 2 to 30 letters) [{client.name}]").capitalize()
                last_name = helpers.read_text(2, 30, f"Last Name (from 2 to 30 letters) [{client.last_name}]").capitalize()
                db.Clients.modify(client.ssn, name, last_name)
                print("Client modified successfully.")
            else:
                print("Client not found.")

        elif option == '5':
            print("Deleting the client...\n")
            ssn = helpers.read_text(3, 3, "DNI (2 numbers and 1 letter)").upper()
            print("Client deleted successfully.") if db.Clients.delete(ssn) else print("Client not found.")

        elif option == '6':
            print("Bye!\n")
            break
        else:
            print("Invalid option!")

        input("\nPress Enter to continue...")