import pymongo
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

osobyTemp = []

for osoba in mydb.osoby.find({'nazwisko':"Nowak"}):
    hobby = []
    if('zainteresowania' in osoba):
        for hob in osoba['zainteresowania']:
            typ = []
            hobby.append({'hobby':hob,'typ':[x['miejsce'] for x in mydb.sport.find({'nazwa':hob})][0]})
        osobyTemp.append({'imie':osoba['imie'],'nazwisko':osoba['nazwisko'],'narodowść':osoba['narodowość'],'hobbies':hobby})

for x in osobyTemp:
    pprint.pprint(x)
    