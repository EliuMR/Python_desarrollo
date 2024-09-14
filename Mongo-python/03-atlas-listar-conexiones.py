
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://eliumoreno:morenoramirez@cluster0.zqmna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#uri = "mongodb+srv://eliumoreno:<db_password>@cluster0.zqmna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

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
