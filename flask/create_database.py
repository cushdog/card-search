import sqlite3

connection_to_database = sqlite3.connect('people.db')

query_executor = connection_to_database.cursor()

query_executor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        lab TEXT NOT NULL,
        date TEXT NOT NULL,
        notes TEXT NOT NULL
    )
''')

connection_to_database.commit()     
connection_to_database.close()
