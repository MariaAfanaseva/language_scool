import sqlite3

database = sqlite3.connect('school_db.sqlite')
cursor = database.cursor()

with open('create_tables.sql', 'r') as file:
    script = file.read()
cursor.executescript(script)

with open('insert_data.sql', 'r') as data:
    insert = data.read()
cursor.executescript(insert)

cursor.close()
database.close()
