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

dbname = client["sample_airbnb"]
print("La base de datos es: ",str(dbname),"\n")

#Colección a usar o crear
propiedades= dbname["listingsAndReviews"]

print("Las colección es: ",str(propiedades),"\n")

#documento a borrar
documento = {"_id":"10006546"}

#Eliminar documento
resultado = propiedades.delete_one(documento)

#Identificar los documentos localizados y los borrados
print("Cantidad de documentos eliminados")
pprint.pprint(resultado.deleted_count)
