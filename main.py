

def is_valid_credentials(u, pw):
    if u == "Robert" and pw == "password123":
        print("I love my Girlfriend over everything <3")
    else:
        print("Wrong credentials, please try again")
    
user = input("what is your name? ")
password = input("Password: ")

is_valid_credentials(user, password)
