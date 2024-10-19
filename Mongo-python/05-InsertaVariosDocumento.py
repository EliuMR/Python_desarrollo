from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://<usuario>:<contraseña>@<cluster-url>/<nombre_base_datos>?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! \n")
except Exception as e:
    print(e)

"""dbname=client["db1"]
colecciones=dbname.list_collection_names()
print("las colecciones: \n")
for col in colecciones:
    print(col)"""

#Base de datos
dbname=client["db1"]
print("La base de datos es: ",str(dbname),"\n")

#Colección a usar o crear
facturas= dbname["facturas"]

print("Las colección es: ",str(facturas),"\n")
#Documento a insertar
factura1={
        "cod_factura":1,
        "descripción": "Un ejemplo de factura",
        "total": 100,
        "productos": ["tomate","pera","limones"]
        }

factura2={
        "cod_factura":2,
        "descripción": "Un ejemplo de factura 2",
        "total": 10,
        "productos": ["naranjas","papas"]
        }
factura3={
        "cod_factura":3,
        "descripción": "Un ejemplo de factura3",
        "total": 201,
        "productos": ["cebollas","jitomate","cilantro"]
        }

#Insertar documento
resultado = facturas.insert_many([factura1,factura2,factura3])

print("El documento insertado es: \n",resultado,"\n")
colecciones = dbname.list_collection_names()

print("Las colecciones")
for coleccion in colecciones:
    print(coleccion)
