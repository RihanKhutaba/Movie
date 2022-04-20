from pymongo import MongoClient
import gridfs

connection = MongoClient("localhost", 27017)

database = connection['DB_NAME']

fs = gridfs.GridFS(database)

file = "poster_1.jpeg"

with open(file, 'rb') as f:
    contents = f.read()

fs.put(contents, filename="file")
