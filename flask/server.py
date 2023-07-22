from flask import Flask
import datetime
import json

x = datetime.datetime.now()

app = Flask(__name__)

# Generate a unique ID for each person
def generate_unique_id():
    return str(datetime.datetime.now().timestamp())

@app.route('/data')
def get_data():
    data = [
        {
            "id": generate_unique_id(),
            "firstName": "Tyler",
            "lastName": "Cushing",
            "lab": "AYC",
            "date": "9:53AM 9/10/22",
            "notes": "No notes"
        },
        {
            "id": generate_unique_id(),
            "firstName": "Eric",
            "lastName": "Roth",
            "lab": "AYC",
            "date": "9:53AM 9/10/22",
            "notes": "No notes"
        }
    ]
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    app.run(debug=True)