from pymongo import MongoClient
from bson.objectid import ObjectId


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
usuario = credenciales['USER']
password = credenciales['PASS']
client = MongoClient(f'mongodb://{usuario}:{password}@localhost:27017/?authSource=admin')
db = client['dav_db']  # Reemplaza 'dav_db' con el nombre de tu base de datos


# Crear un documento de ejemplo para insertar
documento_original = {
    'nombre': 'Ejemplo',
    'edad': 30,
    'correo': 'ejemplo@example.com'
}

# Insertar un documento en una colección
def insertar_documento(doc):
    # Selecciona una colección existente o créala si no existe
    dav_db = db['dav_db']

    # Insertar el documento en la colección
    resultado = dav_db.insert_one(doc)

    # Imprimir el ID del documento insertado
    print(f"Documento insertado con ID: {resultado.inserted_id}")
    return resultado.inserted_id

# Leer todos los documentos de una colección
def leer_documentos():
    dav_db = db['dav_db']

    # Leer todos los documentos de la colección
    documentos = dav_db.find()

    # Imprimir los documentos obtenidos
    for documento in documentos:
        print(documento)

# Función para buscar un documento por ID
def buscar_documento_por_id(documento_id):
    dav_db = db['dav_db']

    # Buscar el documento por su ID
    documento_encontrado = dav_db.find_one({"_id": ObjectId(documento_id)})
    return documento_encontrado  # Retorna el documento encontrado

# Función para comparar los datos originales con los recuperados
def comparar_documentos(documento_original, documento_recuperado):
    # Compara los datos originales con los datos recuperados
    if documento_original == documento_recuperado:
        print("Los datos son iguales.")
    else:
        print("Los datos son diferentes.")


# Llamar a las funciones para insertar y leer documentos
doc_id = insertar_documento(documento_original)
documento_recuperado = buscar_documento_por_id(doc_id)
comparar_documentos(documento_original, documento_recuperado)
