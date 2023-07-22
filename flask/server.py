from flask import Flask, jsonify

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    """
    Append CORS headers to every request.

    NOTE: Unsafe for deplpoyment. Should only be used for development purposes.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'

    return response

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
    app.run(host="127.0.0.1", port=5000)