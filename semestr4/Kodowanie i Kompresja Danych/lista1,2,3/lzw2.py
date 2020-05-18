import codecs
import numpy
import sys
import os
from bitarray import bitarray
import filecmp
import collections
import entropy

# global list with fibonacci value
fib = [1,2]

""" 
return index of fibonacci number <= x
where next fib number > x
"""
def find_leq_x(x):
    for i in range(len(fib)):
        if fib[i] > x:
            return i-1

""" return encoded number with fibonacci coding """
def fibonacci_coding(x):

    if x == 0:
        return '11'

    while fib[-1] <= x:
        fib.append(fib[-1]+fib[-2])

    index = find_leq_x(x)
    bits_amount = index + 1
    code = ''
    while x > 0:
        if x >= fib[index]:
            x -= fib[index]
            code = '1' + code
        else:
            code = '0' + code
        index -= 1

    while len(code) < bits_amount:
        code = '0' + code
    return code+'1'

def fibonacci_decoding(x):
    result = 0
    while len(x)-1 > len(fib):
        fib.append(fib[-1]+fib[-2])

    for i, c in enumerate(x[:-1]):
        result += fib[i] * int(c)

    return result

""" return list of numbers from 'bits' string """
def fibonacci_dividing(bits):
    numbers = []
    i = 0
    while bits:
        if (bits[i] == '1' and bits[i+1] == '1'):
            numbers.append(fibonacci_decoding(bits[:i+2]))
            bits = bits[i+2:]
            i = 0
        else:
            i+=1
        
            
    return numbers

def elias_gamma_coding(x):
    if x == '0':
        return '0'
    
    bits_amount = int(numpy.log2(x))
    rest_value = x - 2**(bits_amount)

    result = (bits_amount) * '0'+'1'
    rest_value_bits = format(rest_value, '0%db' % bits_amount)

    return result + rest_value_bits

def elias_gamma_decoding(x):

    n = 0
    while x[n] != '1':
        n+=1
    
    rest = int(x[n+1:],base=2)

    return 2**n + rest

def elias_gamma_dividing(bits):
    numbers = []
    n = 0
    while bits:
        if bits[0] == '1':
            numbers.append(1)
            bits = bits[2:]
        else:
            while bits[n] == '0':
                n+=1

            rest = int(bits[n+1:2*n+1], base=2)
            numbers.append(2**n + rest)
            bits = bits[2*n+1:]
            n= 0

    return numbers
    
def elias_delta_coding(x):

    n = int(numpy.log2(x))
    l = int(numpy.log2(n+1))

    return l*'0' + format(n+1, 'b') + format(x, '0%db' % n)[1:]

def elias_delta_decoding(x):
    if x == '1':
        return 1
    
    l = 0
    while x[l] == '0':
        l+=1
    num = int(x[:2*l+1],base=2)
    rest = int(x[2*l+1:], base=2)

    return 2**(num-1) + rest

def elias_delta_dividing(bits):
    numbers = []
    n = 0
    while bits:
        while bits[n] == '0':
            n += 1
        num = int(bits[:2*n+1],base=2)
        numbers.append(elias_delta_decoding(bits[:2*n+num]))
        bits = bits[2*n+num:]
        n = 0
    
    return numbers

def elias_omega_coding(x, code=''):

    if x == 1:
        code += '0'
        return code

    x_bin = format(x, 'b')
    code = x_bin + code

    code = elias_omega_coding(len(x_bin)-1, code)

    return code

def elias_omega_decoding(bits):
    numbers = []
    n = 1

    while bits:
           
        while bits[0] != '0':
            temp = int(bits[:n+1], base=2)
            bits =  bits[n+1:]
            n = temp
        bits = bits[1:]
        numbers.append(n)
        n = 1
    
    return numbers

"""find key of value in given dictionary"""
def find_key(dictio, value):
    for key, v in dictio.items():
        if v == value:
            return key

""" return encoded filename content by lzw algrithm"""
def encode(filename):
    infile = open(filename,'rb')
    message = list(infile.read())
    chars_dict = {}
    next_index = 1
    code = []
    for c in message:
        if not [str(c)] in chars_dict.values():
            chars_dict[next_index] = [str(c)]
            next_index += 1

    c = [str(message[0])]
    k = 1
    while k < len(message):
        s = [str(message[k])]
        temp = c+s
        if temp in chars_dict.values():
            c = temp
        else:
            code.append(find_key(chars_dict, c))
            chars_dict[next_index] = temp
            next_index += 1
            c = s
        k += 1
    code.append(find_key(chars_dict, c))

    infile.close()
    return code


def decode(message, slownik, outfilename):
    with open(outfilename,'wb') as file:
        result = ''
        prev_code_char = message[0]
        for i in slownik[prev_code_char]:
            result += format(int(i), '08b')
        next_index = len(slownik)+1

        for c in message[1:]:
            prev_string = slownik[prev_code_char]
            if c in slownik.keys():
                temp = prev_string + [slownik[c][0]]
                slownik[next_index] = temp
                next_index += 1
                for i in slownik[c]:
                    result += format(int(i), '08b')
            else:
                temp = prev_string+[prev_string[0]]
                slownik[next_index] = temp
                next_index += 1
                for i in temp:
                    result += format(int(i), '08b')
            prev_code_char = c

        b = bitarray(result)
        b.tofile(file)

    return


def choose_encoding(code_type, code):
    bits = ''

    if code_type == 'omega':
        for c in code:
            bits += elias_omega_coding(c)
    elif code_type == 'delta':
        for c in code:
            bits += elias_delta_coding(c)
    elif code_type == 'gamma':
        for c in code:
            bits += elias_gamma_coding(c)
    elif code_type == 'fibo':
        for c in code:
            bits += fibonacci_coding(c)
    else:
        print('Wrong encoding type!')
        return 1
    
    # bitarray add some zeros numbers if len(bits) % 8 != 0
    # so count them and add this number to the end of encoded string
    redundant_zeros_num = 8 - len(bits) % 8
    if redundant_zeros_num == 8:
        redundant_zeros_num = 0
    b = bitarray(bits)
    outfile = open('encoded_text.txt','wb')
    b.tofile(outfile)
    b = bitarray(format(redundant_zeros_num, '08b'))

    b.tofile(outfile)
    outfile.close()
    return 0

def choose_decoding(code_type, code, dictio, outfilename):

    if code_type == 'omega':
        numbers = elias_omega_decoding(code)
        decode(numbers, dictio, outfilename)
    elif code_type == 'delta':
        numbers = elias_delta_dividing(code)
        decode(numbers, dictio, outfilename)
    elif code_type == 'gamma':
        numbers = elias_gamma_dividing(code)
        decode(numbers, dictio, outfilename)
    elif code_type == 'fibo':
        numbers = fibonacci_dividing(code)
        decode(numbers, dictio, outfilename)
    else:
        print('Wrong encoding type!')
        return 1
    
    return 0

def main():
    args = list(sys.argv)
    if len(args) == 1:
        args.append('omega')

    infilename = 'test.txt'
    outfilename = 'decoded_text.txt'
    code = encode(infilename)
    encoding_error = choose_encoding(args[1], code)
    if encoding_error:
        return

    # create dictionary for decode function
    message_file = open(infilename,'rb')
    message = list(message_file.read())
    file_length = len(message)
    message_file.close()

    dictio = {}
    next_index = 1
    for c in message:
        if not [str(c)] in dictio.values():
            dictio[next_index] = [str(c)]
            next_index += 1


    # read encoded text and parse it to 0-1 values
    encoding_file = open('encoded_text.txt','rb')
    content = list(encoding_file.read())
    encoded_file_length = len(content)
    bits = ''
 
    for byte in content[:-1]:
        bits += format(byte,'08b')

    # delete redundant zeros from the end of encoded 0-1 string    
    redundant_zeros_num = content[-1]
    if redundant_zeros_num > 0:
        bits = bits[:-content[-1]]

    # decode message
    choose_decoding(args[1],bits,dictio, outfilename)


    if filecmp.cmp(infilename, outfilename):
        print("Good job! Go have a rest.")
    else:
        print("Go work!")
        return

    print("Dlugosc kodowanego pliku: ", file_length)
    print("Dlugosc uzyskanego kodu: ", encoded_file_length)
    compression_deg = os.stat(infilename).st_size/os.stat('encoded_text.txt').st_size
    print("Stopien kompresji: ", compression_deg)
    print("\nEntropia pliku kodowanego:")
    entropy.entropy(infilename)
    print("\nEntropia uzyskanego kodu:")
    entropy.entropy('encoded_text.txt')


if __name__ == "__main__":
    main()
