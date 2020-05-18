import pymongo
import random
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

mydb.sport.drop()

nazwySportów = ['koszykówka', 'hokej','narciarstwo','strzelectwo','siatkówka','piłka nożna','kolarstwo','wspinaczka','pływanie','wiślarstwo']
miejsceSportu = ['hala','na zewnątrz']
rodzajSportu = ['indywidualny','zespołowy']
listaSportów = []

for nazwaSportu in nazwySportów :
    ilośćMiejsc = random.randint(1,2)
    liczbaRodzajów = random.randint(1,2)
    listaSportów.append({"nazwa":nazwaSportu, "miejsce":random.sample(miejsceSportu, ilośćMiejsc), "rodzaj":random.sample(rodzajSportu,liczbaRodzajów)})

mydb.sport.insert_many(listaSportów)

for element in mydb.sport.find():
    pprint.pprint(element)
