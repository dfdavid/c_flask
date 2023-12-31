from flask import Flask, abort, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# ------------------Borrar esto cuando este n uso la base de datos ---------------------------------------------------------------------------
# ------------------Borrar esto cuando este n uso la base de datos ---------------------------------------------------------------------------
# ------------------Borrar esto cuando este n uso la base de datos ---------------------------------------------------------------------------

# Datos de ejemplo (podrían ser datos de una base de datos)
usuarios = [
    {'id': 1, 'nombre': 'Micolini, Orlando', 'rol': 'admin', 'RFID': 'null'},
    {'id': 2, 'nombre': 'Carranza, Agustin', 'rol': 'normal', 'RFID': 'null'},
    # Agrega más datos según sea necesario
]

# ------------------Borrar esto cuando este n uso la base de datos ---------------------------------------------------------------------------
# ------------------Borrar esto cuando este n uso la base de datos ---------------------------------------------------------------------------
# ------------------Borrar esto cuando este n uso la base de datos ---------------------------------------------------------------------------

# Configuración de la conexión a MongoDB
# Función para leer las credenciales del archivo .env

credenciales = {}
with open('.env', 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        if linea.__contains__('USER') or linea.__contains__('PASS'):
            clave, valor = linea.strip().split('=')
            credenciales[clave] = valor
    

# Obtener las credenciales del archivo .env
usuario = credenciales.get('usuario')
password = credenciales.get('password')

client = MongoClient('mongodb://localhost:27017/')
db = client['mi_base_de_datos']  # Reemplaza 'mi_base_de_datos' con el nombre de tu base de datos

# Obtiene el nombre del archivo .py
nombre_archivo = os.path.basename(__file__)
nombre_api = nombre_archivo[:-3]  # Elimina la extensión .py

@app.route('/', methods=['GET'])
def dav_home():
    api_info = {
        "nombre_api": nombre_api,
        "version": "1.0"
    }
    return jsonify(api_info)

# Ruta para obtener todos los usuarios
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Ruta para obtener un usuario por su ID
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    usuario = next((p for p in usuarios if p['id'] == usuario_id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({'mensaje': 'usuario no encontrado'}), 404

# Ruta para crear un usuario
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    # Verificar si el contenido de la solicitud es JSON
    if not request.json:
        abort(400, 'La solicitud no contiene datos JSON')
    
    # Validar si el JSON tiene la estructura esperada (nombre y rol)
    expected_keys = {'nombre', 'rol', 'RFID'}
    received_keys = set(request.json.keys())
    if not expected_keys.issubset(received_keys):
        abort(400, 'El JSON recibido no tiene la estructura esperada')
    
    # Si la validación pasa, crear un nuevo usuario
    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': request.json['nombre'],
        'rol': request.json['rol'],
        'RFID': request.json['RFID']
    }
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

if __name__ == '__main__':
    app.run(debug=True)
