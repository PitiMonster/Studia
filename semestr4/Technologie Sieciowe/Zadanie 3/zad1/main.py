import decode
import encode
import filecmp


def main():
    test_infilename = 'random_bits_data_file.txt'
    test_outfilename = 'decoded_data.txt'
    encoded_filename = 'encoded_data'

    encode.create_32_bits_data(test_infilename)
    encode.encode_file(test_infilename, encoded_filename)
    decode.decode_file(encoded_filename, test_outfilename)

    if filecmp.cmp(test_infilename, test_outfilename):
        print("Work correctly!")
    else:
        print("Something went wrong!")

    return 0


if __name__ == "__main__":
    main()