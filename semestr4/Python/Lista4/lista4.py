# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import time
from numpy.random import choice
import random
import time
from inspect import getfullargspec


# %%
def time_mes(fn):
    """ generator zwracajacy czas wykonania funkcji"""
    def modified_fn(*args):
        start = time.time() # zaczecie liczenia czasu
        fn(*args)
        return time.time() - start # zwrocenie roznicy czasu
    return modified_fn


@time_mes
def x(a, b, c):
    """funkcja liczaca iloczyn trzech liczb"""
    time.sleep(1)
    return a*b*c

print(x(5, 6, 7))


# %%

def add_leaf(i, tree):
    """ dodanie liscia do drzewa """
    k = 0
    for j, x in enumerate(tree):
        if x is None: # jeśli jest liściem pustym
            # jesli True to dodam nowego w miejsce tego pustego liścia
            if random.choice([True, False]):
                tree[j] = [str(i), None, None]
                k = i+1
        # jeśli liść jest listą to szukam tam wartości None, aby spróbować dodajć liść
        elif isinstance(x, list):
            tree[j], k = add_leaf(i, x)
        # k > i -> liść został dodany
        if k > i:
            return tree, k
    return tree, i


def height(tree, h=0, h_max=0):
    """ zwraca wysokość drzewa """
    # idę jak najniżej się da na każdej gałęzi
    for leaf in tree:
        if isinstance(leaf, list):
            h, h_max = height(leaf, h+1, h_max)

    # zmieniam h_max jeśli znalazłem dłużą gałąź
    if h_max < h:
        h_max = h
    return h-1, h_max


def gen_tree(n):
    """ tworzenie drzewa o podanej wysokości n """
    tree = ["0", None, None]
    i = 1
    k = 0
    while max(height(tree)) < n:
        # k > i -> liść został dodany
        while k <= i:
            tree, k = add_leaf(i, tree)
        i = k
    return tree

def dfs(tree):
    """ generator dfs chodzący po drzewie tree """
    for leaf in tree:
        if leaf is None:
            continue
        elif isinstance(leaf, str):
            yield leaf
        elif isinstance(leaf, list):
            for x in dfs(leaf):
                yield x

def bfs(tree):
    """ generator bfs chodzący po drzewie tree """
    q = []
    for leaf in tree:
        if leaf is None:
            continue
        if leaf[0] == "0":
            yield leaf[0]
        if isinstance(leaf, list):
            yield leaf[0]
            q.append(leaf)
    for leaf in q:
       for x in bfs(leaf):
           yield x

TREE = gen_tree(5)
print(TREE)
print(list(dfs(TREE)))
print(list(bfs(TREE)))


# %%

class Node(object):
    """ klasa opisująca obiekt drzewa """
   
    def __init__(self, father, name, height):
        """ konstruktor klasy Node """
        self.father = father
        self.name = name
        self.childs = []
        self.height = height
   
    def add_child(self, child_name):
        """ dodanie dziecka, do któregoś z node'ów """
        # 30% na dodanie dziecka do tego node'a
        if choice([True,False],1,[3,7]):
            new_child = Node(self.name, child_name, self.height + 1)
            self.childs.append(new_child)
            return True
        return False
    
    def get_childs(self):
        """ zwrócenie dzieci node'a """
        return self.childs
   
    def get_height(self):
        """ zwrócenie wysokości na której się znajduje node """
        return self.height
    
    def get_name(self):
        """ zwrócenie nazwy (numeru) node'a """
        return self.name


def insert_leaf(i, tree):
    """ wstawienie nowego liścia """
    k = 0
    if tree.add_child(str(i)):
        return i+1
    else:
        # jeśli się nie udało wstawić do node'a
        # to próba wstawienia, do którego z dzieci
        for child in tree.get_childs():
            k = insert_leaf(i, child)
            if k > i:
                return k
    return i

def height(tree, h=0):
    """ zwrócenie wysokości drzewa """
    # znalezienie najwiekszej wartości get_height() i jej zwrócenie
    if h < tree.get_height():
        h = tree.get_height()
    for leaf in tree.get_childs():
        h = height(leaf, h)
    return h


def gen_tree(n):
    """ generowanie drzewa wysokości n """
    tree = Node(None, "0", 0)
    i = 1
    k = 0
    while height(tree) < n:
        while k <= i:
            k = insert_leaf(i, tree)
        i = k
    return tree

def dfs(tree):
    """ generator dfs chodzący po tree """
    yield tree.get_name()
    for child in tree.get_childs():
        for x in dfs(child):
            yield x
    return


def bfs(tree):
    """ generator bfs chodzący po tree """
    q = []
    if tree.get_name() == "0":
        yield tree.get_name()
    for x in tree.get_childs():
        yield x.get_name()
        q.append(x)
    for x in q:
        for y in bfs(x):
            yield y
    return


def display_tree(tree):
    """ wyświetlenie drzewa w sposób Node : [Dzieci] """
    if len(tree.get_childs()) != 0:
        print("Father: ",tree.get_name(),end=' ')
        print("Children: ",end='')
        for x in tree.get_childs():
            print(x.get_name(),end=' ')
        print("\n")
        for x in tree.get_childs():
            display_tree(x)

TREE = gen_tree(5)
display_tree(TREE)
print(list(dfs(TREE)))
print(list(bfs(TREE)))


# %%

class Overload(object):
    """ klasa overload zwracająca funkcję o odpowiedniej ilości argumentów """

    functions = []
  
    def __init__(self, fn):
        """ konstruktor klasy """
        # dodanie funkcji do listy functions
        self.functions.append(fn)

    def __call__(self, *args):
        """ wywołanie odpowiedniej funkcji z listy """
        for fn in self.functions:
            try:
                return fn(*args)
            except:
                continue

@Overload
def x(a, b, c):
    """ funckja zwracająca iloczyn trzech liczb"""
    return a*b*c

@Overload
def x(a, b):
    """ funkcja zwracająca iloczyn dwóch liczb """
    return a*b

print(x(5, 6, 7))
print(x(5, 6))


# %%
