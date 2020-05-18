import random

from framing import encode_frame_data

"""
creating 1000 binary strings of length = 32
and write them to filename file
"""
def create_32_bits_data(filename):
    result = ''
    for _ in range(1000):
        result += format(random.randint(2**31,2**32), '032b')
    
    file = open(filename, 'w')
    file.write(result)
    file.close()

def encode_file(infilename, outfilename):
    file = open(infilename, 'r')
    outfile = open(outfilename, 'w')
    outfile.write(encode_frame_data(file.read()))

    file.close()
    outfile.close()