from pymongo import MongoClient


client = MongoClient(port=27017)

client.drop_database('MDBHobby')
db = client.MDBHobby
db.create_collection('zwierzęta')
db.create_collection('sport')
db.create_collection('osoby')

print(client.list_database_names())
print(db.list_collection_names())