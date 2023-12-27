from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)


# Ejecuta la aplicación si este archivo es el archivo principal
if __name__ == '__main__':
    app.run(debug=True)
