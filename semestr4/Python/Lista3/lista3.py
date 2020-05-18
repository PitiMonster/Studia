# %%
''' funkcja dookonująca transpozycji macierzy kwadratowej '''
def transpozycja(macierz):
    # tworzenie list z tych samych (w sensie kolejności) elementów list
    # łączenie ich za pomocą spacji
    return [" ".join([rzad.split()[i] for rzad in macierz]) for i in range(len(macierz))]

if __name__=='__main__':
   macierz = ['1.1 2.2 3.3', '4.4 5.5 6.6', '7.7 8.8 9.9']
   print(transpozycja(macierz))


# %%
''' funkcja tworząca listę prostą z listy zagnieżdżonej ''' 
def flatten(l):
    for elem in l:
        # jeśli element jest listą to rekurencyjnie go rozkładamy
        if isinstance(elem, list): 
            for nested_elem in flatten(elem):
                yield nested_elem
        else:
            yield elem
        

if __name__=='__main__':
     l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
     print(list(flatten(l)))
     


# %%
def count_bytes(filename):
    with open(filename, "r") as file:
        return sum([int(line.split()[-1]) for line in file])

if __name__=='__main__':
    filename = 'count_bytes.txt'
    print("Całkowita liczba bajtów: ",count_bytes(filename))


# %%
''' algorytm quick sort z wykorzystaniem filter '''
def q_sort_filter(l):
    return l if len(l) <= 1 else (
        # filtrowanie elementów które są < l[0]
        q_sort_filter(list(filter(lambda k: k < l[0], l[1:]))) 
        + [l[0]] 
        + q_sort_filter(list(filter(lambda k: k >= l[0], l[1:])))
     )

''' algorytm quick sort z wykorzystaniem listy składanej '''
def q_sort_list(l):
    return l if len(l) <= 1 else (
        q_sort_list([elem for elem in l[1:] if elem < l[0]]) 
        + [l[0]] 
        + q_sort_list([elem for elem in l[1:] if elem >= l[0]])
    )

if __name__=='__main__':
    x= [3,2,3,1,5,6,2,8,9,2,3,2]
    print(q_sort_filter(x))
    print(q_sort_list(x))


# %%
''' funkcja zwracająca wszystkie podzbiory zbioru '''
def subsets_map_lambda(l):
    return [[]] if len(l) == 0 else ( 
        # mapowanie zbiorów na połączone zbiory za pomocą lambdy
        list(map(lambda x: [l[0],*x], subsets_map_lambda(l[1:]))) 
        # dołączanie reszty podzbiorów bez elementu l[0] 
        + subsets_map_lambda(l[1:])
    )

def subsets(l):
    return [[]] if len(l) == 0 else (
        # łączenie wszystkich zbiorów z elementem l[0]
        [[l[0],*x] for x in subsets(l[1:])] 
        + subsets(l[1:])
    )


print(subsets_map_lambda([1,2,3]))
print(subsets([1,2,3]))


# %%


