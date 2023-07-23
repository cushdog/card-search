import sqlite3

connection_to_database = sqlite3.connect('people.db')

query_executor = connection_to_database.cursor()

query_executor.execute('SELECT * FROM people')

rows = query_executor.fetchall()

for row in rows:
    print(row)
    print(type(row))