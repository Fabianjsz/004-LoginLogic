from getpass import getpass
import sqlite3
import hashlib
import os

global db_name, tableName


db_name = "ppab6.db"
initTable = "users"


def passwordHasher(pw):
    hashed = hashlib.sha256(pw.encode("utf-8"))
    hashed = hashed.hexdigest()
    return(hashed)


def createTable(tableName):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE '{tableName}'(user VARCHAR, password_hash VARCHAR);")
    conn.commit()
    conn.close()


def listTables(name, fetch):
    #Take name of tables and put the sum after and return a string with all tables 
    tables = ""

    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    print(fetch)
    
    conn.close()
    return tables


def setupDb(tableName):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if tables:
        temp = input(f"The database '{tableName}' already exists and contains following tables: \n{listTables(tableName, tables)} \nWould you like to delete the DB? (Y/N)")
        
        if temp == "n" or temp == "N":
            conn.close()
            print("Database was not deleted")
        elif temp == "y" or temp == "Y":
            conn.close()
            os.remove(db_name)
            print("Database has been removed.")
        else:
            raise Exception

    else:
        print(f"The database '{db_name}' has been created.")
        conn.close()
        createTable(initTable)


def addUser():
    while True:
        userName = input("Enter Username ")
        password = getpass("Select password ")

        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute(f"SELECT user FROM users WHERE user = '{userName}'")
        temp = cur.fetchall()
        print(temp)

        if temp != []:
            continue

        else:
            cur.execute(f"INSERT INTO users(user, password_hash) VALUES('{userName}', '{passwordHasher(password)}') ")
            con.commit()
            con.close()
            print(f"Successfully added user {userName} into database!")
            break 




setupDb(db_name)

addUser()


