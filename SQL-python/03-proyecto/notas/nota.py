import usuarios.conexion as conexion

database,cursor = conexion.conectar()

class Nota:
    def __init__(self,usuario_id,titulo,descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "insert into notas values (null,%s,%s,%s,now())"
        nota = [self.usuario_id,self.titulo,self.descripcion]
        cursor.execute(sql,nota)
        database.commit()
        return (cursor.rowcount,self) 

    def mostrar(self):
        sql = "select * from notas where usuario_id=%s"
        user_id = [self.usuario_id]
        cursor.execute(sql,user_id)
        resultado = cursor.fetchall()
        if resultado:
            return resultado, True
        else:
            return resultado, False

    def borrar(self,id_nota):
        sql = "delete from notas where (id=%s and usuario_id=%s)"
        ids=[id_nota,self.usuario_id]
        cursor.execute(sql,ids)
        database.commit()
        return cursor.rowcount

    def editar_descripcion(self,id_nota,descripcion_nueva):
        sql = "update notas set descripcion=%s where (id=%s and usuario_id=%s)"
        nota = [descripcion_nueva,id_nota,self.usuario_id]
        cursor.execute(sql,nota)
        database.commit()
        return cursor.rowcount
    
    def editar_titulo(self,id_nota,titulo_nuevo):
        sql = "update notas set titulo=%s where (id=%s and usuario_id=%s)"
        nota = [titulo_nuevo,id_nota,self.usuario_id]
        cursor.execute(sql,nota)
        database.commit()
        return cursor.rowcount
       
