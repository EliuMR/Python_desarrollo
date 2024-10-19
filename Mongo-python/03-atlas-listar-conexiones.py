
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

dbname=client["db1"]
colecciones=dbname.list_collection_names()
print("las colecciones: \n")
for col in colecciones:
    print(col)
