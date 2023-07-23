from flask import Flask, jsonify
import datetime
import json
import sqlite3
import subprocess
import csv_converter as csv_thing

x = datetime.datetime.now()

def insert_into_db(firstName, lastName, lab, date, notes):
    connection_to_database = sqlite3.connect('people.db')
    query_executor = connection_to_database.cursor()
    
    query_executor.execute('''
        INSERT INTO people (firstName, lastName, lab, date, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (firstName, lastName, lab, date, notes))
    
    connection_to_database.commit()
    
    connection_to_database.close()

insert_into_db('Tyler','Cushing','AYC','9/10/23','No notes')
insert_into_db('Eric','Tester','AYC','9/10/23','No notes')

app = Flask(__name__)

# Generate a unique ID for each person
def generate_unique_id():
    return str(datetime.datetime.now().timestamp())

def create_dict(person):
    to_return = {"id": person[0], "firstName": person[1], "lastName": person[2], "lab": person[3], "date": person[4], "notes": person[5]}
    return to_return

@app.route('/data')
def get_data():

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

    return json.dumps(data, indent=4)

@app.route('/convert-data')
def convert_data():
    try:
        csv_thing.convert()
        return jsonify({"message": "Data conversion successful."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)