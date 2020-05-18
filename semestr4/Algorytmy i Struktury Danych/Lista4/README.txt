Pliki rbtree.py, binary_tree.py, hmap.py zawierają trzy wymagane struktury. Wszystkie one są obsługiwane przez plik main.py. 

Program należy uruchamiać przy pomocy polecenia python3 np:
python3 main.py --type bst <./input.txt >out.res

Gdzie input.txt jest plikiem z wyowłaniami metod, a out.res zawiera wyniki tych wywołań.

Dane wejściowe podajemy jak w przykładzie zawartym w zadaniu.

Plik count_n.py wylicza najlepszą długość listy w hash mapie, aby opłacało się już przejść na rbtree. Wygenerowałem dane 100 tysięcy insertów i deletów.
Sprawdzałem później te dane dla tresholda od 1 do 1000. Do tresholda 551 najlepszą długością było 27 jednak później zaczęły się trochę zmieniać te czasy i ostatecznie skończyło się na treshold = 984.
Między czasem dla tresholda 984 a 27 jest zaledwie 4 setne sekundy różnicy.


Plik average_times.py wylicza średnie czasy dla każdej z metod insert, delete, find, max, min. Generuję tam 5 plików z danymi dla każdej metody po 100 tysięcy danych w każdym. 
Później dla każdej struktury wywołuję te pliki z operacjami, wyliczam średni czas jaki zajęło wykonanie tych 100 tysięcy operacji. Przykładowy rezultat:

Insert:
rbtree: 0.000021
bstree: 0.000027
hmap: 0.000001
Delete:
rbtree: 0.000158
bstree: 0.000030
hmap: 0.000001
Find:
rbtree: 0.000021
bstree: 0.000025
hmap: 0.000001
Max:
rbtree: 0.000001
bstree: 0.000001
Min:
rbtree: 0.000001
bstree: 0.000001
