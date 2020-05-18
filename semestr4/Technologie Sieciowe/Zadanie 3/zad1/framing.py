from zlib import crc32

MAX_CONSECUTIVE_BITS_NUMBER = 5
START_FLAG = '01111110'
END_FLAG = '01111110'
CRC_LENGTH = 32

def count_crc32(data):
    return format(crc32(data.encode()), '0%db' % (CRC_LENGTH))

""" return data string with properly added 0 bits """
def bit_stuffing(data):
    result = ''
    one_counter = 0

    for d in data:
        if d == '1':
            one_counter += 1
            result += d
            if one_counter == MAX_CONSECUTIVE_BITS_NUMBER:
                result += '0'
                one_counter = 0
        else:
            one_counter = 0
            result += d

    return result

""" return data string without 0 bits added in bit_stuffing method """ 
def draw_back_bit_stuffing(data):
    result = ''
    one_counter = 0

    for d in data:
        if d == '1':
            result += d
            one_counter += 1
        else:
            if one_counter != MAX_CONSECUTIVE_BITS_NUMBER:
                result += d

            one_counter = 0
    
    return result
                
""" return data as a frame with its crc value"""
def encode_frame_data(data):
    data_crc32 = count_crc32(data)
    return START_FLAG + bit_stuffing(data+data_crc32) + END_FLAG

""" remove flags of frame from data """
def remove_flags(data):
    data1 = data[len(START_FLAG):-len(END_FLAG)]
    if len(data)-len(data1) != 16:
        print("error in removing flags")
        return 0
    return data1

""" return decoded data from frame if is valid """ 
def decode_frame_data(data):
    data = remove_flags(data)
    data = draw_back_bit_stuffing(data)
    decoded_data = data[:-CRC_LENGTH]
    crc_value = data[-CRC_LENGTH:]

    # check whether decoded_data is valid after drawing back bit stuffing
    if count_crc32(decoded_data) == crc_value:
        return decoded_data
    else:
        print("crss value are not equal!")
        return 0