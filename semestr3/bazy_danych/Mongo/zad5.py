import pymongo
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

for x in mydb.list_collection_names():
    pprint.pprint(x)

for x in mydb.list_collection_names():
    if(mydb[x].count_documents({}) != 0):
        pprint.pprint(x)