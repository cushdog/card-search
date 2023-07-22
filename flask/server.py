from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/students/", methods=['GET'])
@cross_origin(origin='*')
def students():
    """
    Returns currently checked-in students

    NOTE: This should only be used for testing right now
    """
    students = [
        {
            'firstName': 'Eric',
            'lastName': 'Roth',
            'lab': 'AYC',
            'date': '1690054337',
            'notes': 'None'
        }, {
            'firstName': 'Tyler',
            'lastName': 'Cushing',
            'lab': 'AYC',
            'date': '1690054389',
            'notes': 'None'
        }
    ]

    return jsonify(students)

if __name__=='__main__':
    app.run(debug=True)