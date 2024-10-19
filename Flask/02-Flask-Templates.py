from flask import Flask, request, flash
from flask import redirect, url_for,render_template
from datetime import datetime
from flask_mysqldb import MySQL

#Create a Flask app
app = Flask(__name__)

#Configuración de la clave secreta
app.secret_key = 'mysecret'


#Conexion a base de datos
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2603'
app.config['MYSQL_DB'] = 'Flask'
mysql = MySQL(app) #Inicializamos la conexión



#Context processor
#Sirve para pasar variables a todos los templates
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    } 


#Creamos una ruta, sirve para indicar la dirección de la página
@app.route('/')#url
def index():
    edad = 15
    nombre="Juan"
    return render_template('index.html',
                           edad=edad,
                           nombre=nombre,
                            variable="Hola desde Flask",
                            lista=[1,2,3,4,5],
                           ) #Renderizamos el archivo index.html

@app.route('/info')#url
def info():
    return render_template('Informacion.html') #Renderizamos el archivo Informacion.html

#Redireccionar a otra página
@app.route('/contacto/<redireccion>')#url
def contacto(redireccion=None):
    if redireccion is not None:
        return redirect(url_for('index')) #Redirecciona a la página principal
    else:
        return "<h1>Contacto</h1>"


@app.route('/acerca')#url
def acerca():
    return render_template('AcercaDe.html') #Renderizamos el archivo Acerca.html

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
    #las variables que se pasan a render_template se pueden utilizar en el archivo html
    return render_template('saludo.html',
            nombre=nombre) #Renderizamos el archivo saludo.html

#Insertar datos en la base de datos
@app.route('/insertar')#url
def insertar():
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO coches (id,marca,precio,ciudad,modelo) VALUES (NULL,"Nissan",100000,"CDMX","Versa")')
    mysql.connection.commit()
    return redirect(url_for('index'))

#Formulario para insertar datos
@app.route('/insertar-datos',methods=['GET','POST'])#url
def insertar_datos():    
    if request.method == 'POST':
        #Accedemos a los datos del formulario
        
        modelo = request.form['modelo']
        marca = request.form['marca']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        #Insertamos los datos en la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO coches (id,marca,precio,ciudad,modelo) VALUES (NULL,%s,%s,%s,%s)',(marca,precio,ciudad,modelo))
        mysql.connection.commit() #Guardamos los cambios
        
        #Mensaje flash
        flash('Coche insertado correctamente')


        return redirect(url_for('index'))

    return render_template('insertar-datos.html')


#Obtener datos de la base de datos
@app.route('/lista-coches')#url
def lista_coches():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM coches')
    datos = cur.fetchall() #Obtenemos los datos
    return render_template('lista-coches.html',coches=datos)

@app.route('/coche/<id>')#url
def coche(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM coches WHERE id = %s',(id))
    datos = cur.fetchall()
    cur.close()
    return render_template('coche.html',datos=datos)

@app.route('/eliminar/<id>')#url
def eliminar(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM coches WHERE id = %s',(id))
    mysql.connection.commit()
    cur.close()
    flash('Coche eliminado correctamente')
    return redirect(url_for('lista_coches'))


@app.route('/editar/<id>',methods=['GET','POST'])#url
def editar(id):
    if request.method == 'POST':
        modelo = request.form['modelo']
        marca = request.form['marca']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        cur = mysql.connection.cursor()
        cur.execute('UPDATE coches SET modelo=%s,marca=%s,precio=%s,ciudad=%s WHERE id=%s',(modelo,marca,precio,ciudad,id))
        mysql.connection.commit()
        flash('Coche actualizado correctamente')
        return redirect(url_for('lista_coches'))

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM coches WHERE id = %s',(id))
    datos = cur.fetchall()
    print(datos)
    cur.close()
    return render_template('editar.html',coche=datos)

if __name__ == '__main__': #Checamos si el archivo es el principal
    app.run(debug=True) #Corremos la aplicación en modo debug, el modo debug nos permite ver los errores en la aplicación


