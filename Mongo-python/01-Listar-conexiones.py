from pymongo import MongoClient

#conexion
conexion= "mongodb://admin:2603@localhost"

#usamos mongocliente para conectarnos
cliente = MongoClient(conexion)

#Creamos la base de datos
db_name=cliente["db1"]
db_name=cliente.db1

print(db_name)
