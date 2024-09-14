import mysql.connector

#conexíon base de datos
database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "2603",
        database = "master_python" #Siempre y cuando esté creada
        )
#Conexión data vase
print("Database usada")
print(database)

#Crear base datos
cursor = database.cursor(buffered=True)
cursor.execute("""
                create database if not exists master_python
               """)

#Mostar bases de datos
print("Mostras la bases de datos")
cursor.execute("""
                show databases;
               """)
for i in cursor:
    print(i)

print("*"*50)

#crear tablas
print("Creando tabla vehiculos")
cursor.execute(
        """
        create table if not exists vehiculos(
        id int(10) auto_increment not null,
        marca varchar(30) not null,
        modelo varchar(40) not null,
        precio int(10) not null,
        constraint pk_vehiculo primary key(id)
        )
        """
        )
cursor.execute("Show tables")
for i in cursor:
    print(i)

print("*"*50)
print("Insertar registros")
cursor.execute(
        """
        insert into vehiculos values
        (null,'BMW','Q5',2500)

        """
        )
database.commit()


coches = [
        ('Seat','Ibiza',4000),
        ('Renault','Clio',1500),
        ('Mercedes','Clase C',5333)
        ]
cursor.executemany(
        """
        insert into vehiculos values
            (null,%s,%s,%s)
        """,coches)
database.commit()
print("*"*50)

#Leemos la tabla
print("Leemos la tabla")
cursor.execute("""
                select * from vehiculos
               """)
consulta = cursor.fetchall()
for i in consulta:
    print(i)
print("*"*50)

#Leemos la tabla
print("Leemos la tabla precio mayores a 2000")
cursor.execute("""
                select * from vehiculos where precio>2000
               """)
consulta = cursor.fetchall()
for i in consulta:
    print(i)
print("*"*50)

#Borramos datos
print("Borramos los vehiculos cuya marca se MMW")
cursor.execute(
        """
        delete from vehiculos where marca= 'BMW'
        """
        )
database.commit()
cursor.execute("""
                select * from vehiculos
               """)
consulta = cursor.fetchall()
for i in consulta:
    print(i)
print("*"*50)

#Actualizamos
print("Actualizamos el precio de lo vehiculos cuyo precio sea igual a 1500")
cursor.execute("""
                update vehiculos
                set precio=00 where precio=1500
               """)
database.commit()
cursor.execute("""
                select * from vehiculos
               """)
consulta = cursor.fetchall()
for i in consulta:
    print(i)
print("*"*50)

#Borramos toda la tabla
print("Borramos todos los registros de la base de datos")
cursor.execute("""delete from vehiculos""")
database.commit()
cursor.execute("""
                select * from vehiculos
               """)
consulta = cursor.fetchall()
for i in consulta:
    print(i)
print("*"*50)
