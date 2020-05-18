import random
import math
import os
import sys

def is_prime(n):
    d = n-1
    s = 0
    while d % 2 == 0:
        d>>=1
        s += 1

    for _ in range(8):
        a = random.randint(2, n-2)
        x = pow(a,d,n)
        if (x == 1 or x == n-1):
            continue
        j = 1
        while j < s and x != n-1:
            x = (x*x) % n
            if x == 1:
                return False
            j += 1
        if x != n-1:
            return False
        
    return True


def inverse_mod(a,m):
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 

def encode(a,d,n):
    return pow(a,d,n)

def decode(b,d,n):
    return pow(b,d,n)


def generate_keys(bits_num):

    # choose p and q as big prime numbers
    while True:
        p = random.getrandbits(bits_num)
        if is_prime(p):
            break
    while True:
        q = random.getrandbits(bits_num)
        if is_prime(q):
            break

    n=p*q

    euler = (p-1)*(q-1)

    # choose e which is odd and not a factor of n
    while True:
        e = random.randint(2,euler-1)
        if(math.gcd(e, euler) == 1) and e&1:
            break

    # choose d as a moudlo invertion to e
    d = inverse_mod(e, euler)

    with open('key.prv','w') as file:
        file.write(str(n)+'\n'+str(d))

    with open('key.pub','w') as file:
        file.write(str(n)+'\n'+str(e))

def encrypt(mess_to_enc):

    # check whether public key exists
    assert(os.path.isfile('key.pub')),(
        "Public key does not exist!\nGenerate it and try again!\n")
        
    with open('key.pub','r') as file:
            lines  = file.readlines()
            n = lines[0]
            e = lines[1]

    encrypted_text = ''

    for char in mess_to_enc:
        encrypted_text += str(encode(ord(char),int(e),int(n)))+'.'

    print(encrypted_text)

def decrypt(mess_to_dec):

    # check whether private key exists
    assert(os.path.isfile('key.prv')),(
        "Private key does not exist!\nGenerate it and try again!\n")

    with open('key.prv','r') as file:
            lines  = file.readlines()
            n = lines[0]
            d = lines[1]

    decrypted_text = ''

    numbers = mess_to_dec.split(".")
    for number in numbers[:len(numbers)-1]:
        decrypted_text += chr(decode(int(number),int(d),int(n)))

    print(decrypted_text)

if __name__=='__main__':
    
    arguments = sys.argv

    if arguments[1]=='--gen-keys':
        generate_keys(int(arguments[2]))
    elif arguments[1] == '--encrypt':
        encrypt(arguments[2])
    elif arguments[1] == '--decrypt':
        decrypt(arguments[2])
    else:
        print("""Provide correct arguments:
        1. To generate keys type: rsa.py --gen-keys 'keys bytes number'
        2. To encrypt message: rsa.py --encrypt 'message to encrypt'
        3. To decrypt message: rsa.py --decrypt 'message to decrypt'""")