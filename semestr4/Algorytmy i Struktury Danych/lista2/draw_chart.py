import numpy as np 
from matplotlib import pyplot as plt 
from operator import truediv

# globalne słowniki do trzymania danych 
tests_number_lists = {'insert': [], 'merge': [], 'quick': [], 'dual_quick': []}
comp_amount_lists = {'insert': [], 'merge': [], 'quick': [], 'dual_quick': []}
moves_amount_lists = {'insert': [], 'merge': [], 'quick': [], 'dual_quick': []}
time_lists = {'insert': [], 'merge': [], 'quick': [], 'dual_quick': []}

tests_number = {}
comp_amount = {}
moves_amount = {}
time = {}

""" funkcja rysująca wykresy średnie od n """
def draw_chart(elems, x_label, y_label, path_to_save, max_n_list):

    # dla wszysktich n dla których checmy zrobić wykresy
    for max_n in max_n_list:

        # ograniczamy max_n tak aby powstał wykres na podstawie danych które posiadamy
        if(max_n > 10000):
            max_n = 10000
        elif(max_n < 201):
            max_n = 201

        # zmienianie ścieżki zapisu dla każdego wykresu o innym max_n
        current_path = path_to_save
        current_path += str(max_n)

        # tworzenie tablicy wszystkich wartości x
        x = np.arange(100, max_n, 100)
        # liczba elementów tablicy które możemy wziąć na podstawie max_n
        elems_number = int(max(x)/100)

        # rysowanie wykresów
        plt.plot(x, list(map(truediv, elems['quick'],tests_number_lists['quick']))[:elems_number], 'r', label = "quick")
        plt.plot(x, list(map(truediv, elems['merge'], tests_number_lists['merge']))[:elems_number], 'b', label="merge")
        # plt.plot(x, list(map(truediv, elems['insert'], tests_number_lists['insert']))[:elems_number], 'g', label="insert")

        # odkomentować do rysowania danych dla dual pivot quick sort
        # plt.plot(x, list(map(truediv, elems['dual_quick'],tests_number_lists['dual_quick']))[:elems_number], 'y', label = "dual_quick")
        
        plt.xlabel(x_label) # ustawienie etykiety dla osi x
        plt.ylabel(y_label) # ustawienie etykiety dla osi y
        plt.legend()    # stworzenie legendy na podstawie labeli w plt.plot()
        plt.savefig(current_path)   # zapisanie wykresu do podanej ścieżki
        plt.clf()   # usunięcie danych na wykresie

""" funkcja rysująca średnie/n od n """
def draw_chart_div_n(elems, x_label, y_label, path_to_save, max_n_list):

    for max_n in max_n_list:

        if(max_n > 10000):
            max_n = 10000
        elif(max_n < 201):
            max_n = 201

        current_path = path_to_save
        current_path += str(max_n)

        # stworzenie tablicy o wszystkich możliwych ilościach elementów w tablicy
        n_amount = [i*100 for i in range(1,100)] 

        x = np.arange(100, max_n, 100)
        elems_number = int(max(x)/100)

        plt.plot(x, list(map(truediv, list(map(truediv, elems['quick'],tests_number_lists['quick'])), n_amount*np.log(n_amount)))[:elems_number], 'r', label = "quick")
        # plt.plot(x, list(map(truediv, list(map(truediv, elems['merge'], tests_number_lists['merge'])), n_amount))[:elems_number], 'b', label="merge")
        # plt.plot(x, list(map(truediv, list(map(truediv, elems['insert'], tests_number_lists['insert'])),n_amount))[:elems_number], 'g', label="insert")
        plt.plot(x, list(map(truediv, list(map(truediv, elems['dual_quick'],tests_number_lists['dual_quick'])), n_amount*np.log(n_amount)))[:elems_number], 'y', label = "dual_quick")

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.savefig(current_path)
        plt.clf()



""" funckja dodająca sumy danych dla konkretnych n do listy dla każdej funkcji sortującej """
def fill_list(list_name, data_name, n):

    list_name['insert'].append(data_name[n]['insert'])
    list_name['merge'].append(data_name[n]['merge'])
    list_name['quick'].append(data_name[n]['quick'])
    list_name['dual_quick'].append(data_name[n]['dual_quick'])

def main():

    filename = "data_to_zad3.txt"       # nazwa pliku z którego są pobierane dane do porównanie quick sorta i dual pivot quick sorta
    # filename = "comp.txt"           # plik z danymi do zadania 2
    data = []       # lista na wczytane dane z pliku
    with open(filename, "r") as file:
        # uzupełnienie listy data listami danych z każdej linijki z pliku wejściowego
        data.extend([[x for x in line.split()] for line in file])  


    for n in range(100, 10000, 100):
        # tworzenie słowników do sumowania danych dla konkretnych n
        tests_number[n] = {'insert': 0, 'merge': 0, 'quick': 0, 'dual_quick': 0}
        comp_amount[n] = {'insert': 0, 'merge': 0, 'quick': 0, 'dual_quick': 0}
        moves_amount[n] = {'insert': 0, 'merge': 0, 'quick': 0, 'dual_quick': 0}
        time[n] = {'insert': 0, 'merge': 0, 'quick': 0, 'dual_quick': 0}
        

        # uzupełnienie słowników danymi z pliku
        # arr[0] - ilość sortowanych elementów
        # arr[1] - ilość porównań
        # arr[2] - ilość przestawień
        # arr[3] - czas sortowania
        # arr[4] - nazwa funkcji sortującej
        for arr in data:
            if int(arr[0]) == n:
                tests_number[n][arr[4]] += 1
                comp_amount[n][arr[4]] += float(arr[1])
                moves_amount[n][arr[4]] += float(arr[2])
                time[n][arr[4]] += float(arr[3])

        # wypełnianie list zsumowanymi danymi dla konkretnych n
        fill_list(tests_number_lists, tests_number, n)
        fill_list(comp_amount_lists, comp_amount, n)
        fill_list(moves_amount_lists, moves_amount, n)
        fill_list(time_lists, time, n)
        
    # tworzenie listy o wartościach n dla których chcemy stworzyć wykres
    max_n_list = [201, 1000, 5001, 10000]

    # rysowanie wykresów
    # draw_chart(comp_amount_lists, "Elements amount", "Comparisons number", "charts//average_of_comp//without_insert_comp_n<=", max_n_list)
    # draw_chart(moves_amount_lists, "Elements amount", "Moves number", "charts//average_of_moves//without_insert_moves_n<=", max_n_list)
    # draw_chart(time_lists, "Elements amount", "Average exec time", "charts//average_of_time//without_insert_time_n<=", max_n_list)
    draw_chart_div_n(comp_amount_lists, "Elements amount", "Comparisons number", "charts//dual_quick_vs_quick//comp_divn_n<=", max_n_list)
    # draw_chart_div_n(moves_amount_lists, "Elements amount", "Moves number", "charts//dual_quick_vs_quick//comp_divn_n<=", max_n_list)
    print(comp_amount_lists['quick'])
    print(comp_amount_lists['dual_quick'])
    print("\n")
    print(list(map(truediv, comp_amount_lists['quick'],tests_number_lists['quick'])))
    print(list(map(truediv, comp_amount_lists['dual_quick'],tests_number_lists['dual_quick'])))
    print()
    n_amount = [i*100 for i in range(1,100)] 
    print(list(map(truediv, list(map(truediv, comp_amount_lists['quick'],tests_number_lists['quick'])), n_amount*np.log(n_amount))))
    print(list(map(truediv, list(map(truediv, comp_amount_lists['dual_quick'],tests_number_lists['dual_quick'])), n_amount*np.log(n_amount))))
    

if __name__ == '__main__':
    main()


