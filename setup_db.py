import os
import sqlite3
import hashlib


from dotenv import find_dotenv, load_dotenv
from getpass import getpass
from pathlib import Path



global db_name


# Fetch .env file location
dotenv_path = find_dotenv()

# Load up entries of .env
load_dotenv(dotenv_path)

# Load .env database name into dbName variable
dbName = os.getenv("dbName")



def passwordHasher(pw):
    hashed = hashlib.sha256(pw.encode("utf-8"))
    hashed = hashed.hexdigest()
    return hashed


def is_valid_credentials(a, b):
    temp = 0
    while temp < 3:
        con = sqlite3.connect(dbName)
        cur = con.cursor()
        cur.execute(f"SELECT user FROM users WHERE user = '{a}' AND password_hash = '{passwordHasher(b)}'")
        if cur.fetchall():
            return True
        else:
            return False
    else:
        return False


# Function which returns every table in given database
def checkDb():
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables


# Function which sets up database
def setupDb():
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    cur.execute(f"CREATE TABLE users(user VARCHAR, password_hash VARCHAR);")
    con.commit()
    
    dbPath = Path(dbName).resolve() 

    return dbPath


# function which adds user to database
def addUser():
    
    while True:
        con = sqlite3.connect(dbName)
        cur = con.cursor()


        userName = input("Enter Username ")
        cur.execute(f"SELECT user FROM users WHERE user = '{userName}'")
        if cur.fetchall() == []:
            password = getpass("Select password ")
            cur.execute(f"INSERT INTO users(user, password_hash) VALUES('{userName}', '{passwordHasher(password)}') ")
            con.commit()
            con.close()
            print(f"Successfully added user {userName} into database!")
            break

        else:
            print("user already in database")
