from pymongo import MongoClient
import gridfs

# Connect to the server with the hostName and portNumber.
connection = MongoClient("localhost", 27017)

# Connect to the Database where the images will be stored.
database = connection['DB_NAME']

#Create an object of GridFs for the above database.
fs = gridfs.GridFS(database)

#define an image object with the location.
file = "poster_1.jpeg"

#Open the image in read-only format.
with open(file, 'rb') as f:
    contents = f.read()

#Now store/put the image via GridFs object.
fs.put(contents, filename="file")

# read files:
db = MongoClient().mygrid
fs = GridFS(db)
ob = fs.put("hello world")
fs.get(ob).read()
'hello world'

"""
#delete files:
db = MongoClient().mygrid
fs = GridFS(db)
fileid = fs.put("This is the content of the file.", filename="newfile.txt")
fs.get(fileid).read()
'This is the content of the file.'
fs.delete(fileid)
"""