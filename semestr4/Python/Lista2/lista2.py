
# %%
import os
import re

def count(filename):
    with open(filename,"r") as file:
        content = file.read()
        lines = content.split("\n")
        text = content.strip().split()
        return os.path.getsize(filename),             len(lines),             len(text),             max(len(line) for line in lines)

filename = "test_decode.txt"
bytess, lines, words, charss = count(filename)
print("bytes amount: ", bytess)
print("lines amount: ", lines)
print("words amount: ", words)
print("characters amount: ", charss)


# %%
""" function encoding file content from ASCII to base64"""
def encode(filename):
    base_64_encoding_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    with open(filename,"rb") as file:
        content = file.read()
        bins = str()
        for bit in content:
            # fromat up to eight chars because bin function truncates zeros
            # from the beginning
            bins += '{:0>8}'.format(str(bin(bit))[2:])
        # add zeros to divide by 6
        while len(bins) % 6:
            bins += '00'
        binsLength = len(bins)
        # insert ' ' every six chars to split bins to Base64 chars
        for i in range(6, len(bins) + int(len(bins)/6),7):
            bins = bins[:i] + ' ' + bins[i:] 
        bins = bins.split(' ')
        if '' in bins:
            bins.remove('')
        code = str()
        for b in bins:
            code += base_64_encoding_characters[int(b,2)]
        # add necessary padding characters
        while binsLength % 8:
            code += '='
            binsLength += 6
    
        return code

""" function decoding file content from base64 to ASCII"""
def decode(filename):
    base_64_encoding_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    with open(filename,"r") as file:
        content = file.read()
        bins = str()
        for b in content:
            if b != '=':
                # fromatting up to six chars because bin function truncates zeros
                # from the beginning
                bins += '{:0>6}'.format(
                    str(bin(base_64_encoding_characters.index(b)))[2:]
                    )
        # deleting useless zeros from bins
        while len(bins) % 8:
            bins = bins[:len(bins)-2]
        # insert ' ' every eight chars to split bins to ASCII chars
        for i in range(8, len(bins)+int(len(bins)/8), 9):
            bins = bins[:i] + ' ' + bins[i:]
        bins = bins.split(' ')
        if '' in bins:
            bins.remove('')
        code = str()
        for b in bins:
            code += chr(int(b,2))
        
        return code
"""function testing program operation"""
def test():
    filename_encode = "test_encode.txt"
    filename_decode = "test_decode.txt"
    if encode(filename_encode) == "UHl0aG9u" and decode(filename_decode) == 'Python':
        return True
    else: 
        return False

if __name__ == '__main__':
    print(test())



# %%
import os
""" change filenames to lowercase """
def files_to_lower():
    this_dir = os.getcwd()

    # r - root, d - directories, f - filenames
    for r, d, f in os.walk(this_dir):
        for dictio in d:
            src = r + "\\" + dictio
            dst = r + "\\" + dictio.lower()
            os.rename(src,dst)
        for ffile in f:
            src = r + "\\" + ffile
            dst = r + "\\" + ffile.lower()
            os.rename(src,dst)

if __name__ == '__main__':
  files_to_lower()


# %%
import os
import hashlib

# print all the same files
def rep_checker():
    # dictionary which stores file_hash as a key
    # and list of paths of the same files as a value
    my_dict = {}
    this_dir = os.getcwd()

    for r, d, f in os.walk(this_dir):
        for filename in f:
            content_hash = str()
            fil = r + "\\" + filename
            with open(fil, "r") as file:
                content = file.read()
                content_hash = hashlib.sha256(str(content).encode()).hexdigest()

            size_hash = hashlib.sha256(str(os.path.getsize(fil)).encode()).hexdigest()
            file_hash = size_hash + content_hash

            if file_hash in my_dict:
                my_dict[file_hash].append(fil)
            else:
                my_dict[file_hash] = [fil]
    
    for key, value in my_dict.items():
        if len(value) > 1:
            print("-------------------------")
            for i in range(len(value)):
                print(value[i])

    print("-------------------------")



if __name__ == '__main__':
    rep_checker()
    

