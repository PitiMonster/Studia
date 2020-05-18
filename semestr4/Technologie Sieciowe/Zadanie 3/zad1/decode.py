from framing import decode_frame_data


def decode_file(infilename, outfilename):
    infile = open(infilename, 'r')
    outfie = open(outfilename, 'w')
    outfie.write(decode_frame_data(infile.read()))

    infile.close()
    outfie.close()