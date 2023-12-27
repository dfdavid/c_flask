from flask import Flask, request, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta (endpoint) para la página principal
@app.route('/')
def index():
    return '¡Bienvenido a mi server!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        hard_usr = 'test'
        hard_pwd = '1234'

        usr = request.form['username']
        pwd = request.form['password']

        if hard_usr == usr and hard_pwd == pwd:
            return 'Login successful'
        else:
            return 'Login failed'

    return render_template('login.html')

# Ejecuta la aplicación si este archivo es el archivo principal
if __name__ == '__main__':
    app.run(debug=True)