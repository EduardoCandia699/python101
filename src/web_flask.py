import csv
from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/json', methods=['GET'])
def jaison():
    results = []
    with open('data/ejemplo.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
    return jsonify(results)

@app.route("/", methods=['GET'])

def saludo():
    return ("HOLA MARIA")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")