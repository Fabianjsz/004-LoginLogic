# Step 5.1: Storing credentials in a database

- [ ] get the amount of rows out of a table

# Step 6.1: Adding user into database

- [x] create function addUser()
- [x] ask user for username
- [x] ask user for password
- [x] hash password with sha256
- [x] save their name and password to database

## Step 6.2: adding improvements

- [x] Check if user is already in database; if true, ask for new username
- [x] hide password in text console
- [x] write a config file, where the programm will pull the database name from

## Step 6.3: adjusting main.py to new changes

- [x] fix potential errors in setup_db.py
- [x] adjust isValidCredentials to account for following:
- [x] Hash the users password as before
- [x] check for userdata via a query to the main database
- [x] if it finds a user: return true; else: False
