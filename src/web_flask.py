from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/json', methods=['GET'])
def jaison():
    contenido={"id":1, "nombre":"Jamil", "Apellido":"Candia"}
    contenido2 = {"id": 2, "nombre": "no es Jamil", "Apellido": "no es Candia"}
    lista = (contenido, contenido2)
    return jsonify(lista)

@app.route("/", methods=['GET'])

def saludo():
    return ("HOLA MARIA")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")