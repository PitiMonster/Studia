import pymongo
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

for osoba in mydb.osoby.find({'imie':'Jan'},{'_id':False}):
    if('narodowość' in osoba):
        if('Polska' in osoba['narodowość'] or len(osoba['narodowość']) > 1):
            pprint.pprint(osoba)

