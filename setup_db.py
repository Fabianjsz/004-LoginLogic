import sqlite3 
import os

db_name = "ppab6.db"

def createTable(db, tableName):
    conn = sqlite3.connect(db)
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


def setupDb(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if tables:
        temp = input(f"The database '{name}' already exists and contains following tables: \n{listTables(name, tables)} \nWould you like to delete the DB? (Y/N)")
        
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
        print(f"The database '{name}' has been created.")
        conn.close()
        createTable(name)

    

createTable(db_name, "Test")
createTable(db_name, "Test2")
createTable(db_name, "Test3")

setupDb(db_name)

