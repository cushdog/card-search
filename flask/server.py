from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/')
def root():
    return "This is root"

@app.route('/test')
def test():
    return "testing"

@app.route("/students", methods=["GET"])
def students():
    """
    Returns currently checked-in students. Currently just a dummy.
    """
    students = {
        'students': [
            {
                'firstName': 'Eric',
                'lastName': 'Roth',
                'lab': 'AYC',
                'date': '1690054337',
                'notes': 'None'
            }, 
            {
                'firstName': 'Tyler',
                'lastName': 'Cushing',
                'lab': 'AYC',
                'date': '1690054389',
                'notes': 'None'
            }
        ]
    }

    return students

if __name__=='__main__':
    app.run(host="localhost", port=5000)