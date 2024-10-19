from flask import Flask
from flask import redirect, url_for,render_template

#Create a Flask app
app = Flask(__name__)

#Creamos una ruta, sirve para indicar la dirección de la página
@app.route('/')#url
def index():
    return 'Flask esta funcionando!'

@app.route('/info')#url
def info():
    return "<h1>Información</h1>"

#Redireccionar a otra página
@app.route('/contacto/<redireccion>')#url
def contacto(redireccion=None):
    if redireccion is not None:
        return redirect(url_for('index')) #Redirecciona a la página principal
    else:
        return "<h1>Contacto</h1>"


@app.route('/acerca')#url
def acerca():
    return "<h1>Acerca de</h1>"

#Rutas con parametros
@app.route('/saludo/<nombre>')#url
def saludo(nombre):
    return f"""<h1>Hola {nombre}</h1> 
            <p>¿Cómo estas?</p>"""  

#Podemos indicar el tipo de dato que se espera en la url
@app.route('/suma/<int:num1>/<int:num2>')#url
def suma(num1,num2):
    return f""" <h1>Suma</h1>
            <p>El resultado de la suma es: {num1+num2}</p>"""

#Parametros opcionales
@app.route('/saludo2/<nombre>')#url
@app.route('/saludo2')#url
def saludo2(nombre="Invitado"):#valor por defecto
    return f"""<h1>Hola {nombre}</h1> 
            <p>¿Cómo estas?</p>"""

if __name__ == '__main__': #Checamos si el archivo es el principal
    app.run(debug=True) #Corremos la aplicación en modo debug, el modo debug nos permite ver los errores en la aplicación


