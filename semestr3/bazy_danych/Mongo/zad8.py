import pymongo
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

mySports = []

for sport in mydb.sport.find():
    tempOsoby = []
   ## tempOsoby = [x for x in mydb.osoby.find({sport['nazwa'] in x['zainteresowania']})]
    for osoba in mydb.osoby.find():
        if('zainteresowania' in osoba):
            if(sport['nazwa'] in osoba['zainteresowania']):
                tempOsoby.append(osoba)
    if(len(tempOsoby) >= 5):
        print(sport['nazwa'])
    