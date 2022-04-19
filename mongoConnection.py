import pymongo
import gridfs
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
database = connection['DB_NAME']
""" database = client['db']
my_collection = database['movies']
"""
a = my_collection.find()
print(a)
for i in a:
    print(i)
"""
#my_collection.insert_one({'name': 'avengers'})


#Create an object of GridFs for the above database.
fs = gridfs.GridFS(database)

#define an image object with the location.
file = "poster_1.jpeg"

#Open the image in read-only format.
with open(file, 'rb') as f:
    contents = f.read()

#Now store/put the image via GridFs object.
fs.put(contents, filename="file")
client.close()