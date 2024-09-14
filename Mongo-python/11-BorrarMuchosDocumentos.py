from pymongo.mongo_client import MongoClient
import pprint
uri = "mongodb+srv://eliumoreno:morenoramirez@cluster0.zqmna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! \n")
except Exception as e:
    print(e)

dbname = client["db1"]
print("La base de datos es: ",str(dbname),"\n")

#Colección a usar o crear
propiedades= dbname["facturas"]

print("Las colección es: ",str(propiedades),"\n")

#documento a borrar
documento = {"total":{"$gt":50}}

# Verificar documentos que coinciden
documentos = propiedades.find(documento)
print("Documentos que coinciden con el filtro:")
for doc in documentos:
    print(doc)


#Eliminar documentos
resultado = propiedades.delete_many(documento)

#Identificar los documentos localizados y los borrados
print("Cantidad de documentos eliminados")
pprint.pprint(resultado.deleted_count)
