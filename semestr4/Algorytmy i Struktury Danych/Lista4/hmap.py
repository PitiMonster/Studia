import rb_tree
import sys

class HashMap():

    def __init__(self, length=1000000, max_treshold=984):
        self.length = length
        self.hash_table = [('table', []) for _ in range(self.length)]
        self.max_treshold = max_treshold

    def insert(self, word):
        hashed_key = hash(word) % self.length

        if self.hash_table[hashed_key][0] == 'table':
            self.hash_table[hashed_key][1].append(word)
            
            # przejście na rbtree jeśli przekroczyliśmy ilość dozwolonych elementów
            if len(self.hash_table[hashed_key][1]) >= self.max_treshold:
                tree = rb_tree.RBTree()
                for key in self.hash_table[hashed_key][1]:
                    tree.insert(key)
                self.hash_table[hashed_key] = ('tree', tree)
        else:
            self.hash_table[hashed_key][1].insert(word)

    def find(self, word):
        hashed_key = hash(word) % self.length
        if self.hash_table[hashed_key][0] == 'table':
            if word in self.hash_table[hashed_key][1]:
                return 1

            else:
                return 0
        else:
            if self.hash_table[hashed_key][1].root is not None:
                return self.hash_table[hashed_key][1].find(word)
            else:
                return 0

    def delete(self, word):
        hashed_key = hash(word) % self.length
        if self.hash_table[hashed_key][0] == 'table':
            # print("xd ", word)
            if word in self.hash_table[hashed_key][1]:
                self.hash_table[hashed_key][1].remove(word)
        else:
            self.hash_table[hashed_key][1].delete(word)

            # wracanie do listy jeśli znów jest mniej elementów niż self.max_treshold
            if self.hash_table[hashed_key][1].root is not None:
                lista = list(self.hash_table[hashed_key][1].inorder())
                if len(lista) < self.max_treshold:
                    self.hash_table[hashed_key] = ('table', lista)


    def min(self):
        return "\n"

    def max(self):
        return "\n"

    def successor(self):
        return "\n"

    def inorder(self):
        return ""

    def display(self):
        for i in range(self.length):
            if self.hash_table[i][0] == 'table':
                if len(self.hash_table[i][1]) > 0:
                    print(self.hash_table[i])
            else:
                if self.hash_table[i][1].root is not None:
                    print(list(self.hash_table[i][1].inorder()))

        return ""