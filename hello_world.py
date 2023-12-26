from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta (endpoint) para la página principal
@app.route('/')
def index():
    return '¡Bienvenido a mi server!'

@app.route('/sa')
def spurs():
    return render_template('spurs.html')

# Ejecuta la aplicación si este archivo es el archivo principal
if __name__ == '__main__':
    app.run(debug=True)

