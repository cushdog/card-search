import flask

app = flask.Flask(__name__)

@app.route('/students/')
def students():
    """
    Returns currently checked-in students

    NOTE: This should only be used for testing right now
    """
    return {
        'students': [
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
    }