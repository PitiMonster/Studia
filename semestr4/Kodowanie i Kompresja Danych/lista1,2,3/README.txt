Zadania nalezy uruchamiaz za pomoca instrukcji:
python nazwa_pliku.py

Zadanie lzw2 posiada dodatkowy argument ustalajacy sposob kodowania liczb calkowitych:
1. omega - koduje za pomoca Eliasa Omega
2. gamma - koduje za pomoca Eliasa Gamma
3. delta - koduje za pomoca Eliasa Delta
4. fibo - koduje za pomoca kodowania Fibonacciego

Przykladowe uzycie:
python lzw2.py fibo

Jesli nie poda sie argumentu ustalajacego kodowanie to automatycznie zostanie wywolane kodowanie Eliasa Omega. 

Prawdopodobnie bedzie trzeba doinstalowac pewne biblioteki. Nalezy to zrobic za pomoca instrukcji pip:
pip install nazwa_biblioteki

Pliki lzw2.py oraz arytmetyczne.py zwierają zmienne 'infilename' i 'outfilename', które zwierają odpowiednio plik kodowany oraz zdekodowany plik dekodowany.

Plik entropy.py jest stworzony w ten sposób, że liczy on entropię zwykłą i warunkową dla wszystkich plików .txt oraz .bin znajdujących się w tym samym folderze.