import hashlib
from setup_db import *



users = ["Emmi", "Fabian"]
passwords = ["8fe29b9687d13858578b19e2de262c42d1ad13c9e50aea5c8a4f50aece775479", "112851505944c52438aee6c8b39e3cc4cfed418cff97fb73b862b63d8b459aec"]


def passwordHasher(pw):
    hashed = hashlib.sha256(pw.encode("utf-8"))
    hashed = hashed.hexdigest()
    return(hashed)




def is_valid_credentials(u, pw):
    if u in users:
        index = users.index(u)
        if str(passwordHasher(pw)) == passwords[index]:
            return True
    else:   
        return False
    





user = input("what is your name? ")
password = input("Password: ")

print(is_valid_credentials(user, password))


