from PIL import Image
import numpy
from bitarray import bitarray
import sys

''' 
funckja przeprowadzająca kwantyzację wektorową na pliku infilename
zwraca obrac outfilename o ilości kolorów 2**number_colors
'''
def quantization(infilename, outfilename, colors_number):

    with open(infilename, 'rb') as file:
        content = file.read()

    # nagłówek i stopka kodowanego obrazu w formacie TGA
    header = content[:18]
    footer = content[-26:]
    picture_bytes = content[18:-26]


    pixel_values = []
    # dzielenie listy bitów obrazka na tuple  wartości pikseli
    for i in range(0, len(picture_bytes), 3):
        pixel_values.append(tuple(picture_bytes[i:i+3]))

    colors_number = 2**colors_number

    # stała o którą będziemy przesuwać wektor przy jego podziale na dwa nowe wektory
    pert_vect = 1

    # lista kolorów wyjściowych
    codebook = []

    # pierwszy kolor jako średnia całego obrazka
    r0 = avg_of_vectors(pixel_values)
    codebook.append(r0)

    # lista najbliżysz wektorów r dla każdego piksela
    pixels_nearest_r = [r0] * len(pixel_values)
    avg_err = avg_quant_err(pixels_nearest_r, pixel_values)

    # dopóki nie mamy oczekiwanej liczby kolorów podwajamy ją używając algorytmu lbg
    while len(codebook) < colors_number:
        print(len(codebook))
        codebook, avg_err, pixels_nearest_r = lbg(codebook, avg_err, pert_vect, pixel_values)

    # tworzenie listy bajtów z wszystkich pikseli
    result_pixels = [pixel for sublist in pixels_nearest_r for pixel in sublist]


    header = list(header)
    footer = list(footer)
    header.extend(result_pixels)
    header.extend(footer)
    content = ''

    for h in header:
        content += format(h, '08b')
    x = bitarray(content)
    temp_file = open(outfilename, 'wb')
    x.tofile(temp_file)
    temp_file.close()


    original_mse = avg_quant_err(pixel_values, [(0, 0, 0)]*len(pixel_values))

    print("Błąd średniokwadratowy uzyskanego obrazu: %f" % (avg_err))
    print("Stosunek sygnału do szumu: %f" % (original_mse/avg_err))

''' 
algorytm lbg do dzielenia listy wektorów na przedziały
i znajdowanie średniej wartości każdego z przedziałów
 '''
def lbg(codebook, avg_err, pert_vect, pixel_values):
    # lista najbliższych wektorów r dla każdego piksela
    pixels_nearest_r = [None] * len(pixel_values)

    # dzielenie każdego wektora z codebooka na dwa odsunięte od siebie wektory
    new_codebook = []
    for r in codebook:
        first_r = move_vector(r, pert_vect)
        second_r = move_vector(r, -pert_vect)
        new_codebook.append(first_r)
        new_codebook.append(second_r)

    codebook = new_codebook

    error = 1
    # maksymalny dopuszczalny błąd
    MAX_TRESHOLD = 0.1
    while error > MAX_TRESHOLD:

        # słownik z wektorami r jako klucze i ich najbliższymi pikselami jako wartości
        r_pixels = dict((r, []) for r in codebook)
        # słownik z wektorami r jako klucze i ich najbliższych pikseli indeksami jako wartości
        r_pixels_id = dict((r, []) for r in codebook)

        for i, pixel in enumerate(pixel_values):
            min_dist = None
            nearest_r = None
            for r in codebook:
                dist = squared_err(r, pixel)
                if min_dist is None or min_dist > dist:
                    nearest_r = r
                    min_dist = dist

            pixels_nearest_r[i] = nearest_r
            r_pixels[nearest_r].append(pixel)
            r_pixels_id[nearest_r].append(i)

        # liczenie nowego najlepszego wektora r dla każdego przedziału
        for r_i, pixels in enumerate(r_pixels.values()):
            if len(pixels) > 0:  
                old_r = list(r_pixels.keys())[r_i]
                new_r = avg_of_vectors(pixels)
                codebook[r_i] = new_r
                # aktualizowanie wektora r dla każdego punktu z tego przedziału
                for i in r_pixels_id[old_r]:
                    pixels_nearest_r[i] = new_r

        # liczenie nowego mse
        new_avg_err = avg_quant_err(pixels_nearest_r, pixel_values)

        # liczenie aktualnego błędu
        error = (avg_err - new_avg_err)/new_avg_err
       
        avg_err = new_avg_err

    return codebook, avg_err, pixels_nearest_r

''' zwrócenie mse podanych list'''
def avg_quant_err(r_list, vecotrs):
    result = 0
    for i, vect in enumerate(vecotrs):
        result += squared_err(r_list[i], vect)

    return result/len(vecotrs)

''' 
zwrócenie miary kwadratowej błedu 
dla podanych wektorów
'''
def squared_err(r, x):
    return sum((a-b)**2 for a,b in zip(r,x))

''' wyliczenie średniej wartości podanej listy wektorów '''
def avg_of_vectors(vectors, size=3):
    avg_vector = [0.0]*size
    vect_num = len(vectors)
    for vect in vectors:
        for i, v in enumerate(vect):
            avg_vector[i] += v / vect_num

    avg_vector = tuple([int(x) for x in avg_vector])
    return avg_vector

''' przesunięcie wektora o podany dystans '''
def move_vector(vector, dist):
    return tuple([v+dist for v in vector])

def main():
    args = list(sys.argv)
    infilename = str(args[1])
    outfilename = str(args[2])
    colors_num = int(args[3])
    quantization(infilename, outfilename, colors_num)

if __name__ == "__main__":
    main()