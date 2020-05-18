import numpy as np
from bitarray import bitarray
import filecmp
import os
import entropy


""" return float value of binary number """
def bin_to_float(bin_code):
    multiplier = 0.5
    result = 0
    for i, b in enumerate(bin_code):
        result += int(b)*multiplier
        multiplier /= 2
        if i == 60:
            break
    
    return result

""" return letter and start, end of search interval """
def find_interval(chars_amount_list, chars_amount, value, start, end):
    length = end - start
    for i in range(chars_amount):
        # check which interval cointains search value 
        if (value >= start + length*sum(chars_amount_list[:i])/chars_amount and value < start + length*sum(chars_amount_list[:i+1])/chars_amount):
            return i, start + length*sum(chars_amount_list[:i])/chars_amount, start + length*sum(chars_amount_list[:i+1])/chars_amount

""" return start, end, counter, bin_code after scaling """
def encode_scaling(start, end, counter, bin_code):

    while True:
        if (end < 0.5 and start >= 0):
            bin_code += '0'
            while counter:
                bin_code += '1'
                counter -= 1
        elif (start >= 0.5 and end < 1):
            bin_code += '1'
            while counter:
                bin_code += '0'
                counter -= 1
            start -= 0.5
            end -= 0.5
        elif (start >= 0.25 and end < 0.75):
            counter += 1
            start -= 0.25
            end -= 0.25
        else:
            return start, end, counter, bin_code

        start *= 2
        end *= 2

""" 
encoding message from filename
and write it to 'encoded_text.txt' file
"""
def encode(filename):

    chars_amount_list = [1 for _ in range(257)]
    chars_amount = 257

    start = 0
    end = 1
    counter = 0
    bin_code = ''
    outfile = open('encoded_text.txt', 'wb')
    with open(filename, 'rb') as file:
        content = list(file.read()) + [256] # 256 jako EOF
        for c in content:
            length = end - start
            # compute new start and new end of interval
            start, end =  start + length*sum(chars_amount_list[:c])/chars_amount, start + length*sum(chars_amount_list[:c+1])/chars_amount
            start, end, counter, bin_code = encode_scaling(start, end, counter, bin_code)
            # increment occurence of that letter
            chars_amount_list[c] += 1
            chars_amount += 1

    # finish encoding
    counter += 1
    if start < 0.25:
        bin_code += '0'
        while counter:
            bin_code += '1'
            counter -= 1
    else:
        bin_code += '1'
        while counter:
            bin_code += '0'
            counter -= 1

    # outfile.write(bin_code)
    b = bitarray(bin_code)
    b.tofile(outfile)
    outfile.close()

""" return start, end, bin_code after scaling """
def decode_scaling(start, end, bin_code):

    while True:
        if end < 0.5:
            pass
        elif start >= 0.5:
            bin_code[0] = '0' # substract 0.5 from bin_code
            start -= 0.5
            end -= 0.5
        elif (start >= 0.25 and end < 0.75):
            start -= 0.25
            end -= 0.25
            # substract 0.25 from bin_code
            if (bin_code[0] == '1' and bin_code[1] == '1'):
                bin_code[1] = '0'
            elif bin_code[0] == '1':
                bin_code[0] = '0'
                bin_code[1] = '1'
            else:
                bin_code[1] = '0'
        else:
            return start, end, bin_code
        
        bin_code = bin_code[1:] # multiply bin_code by 2
        start *= 2
        end *= 2

""" 
decode message from filename file
and write it to 'decoded_text.txt' file
"""
def decode(filename, outfilename):
    infile = open(filename, 'rb')
    b = list(infile.read())
    bin_code = []
    for bit in b:
        temp = format(bit,'08b')
        for c in temp:
            bin_code.append(c)  
    infile.close()

    start = 0
    end = 1
    letter = 0
    message = ''

    chars_amount_list = [1 for _ in range(257)]
    chars_amount = 257

    while True:
        
        bin_code_value = bin_to_float(bin_code)

        # find next interval giving next letter, new start and new end
        letter, letter_start, letter_end = find_interval(chars_amount_list, chars_amount, bin_code_value, start, end)
        if letter == 256: # EOF = 256
            break
        # add to message eight bits equivalent to encoded letter
        message += format(letter, '08b')
    
        start, end, bin_code = decode_scaling(letter_start, letter_end, bin_code)
        # increment occurence of encoded letter
        chars_amount_list[letter] += 1
        chars_amount += 1

    outfile = open(outfilename, 'wb')
    b = bitarray(message)
    b.tofile(outfile)
    outfile.close()


def main():

    infilename = 'test.txt'
    outfilename = 'decoded_text.txt'

    encode(infilename)
    decode('encoded_text.txt', outfilename)

    if filecmp.cmp(infilename, outfilename):
        print("Good job! Go have a rest.")
    else:
        print("Go work!")
        return
    
    x = open('encoded_text.txt','rb')
    encoded_file_length = len(list(x.read()))
    x.close()

    x = open(infilename,'rb')
    file_length = len(list(x.read()))
    x.close()

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

        