

def minimum(stacje, od, do):
    mini = None
    index = do
    for i in range(od,do+1):
        v = stacje[i]
        if v != 0 and (mini == None or mini > v):
            index = i
            mini = v

    return index


def licz_droge(stacje, W):
    # lista par (cena paliwa, km od startu)
    stacje = stacje
    W = W
    n = len(stacje)
    # km na którym znajduje się ostatnia stacja
    dł_drogi = stacje[-1][1] 
    nr_stacji = 0
    # i-ty indeks cena na stacji na i-tym km
    odwiedzone_stacje = [0] * (dł_drogi + 1)
    koszt = 0
    km = 0
    # stacja na której ostatnio tankowaliśmy najtańsze paliwo
    min_s  = stacje[nr_stacji]
    # aktualne km od min_s
    km_min = 0
    # na i-tym indeksie jest ilość litrów do kupienia na stacji na i-tym km
    wynik = [0] * (dł_drogi + 1) 
    odwiedzone_stacje[0] = min_s[0]
    
    
    while nr_stacji < n - 1:
        nr_stacji += 1
        różnica = stacje[nr_stacji][1] - km
        # jeśli jesteśmy w stanie na min_s zatankować wystarczająco 
        # paliwa by dojechać dalej to tak robimy
        if km_min + różnica <= W:
            koszt += min_s[0] * różnica
            wynik[min_s[1]] += różnica
        else:
            # min_s, z którego damy radę dojechać do następnej stacji
            indeks = minimum(odwiedzone_stacje, max(0, km - W + różnica), km)
            # ilość km, które kupimy przed stacją na indeks km, które są tańsze niż na niej
            tańsze_km = min_s[1] + W - km
            koszt += tańsze_km * min_s[0]
            wynik[min_s[1]] += tańsze_km
            prev_min_i = min_s[1]
            # kolejne minimum przed stacją indeks
            temp_min_i = minimum(odwiedzone_stacje, prev_min_i + 1, indeks)
            # dopóki stacja z mniejszą ceną paliwa przed stacją indeks
            while odwiedzone_stacje[temp_min_i] < odwiedzone_stacje[indeks]:
                koszt += (temp_min_i - prev_min_i) * odwiedzone_stacje[temp_min_i]
                # tankujemy na tej stacji do pełna, czyli tyle ile przejchaliśmy od poprzendiego tankowania
                # bo tam też tankowaliśmy do pełna
                tańsze_km += temp_min_i - prev_min_i
                wynik[temp_min_i] += temp_min_i - prev_min_i
                prev_min_i = temp_min_i
                # na trasie od stacji na której teraz tankujemy do pełna
                # do stacji indeks szukamy kolejnej tańszej stacji
                temp_min_i = minimum(odwiedzone_stacje, prev_min_i + 1, indeks)
            
            # na stacji indeks kupujemy tyle paliwa ile nam jeszcze brakuje 
            # by dojechać do następnej stacji
            koszt += odwiedzone_stacje[indeks] * ( różnica - tańsze_km)
            wynik[indeks] += różnica - tańsze_km
            min_s = (odwiedzone_stacje[indeks], indeks)
            km_min = km - min_s[1]

        if stacje[nr_stacji][0] <= min_s[0]:
            min_s = stacje[nr_stacji]
            km_min = 0
        else:
            km_min += różnica

        km += różnica
        odwiedzone_stacje[km] = stacje[nr_stacji][0]
        

    return wynik, koszt

def main():
    stacje = [(5,0), (6,3), (4,5), (5,9), (7,12), (8,14), (10000000, 19)]
    W = 6
    wynik, koszt = licz_droge(stacje, W)
    print(f"wynik:{wynik}\n koszt: {koszt}")

if __name__ == "__main__":
    main()