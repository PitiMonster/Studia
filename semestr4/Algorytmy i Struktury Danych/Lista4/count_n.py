import time 
import hmap
import random
import string
import sys

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generuj_plik():
    print("1000000")
    for _ in range(100000): 
        print("insert " + randomString(5))
    for _ in range(100000):
        print("delete " +randomString(5))
        



# generuj_plik()
MIN_T = (10000,0)
for i in range(1,1000):
    print(i, file=sys.stderr)
    t0 = time.time()
    hashmap = hmap.HashMap(1000000,i)
    with open("test_n.txt","r") as f: 
        content = f.readlines()
    n = int(content[0])
    for c in content[1:]:
        message = c.split(" ")
        if message[0] == "insert":
            hashmap.insert(message[1])
        elif message[0] == "delete":
            hashmap.delete(message[1])

    t1 = time.time()
    if t1 - t0 < MIN_T[0]:
        MIN_T = (t1-t0, i) 
    print(MIN_T)







