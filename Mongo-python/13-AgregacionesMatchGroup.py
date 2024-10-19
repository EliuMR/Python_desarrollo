from pymongo.mongo_client import MongoClient
import pprint
uri = "mongodb+srv://<usuario>:<contraseña>@<cluster-url>/<nombre_base_datos>?retryWrites=true&w=majority"

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

#Etapa 1: Precio mayor o igual 100
match = {"$match":{"price":{"$gte":100}}}

#Etapa 2:Vamos a agrupar por tipo de propiedad y averiguar el precio medio
grupo = {"$group": {"_id":"$property_type","precio_medio":{"$avg":"$price"}}}

#Crear la tuberia, de acuerdo a la cantidad de etapas
tuberia = [match,grupo]

#lanzar el aggregate
resultados = propiedades.aggregate(tuberia)

#Visualizar el resultados
for resultado in resultados:
    pprint.pprint(resultado)
