from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

""" @app.route('/')
def hello_geek():
    return '<h1>Ejercicios python en FLASK WEB 2</h1>' """

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'hola {0}!'.format(nombre)

@app.route('/datos')
def datos():
    """ print(request.args) """
    """ en la ruta se ingresa http://127.0.0.1:5000/datos?val1=ACA EL VALOR OPTENIDO """
    val1 = request.args.get('val1')
    """ obtiene un request desde la ruta con los lavores en variables """
    return 'estos son los datos: {0}'.format(val1)

@app.route('/eje1', methods=['GET','POST'])
def eje1():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@'
    }
    if request.method == "POST":
        """ print(request.form['a']) """
        a=request.form['a']
        a = int(a)
        b=request.form['b']
        b = int(b)
        z=a+b
        return 'LA SUMA ES: {0}'.format(z)
    else:
        return render_template('eje1.html',data=data)

@app.route('/')
def index():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@'
    }
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.add_url_rule('/', view_func=index)
    app.run(debug=True)