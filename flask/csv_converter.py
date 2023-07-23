import sqlite3
import csv

def create_dict(person):
    to_return = {"id": person[0], "firstName": person[1], "lastName": person[2], "lab": person[3], "date": person[4], "notes": person[5]}
    return to_return

def test():
    print("hi")

def convert():
    connection_to_database = sqlite3.connect('people.db')

    query_executor = connection_to_database.cursor()

    query_executor.execute('SELECT * FROM people')

    rows = query_executor.fetchall()

    data = []

    seen = []


    for row in rows:
        row_as_dict = create_dict(row)
        name = row_as_dict["firstName"]
        if name not in seen:
            seen.append(name)
            data.append(row_as_dict)
            
    with open('mycsv.csv', 'w', newline='') as f:  # Use 'wb' mode in Python 2.x
        field_names = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for my_dict in data:
            writer.writerow(my_dict)
convert()
    