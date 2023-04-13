from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Ejercicios python en FLASK WEB 2</h1>'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'hola {0}!'.format(nombre)

if __name__ == "__main__":
    app.run(debug=True)