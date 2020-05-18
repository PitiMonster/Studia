import numpy
from arytmetyczne import encode, decode
import time
import filecmp
from bitarray import bitarray
from entropy import entropy
import sys


def original_file(infilename, outfilename, file_R, file_G, file_B):
    with open(infilename, 'rb') as file:
        content = file.read()

    bit_map = content[18:-26]

    r_file = open(file_R, 'wb')
    g_file = open(file_G, 'wb')
    b_file = open(file_B, 'wb')

    with open(outfilename,'wb') as file:
        for i, b in enumerate(bit_map):
            b = b.to_bytes(1, 'big')
            file.write(b)

            # decide whether b is component of R, G or B
            if i % 3 == 0:
                r_file.write(b)
            elif i % 3 == 1:
                g_file.write(b)
            else:
                b_file.write(b)

    r_file.close()
    g_file.close()
    b_file.close()

def pred0(value):
    return value

def pred1(i, j, predictors, value):
    # i - height, j - width
    return (value - predictors[i][j-3]) % 256

def pred2(i, j, predictors, value):
    # i - height, j - width
    return (value - predictors[i-1][j]) % 256

def pred3(i, j, predictors, value):
    # i - height, j - width
    return (value - predictors[i-1][j-3]) % 256

def pred4(i, j, predictors, value):
    # i - height, j - width
    return (value - (predictors[i][j-3] + predictors[i-1][j] - predictors[i-1][j-3])) % 256

def pred5(i, j, predictors, value):
    # i - height, j - width
    return (value - (predictors[i][j-3]
            + (predictors[i-1][j]
            - predictors[i-1][j-3]) / 2
            )) % 256

def pred6(i, j, predictors, value):
    # i - height, j - width
    return (value - (predictors[i-1][j]
            + (predictors[i][j-3]
            - predictors[i-1][j-3]) / 2
            )) % 256

def pred7(i, j, predictors, value):
    # i - height, j - width
    return (value - ((predictors[i][j-3]
            + predictors[i-1][j]) / 2
            )) % 256

def pred8(i, j, predictors, value):
    a = predictors[i][j-3]
    b = predictors[i-1][j]
    c = predictors[i-1][j-3]
    if c >= max(a,b):
        return (value - max(a,b)) % 256
    elif c <= min(a,b):
        return (value - min(a,b)) % 256
    else:
        return (value - (a + b - c)) % 256

def read_filename(infilename, outfilename, pred_num, file_R, file_G, file_B):
    with open(infilename, 'rb') as file:
        content = file.read()

    header = content[:18]
    footer = content[-26:]
    bit_map = content[18:-26]

    two_dimensional_pred = "pred"+str(pred_num)
    height = (header[14] + header[15]*256) # get height from specified place in header
    width = (header[12] + header[13]*256) * 3   # get width from specified place in header and multiply it by 3 because of rgb value for each one
    encoded_bit_map = numpy.zeros((height,width))
    curr_width = 0 
    curr_height = 0

    r_file = open(file_R, 'wb')
    g_file = open(file_G, 'wb')
    b_file = open(file_B, 'wb')

    with open(outfilename,'wb') as file:
        for b in bit_map:

            if curr_width == width:
                curr_width = 0
                curr_height += 1

            # first piksel of photo
            if curr_height == 0 and curr_width < 3:
                res = pred0(b)
            # first row of piksels
            elif curr_height == 0 and curr_width >= 3:
                res = pred1(curr_height, curr_width, encoded_bit_map, b)
            # first column of piksels
            elif curr_height > 0 and curr_width < 3:
                res = pred2(curr_height, curr_width, encoded_bit_map, b)
            # middle piksels
            else:
                res = globals()[two_dimensional_pred](curr_height, curr_width, encoded_bit_map, b)
                res = (numpy.ceil(res)) % 256
            
            encoded_bit_map[curr_height][curr_width] = res
 
            res = int(res).to_bytes(1, 'big')
            file.write(res)

            # decide whether b is component of R, G or B
            if curr_width % 3 == 0:
                r_file.write(res)
            elif curr_width % 3 == 1:
                g_file.write(res)
            else:
                b_file.write(res)

            curr_width += 1

    r_file.close()
    g_file.close()
    b_file.close()

    return header, footer

def decode_pred0(value):
    return value

def decode_pred1(i, j, predictors, x):
    return (x + predictors[i][j-3]) % 256

def decode_pred2(i, j, predictors, x):
    return (x + predictors[i-1][j]) % 256

def decode_pred3(i, j, predictors, x):
    return (x + predictors[i-1][j-3]) % 256

def decode_pred4(i, j, predictors, value):
    # i - height, j - width
    return (value + (predictors[i][j-3] + predictors[i-1][j] - predictors[i-1][j-3])) % 256

def decode_pred5(i, j, predictors, value):
    # i - height, j - width
    return (value + (predictors[i][j-3]
            + (predictors[i-1][j]
            - predictors[i-1][j-3]) / 2
            )) % 256

def decode_pred6(i, j, predictors, value):
    # i - height, j - width
    return (value + (predictors[i-1][j]
            + (predictors[i][j-3]
            - predictors[i-1][j-3]) / 2
            )) % 256

def decode_pred7(i, j, predictors, value):
    # i - height, j - width
    return (value + ((predictors[i][j-3]
            + predictors[i-1][j]) / 2
            )) % 256

def decode_pred8(i, j, predictors, value):
    a = predictors[i][j-3]
    b = predictors[i-1][j]
    c = predictors[i-1][j-3]
    if c >= max(a,b):
        return (value + max(a,b)) % 256
    elif c <= min(a,b):
        return (value + min(a,b)) % 256
    else:
        return (value + (a + b - c)) % 256

def result_file(infilename, header, footer, outfilename, pred_num):

    filename = 'encoded_bit_map.bin'
    # decode(infilename, filename)

    with open(filename, 'rb' ) as file:
        content = list(file.read())
    
    two_dimensional_pred = "decode_pred" + str(pred_num)
    height = (header[14] + header[15]*256)
    width = (header[12] + header[13]*256) * 3
    temp = numpy.zeros(())
    curr_width = 0
    curr_height = 0
    decoded_bit_map = []
    temp = numpy.zeros((height, width))
    k = 0
    # create two dimensional list of predicators
    for i in range(height):
        for j in range(width):
            temp[i][j] = float(content[k])
            k += 1

    for c in content:
            c = float(c)
            if curr_width == width:
                curr_width = 0
                curr_height += 1

            if not curr_height and curr_width < 3:
                res = decode_pred0(c)
            elif not curr_height and curr_width >= 3:
                res = decode_pred1(curr_height, curr_width, temp, c)
            elif curr_height and curr_width < 3:
                res = decode_pred2(curr_height, curr_width, temp, c)
            else:
                res = globals()[two_dimensional_pred](curr_height, curr_width, temp, c)
                res = numpy.floor(res)
            
            
            decoded_bit_map.append(int(res))
            curr_width += 1

    header = list(header)
    footer = list(footer)
    header.extend(decoded_bit_map)
    header.extend(footer)
    content = ''

    for h in header:
        content += format(h, '08b')
    x = bitarray(content)
    temp_file = open(outfilename, 'wb')
    x.tofile(temp_file)
    temp_file.close()

def main():

    filename = list(sys.argv)[1]

    best_r_entropy = ('', 8)
    best_g_entropy = ('', 8)
    best_b_entropy = ('', 8)
    best_file_entropy = ('', 8)

    file_R = 'r_values.bin'
    file_G = 'g_values.bin'
    file_B = 'b_values.bin'
    outfilename = "encoded_bit_map.bin"
    encoded_aryt_file = 'encoded_file.bin'

    # entropy for original file
    original_file(filename, outfilename, file_R, file_G, file_B)

    # encode(file_R, encoded_aryt_file) # arithmetic encoding
    # entrop = entropy(encoded_aryt_file) # entropy computing
    entrop = entropy(file_R)

    print("Original file R component entropy: %f" % entrop)

    # encode(file_G, encoded_aryt_file)
    # entrop = entropy(encoded_aryt_file)
    entrop = entropy(file_G)
        
    print("Original file G component entropy: %f" % entrop)

    # encode(file_B, encoded_aryt_file)
    # entrop = entropy(encoded_aryt_file)
    entrop = entropy(file_B)

    print("Original file B component entropy: %f" % entrop)


    # encode(outfilename, encoded_aryt_file)
    # entrop = entropy(encoded_aryt_file)
    entrop = entropy(outfilename)

    print("Original file entropy: %f" % entrop)

    for pred_num in range(1,9):
        
        header, footer = read_filename(filename, outfilename, pred_num, file_R, file_G, file_B)
        result_file('encoded_text.txt', header, footer, 'result.tga', pred_num)

        if filecmp.cmp(filename, 'result.tga'):
            print("YEAAA!")
        else:
            print("BUUUU!")

        # entropy counting
        # encode(file_R, encoded_aryt_file) # arithmetic encoding
        # entrop = entropy(encoded_aryt_file) # entropy computing
        entrop = entropy(file_R) # entropy just for predicate encoding
        if entrop < best_r_entropy[1]:
            best_r_entropy = ("standard " + str(pred_num), entrop)

        
        # encode(file_G, encoded_aryt_file)
        # entrop = entropy(encoded_aryt_file)
        entrop = entropy(file_G)
        if entrop < best_g_entropy[1]:
            best_g_entropy = ("standard " + str(pred_num), entrop)


        # encode(file_B, encoded_aryt_file)
        # entrop = entropy(encoded_aryt_file)
        entrop = entropy(file_B)
        if entrop < best_b_entropy[1]:
            best_b_entropy = ("standard " + str(pred_num), entrop)


        # encode(outfilename, encoded_aryt_file)
        # entrop = entropy(encoded_aryt_file)
        entrop = entropy(outfilename)
        if entrop < best_file_entropy[1]:
            best_file_entropy = ("standard " + str(pred_num), entrop)

    print("Best standard for R component is: %s, entopy = %f" % best_r_entropy)
    print("Best standard for G component is: %s, entropy = %f" % best_g_entropy)
    print("Best standard for B component is: %s, entropy = %f" % best_b_entropy)
    print("Best standard for whole file is %s, entropy = %f" % best_file_entropy)

if __name__ == "__main__":
    main()