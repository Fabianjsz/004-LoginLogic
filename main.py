
users = ["Fabian", "Emmi"]
passwords = ["Emmi0707", "penispenis123"]

def is_valid_credentials(u, pw):
    if u in users:
        index = users.index(u)
        if pw == passwords[index]:
            if u == "Fabian":
                print("I love my girlfriend more than anything <3")
            elif u == "Emmi":
                print("I love my Boyfriend >:(")
    
    else:
        print("Wrong credentials, please try again")
    
user = input("what is your name? ")
password = input("Password: ")

is_valid_credentials(user, password)
