import pymongo
import random
import pprint

myClient = pymongo.MongoClient(port=27017)

mydb = myClient.MDBHobby

mydb.osoby.drop()

imiona = "Jan, Ada, Adela, Adelajda, Adrianna, Agata, Agnieszka, Aldona, Aleksandra, Alicja, Alina, Amanda, Amelia, Anastazja, Andżelika, Aneta, Anita, Anna, Antonina, Adam, Adolf, Adrian, Albert, Aleksander, Aleksy, Alfred, Amadeusz, Andrzej, Antoni, Arkadiusz, Arnold, Artur".split(", ")
##imiona = ["Jan"]
nazwiska = ['Nowak','Kowalski','Wiśniewski','Wójcik','Kowalczyk','Kamiński']
zainteresowania = [x['nazwa'] for x in mydb.sport.find()]
narodowości = ['Polska','Niemcy','Rosja','USA','Szwajcaria','Egipt','Korea Północna']
podziałRosji = ['Republika Jakucji','Republika Komi']
podziałNiemiec = ['Bawaria','Saksonia']
podziałUSA = ['California','Colorado','Floryda']
zwierzęta = []

for zwierzę in mydb.zwierzęta.find():
    if('rasy' in zwierzę):
        for rasa in zwierzę['rasy']:
            zwierzęta.append(rasa['nazwa'])
    else:
        zwierzęta.append(zwierzę['nazwa'])

listaOsób = []

for i in range(1,51):
    pupile = []
    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    liczbaPupili = random.randint(0, len(zwierzęta))
    zwierzętaTemp = random.sample(zwierzęta,liczbaPupili)
    for i in range (0,liczbaPupili):
        pupile.append({'gatunek':zwierzętaTemp[i], 'imię':random.choice(imiona)})

    if(random.uniform(0.0,1.0) > 0.20):
        wiek = random.randint(5, 55)
        wzrost = random.randint(150, 195)
        ilośćZainteresowań = random.randint(1, len(zainteresowania))
        ilośćNarodowości = random.randint(1, len(narodowości))
        zainteresowanie = random.sample(zainteresowania, ilośćZainteresowań)
        narodowość = random.sample(narodowości,ilośćNarodowości)

        listaNarodowości = []
        for naro in narodowość:
            if(naro == "USA"):
                listaNarodowości.append({'nazwa':'USA',
                'stan':random.choice(podziałUSA)})
            elif(naro == 'Rosja'):
                listaNarodowości.append({'nazwa':'Rosja',
                'republika':random.choice(podziałRosji)})
            elif(naro == 'Niemcy'):
                listaNarodowości.append({'nazwa':'Niemcy',
                'land':random.choice(podziałNiemiec)})
            else:
                listaNarodowości.append({'nazwa':naro})

        listaOsób.append({'imie':imie,'nazwisko':nazwisko, 'wiek':wiek, 'wzrost':wzrost, 'zainteresowania':zainteresowanie, 'narodowość':listaNarodowości, 'pupile':pupile})
    
    else:
        listaOsób.append({'imie':imie,'nazwisko':nazwisko, 'pupile':pupile})

mydb.osoby.insert_many(listaOsób)

for x in mydb.osoby.find():
    pprint.pprint(x)
        




