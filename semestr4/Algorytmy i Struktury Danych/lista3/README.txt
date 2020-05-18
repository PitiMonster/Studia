Zadania należy kompilować przy pomocy g++ i odpowiednich argumentów podanych w poleceniu.

W folderze 'charts' zawarte są wszystkie wykresy dotyczące listy i porównań algorytmów.

Plik 'binary_search.pdf' dotyczy zadania 3. Dokładnie części dotyczącej Master Theorem.

Plik select_vs_r_select.png zawiera porównanie wyników dla zadania 2 dotyczącego średniej i odchylenia standardowego dla algorytmów select i random_select.

Zadanie 4 należy uruchamiać za pomocą narzędzia g++ oraz według parametrów z listy 2 zadania 2. Czyli np:
g++ zad4.cpp -o zad4
./zad4 --type dual_quick --comp '<=' --stat dane.txt 10

Wtedy zostaną wygenerowane tablice losowych liczb po 10 razy dla kazdego n w{100,200,...,10000} i zostaną one posortowane a wyniki tych sortowań zostaną zapisane do pliku dane.txt
