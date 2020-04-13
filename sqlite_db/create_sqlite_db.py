import sqlite3


class DatabaseBuilder:

    def __init__(self, database_addr):
        self.database_addr = database_addr
        self.database = sqlite3.connect(self.database_addr)
        self.cursor = self.database.cursor()

    def create_database(self):
        with open('../create_tables.sql', 'r') as file:
            script = file.read()
        self.cursor.executescript(script)

        with open('../insert_data.sql', 'r') as data:
            insert = data.read()
        self.cursor.executescript(insert)

        self.cursor.close()
        self.database.close()

    def clear_database(self):
        with open('../create_tables.sql', 'r') as file:
            script = file.read()
        self.cursor.executescript(script)

        self.cursor.close()
        self.database.close()
