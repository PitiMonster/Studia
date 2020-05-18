import pymongo
import random
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

mydb.zwierzęta.drop()

nazwy = ['kot','koń','lew','małpa','hipopotam','zebra','koza','krowa','słoń']
ubarwienia = ['biały','szary','czarny','brązowy','niebieski','zielony']
listaZwierzat = []

for nazwa in nazwy:
    wagaMinimalna = random.uniform(0.5, 60.0)
    wagaMaksymalna = wagaMinimalna + random.uniform(1.0, 30.0)
    ilośćUbarwień = random.randint(1, len(ubarwienia))
    ubarwienie = random.sample(ubarwienia, ilośćUbarwień)
    długośćŻycia = random.randint(1, 12*36)
    listaZwierzat.append({'nazwa':nazwa,'wagaMin':wagaMinimalna, 'wagaMax': wagaMaksymalna, 'ubarwienie': ubarwienie, 'długość życia':długośćŻycia})

#przykład zwierzęcia z rasami
nazwyRas = ['pudel','maltańczyk','jork','shih tzu','pegaz']
rasy = []

for rasa in nazwyRas:
    wagaMinimalna = random.uniform(0.5, 60.0)
    wagaMaksymalna = wagaMinimalna + random.uniform(1.0, 30.0)
    ilośćUbarwień = random.randint(1, len(ubarwienia))
    ubarwienie = random.sample(ubarwienia, ilośćUbarwień)
    długośćŻycia = random.randint(1, 12*36)
    rasy.append({'nazwa': rasa,'wagaMin':wagaMinimalna, 'wagaMax': wagaMaksymalna, 'ubarwienie': ubarwienie, 'długość życia':długośćŻycia})

listaZwierzat.append({'nazwa':'pies','rasy':rasy})

mydb.zwierzęta.insert_many(listaZwierzat)

for x in mydb.zwierzęta.find():
    pprint.pprint(x)