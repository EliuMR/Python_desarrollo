#Python viene con un gestor de BD Sql sencillo SQLITE

import sqlite3

#Conexión
conexion = sqlite3.connect('pruebas.db')

#Crear cursor, para consultas
cursor = conexion.cursor()

#Crear tabla
campos= "id integer primary key autoincrement, titulo varchar(20), descripcion varchar(20), precio int(255)"
cursor.execute("create table if not exists productos("+campos+")")
#guardar cambios como consultas etc.
conexion.commit()

#Insertar datos
print("Insertando datos")
dato01="(null, 'Primer producto', 'Descripcion 1', 128),"
dato02="(null, 'Segundo producto', 'Descripcion 2', 14),"
dato03="(null, 'Tercero producto', 'Descripcion 3', 188),"
dato04="(null, 'Cuarto producto', 'Descripcion 4', 28)"
cursor.execute("insert into productos values "+dato01+dato02+dato03+dato04)
conexion.commit()

#leer
print("*"*50)
print("Consulta de los producto")
cursor.execute("select * from productos")
productos = cursor.fetchall()
for i in productos:
    print(i)
print("*"*50)
print("Consulta de productos con un filtro precio mayor a 100")
cursor.execute("select * from productos where precio>100")
productos = cursor.fetchall()
for i in productos:
    print(i)
print("*"*50)

#Borrar 
#en vez de muchas cadenas concatenadas para la consulta, puede hacerse multilena
print("Borrando productos con filtro")
cursor.execute("""
    delete from productos
    where titulo = 'Primer producto'
               """)
conexion.commit()
print("*"*50)
#Consulta
print("Consulta después de borrar")
cursor.execute("""
        select * from productos
               """)
productos=cursor.fetchall()
for i in productos:
    print(i)
print("*"*50)

#Actualizar datos
print("Update de algun producto")
cursor.execute("""
                update productos
                set titulo = 'Otro producto'
                where titulo = 'Tercero producto'
               """)
conexion.commit()
print("Consulta de datos:")
cursor.execute("""
                select * from productos
               """)
productos=cursor.fetchall()
for i in productos: print(i)
print("*"*50)

#Borrado de los elementos de la tabla
print("Borrando toda la tabla")
cursor.execute("""
        delete from productos
               """)
conexion.commit()
print("Consulta de datos:")
cursor.execute("""
                select * from productos
               """)
productos=cursor.fetchall()
for i in productos: print(i)
print("*"*50)


#cerrar conexion
conexion.close()
