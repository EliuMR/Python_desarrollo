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

#documento a modificar
documento = {"_id":"10006546"}

#cambio a realizar, poner nocher minimas a 1
cambio={"$set":{"minimum_nights":1}}

#modificar documento
resultado = propiedades.update_one(documento,cambio)

#identificar los documentos y los modificados
print("Cuántas filas a localizado")
pprint.pprint(resultado.matched_count)
print("Cuántas filas has modificado")
pprint.pprint(resultado.modified_count)

#Modificación
pprint.pprint(propiedades.find_one(documento)["minimum_nights"])
