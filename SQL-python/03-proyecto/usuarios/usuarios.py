import hashlib
import usuarios.conexion as conexion

database,cursor= conexion.conectar()

#Métodos de  usuario
class Usuario:
    def __init__(self,nombre,apellidos,email,password):
        self.nombre     = nombre
        self.apellidos  = apellidos
        self.email      = email
        self.password   = password

    def registrar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #password cifrado
        sql = "insert into usuarios values (null,%s,%s,%s,%s,curdate())"
        usuario = (self.nombre,self.apellidos,self.email,cifrado.hexdigest())
        try:
            cursor.execute(sql,usuario)
            database.commit()
            result =  [cursor.rowcount,self]
        except:
            result = [0,self]

        return result

    def identificar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #password cifrado
        sql = "select * from usuarios where email=%s and password=%s"
        usuario = (self.email,cifrado.hexdigest())#Datos a sustituir en la consulta
        try:
            cursor.execute(sql,usuario) #consulta
            resultado = cursor.fetchone()
        
        except:
            resultado = None
        return resultado
