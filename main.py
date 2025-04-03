import sys
from setup_db import *

#dbname = ppab6.db

# main function which links funcitons to switch cases
def loginLogic():
    while True:
        if checkDb() == []:
            print(f"\nNo database has been found on system.\nCreating database in {setupDb()}")
        else:
            select = input("\nWhich action would you like to take?\n\n1. Login \n2. add user\n")
            # switch-case for logging in 
            if select == "1":
                user = input("username: ")
                credential = input("password: ")
                if is_valid_credentials(user, credential):
                    print(f"logged in as {user}")
                    input()
                    sys.exit()
                else:
                    print("wrong credentials, please try again")

                

            # switch-case for adding a new user
            elif select == "2":
                addUser()

            else:
                break


if __name__ == "__main__":

    loginLogic()
