from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/convert-data')
def convert_data():
    try:
        # Run the Python script using subprocess
        subprocess.run(['python', '../flask/csv_converter.py'], check=True)
        return jsonify({"message": "Data conversion successful."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()