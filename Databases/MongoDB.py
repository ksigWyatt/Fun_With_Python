# importing MongoDB's library for Python -- PyMongo
# We don't really need this line but It's helpful to have to think about where the information is coming from
#import pymongo

#from pymongo directory import MongoClient so we can connect to a client port
from pymongo import MongoClient
#create a new MongoClient Object
client = MongoClient()

#here is where the port and server for mongoDB is running on your machine is located
client = MongoClient('localhost', 27017)

# assign to the database the name of pymongo_test
# running show dbs in the mongo.exe shell will display this name after running the code while the DB is open
# this will become the name of the database
db = client.pymongo_test

#create a new post -- post is another name for a "document" in MongoDB
posts = db.posts

# assign the data to the Document after it has been created ... you'll notice that this looks exactly like JSON format
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys!',
    'author': 'Wyatt'
}

# insert the document into the database
result = posts.insert_one(post_data)

# printing the ID of the document in the database once it has been added
print('One post: {0}'.format(result.inserted_id))