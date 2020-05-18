import pymongo
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

for osoba in mydb.osoby.find({'pupile.gatunek':"kot"}):
    for pupil in osoba['pupile']:
        if (pupil['gatunek'] == "kot"):
            print("właściciel:"+osoba['imie']+", kotek:"+pupil['imię'])
        