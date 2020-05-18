import re

root = None

class Node():
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key

    def __str__(self):
        return str(self.key)

    def __lt__(self, word):
        if type(word) == Node:
            word = word.key
        if len(word) <= len(self.key):
            shorter = (len(word), 'word')
        else:
            shorter = (len(self.key), 'key')
        
        for i in range(shorter[0]):
            if self.key[i] < word[i]:
                return True
            elif self.key[i] > word[i]:
                return False

        if shorter[1] == 'word':
            return False
        else:
            return True

    def __eq__(self, word):
        return self.key == word

    def get_root(self):
        root = self
        while root.parent is not None:
            root = root.parent

        return root

    def insert(self, new_string):
        # insert root
        if self.key is None:
            return Node(new_string, None)

        if self < new_string:
            if self.right is None:
                child = Node(new_string, self)
                self.right = child
                child.parent = self
            else:
                self.right.insert(new_string)
        else:
            if self.left is None:
                child = Node(new_string, self)
                self.left = child
                child.parent = self
            else:
                self.left.insert(new_string)       
        return

    def find(self, word):
        
        if self < word:
            if self.right is None:
                return 0
            return self.right.find(word)         
        elif self == word:
            return 1
        else:
            if self.left is None:
                return 0
            return self.left.find(word)

    def change_parent_child(self, side, child):
        if side == 'left':
            self.parent.left = child
            
        else:
            self.parent.right = child

        if child is not None:
            child.parent = self.parent

    def delete(self, word, side=None):
        if self < word:
            if self.right is None:
                return False
            return self.right.delete(word, 'right')        
        elif self == word:
            # delete root of btree
            if side is None:
                if self.left is None and self.right is None:
                    return None
                elif self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left
                else:
                    succ = self.successor()
                    succ.delete(succ.key, 'left')
                    succ.right = self.right
                    succ.left = self.left
                    self.left.parent = succ
                    self.right.parent = succ
                    succ.parent = None
                    return succ
            # delete any inner node
            else:
                if self.left is None and self.right is None:
                    self.change_parent_child(side, None)
                elif self.left is None:
                    self.change_parent_child(side, self.right)
                elif self.right is None:
                    self.change_parent_child(side, self.left)
                else:
                    succ = self.successor()
                    if succ.parent.left is not None:
                        if succ.parent.left == succ:
                            succ.delete(succ.key, 'left')
                        else:
                            succ.delete(succ.key, 'right')   
                    else:
                        succ.delete(succ.key, 'right')                    
                    succ.right = self.right
                    succ.left = self.left
                    succ.parent = self.parent
                    self.change_parent_child(side, succ)
                return True
        # if word < self
        else:
            if self.left is None:
                return False
            return self.left.delete(word, 'left')

    def successor(self):
        if self.right is None:
            p = self
            while p.parent is not None and p.parent.left != p:
                p = p.parent
            if p.parent is None:
                return False
            else:
                return p.parent
        return self.right.min()

    def min(self):
        min = self
        while min.left is not None:
            min = min.left
        return min

    def max(self):
        max = self
        while max.right is not None:
            max = max.right
        return max

    def inorder(self):
        if self.left is not None:
            for x in self.left.inorder():
                yield x
        
        yield str(self)
        
        if self.right is not None:
            for x in self.right.inorder():
                yield x

class BinaryTree():
    def __init__(self):
        self.root = Node(None, None)

    def insert(self, word):
        if self.root.key is None:
            self.root = self.root.insert(word)
        else:
            self.root.insert(word)

        # if root has changed
        if self.root.parent is not None:
            self.root = self.root.get_root()
        return True
    
    def delete(self, word):
        result = self.root.delete(word)

        if type(result) == bool:
            pass
        else:
            self.root = result
        # check whether root has changed
        if self.root is not None:
            if self.root.left is not None:
                self.root = self.root.left.get_root()
            elif self.root.right is not None:
                self.root = self.root.right.get_root()

    def find(self, word):
        return self.root.find(word)

    def min(self):
        return self.root.min()

    def max(self):
        return self.root.max()

    def successor(self, k):
        return k.successor()

    def inorder(self):
        return self.root.inorder()
