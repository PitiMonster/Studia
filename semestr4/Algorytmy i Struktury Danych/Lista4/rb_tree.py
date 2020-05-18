is_root_removed = False

class Node():
    def __init__(self, key, parent, color='red'):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.color = color
        self.second_color = None

    def __str__(self):
        # return ("key: %s, color: %s" % (str(self.key), self.color))
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

    def get_root(self):
        root = self
        while root.parent is not None:
            root = root.parent

        return root

    def rot_right(self):
        # self.left is for sure red color
        # if self is black color then self.left.left is red color
        # else self is red color
        self.left.parent = self.parent
        self.parent = self.left
        self.left = self.parent.right
        if self.parent.right is not None:
            self.parent.right.parent = self
        self.parent.right = self
        # if self.parent is not root
        if self.parent.parent is not None:
            if self.parent.parent.left is not None:
                if self.parent.parent.left == self:
                    self.parent.parent.left = self.parent
                    return True

            self.parent.parent.right = self.parent
            return True
        return True

    def rot_left(self):
        # self.right is for sure red color
        # if self is black color then self.right.right is red color
        # else self is red color
        self.right.parent = self.parent
        self.parent = self.right
        self.right = self.parent.left
        if self.parent.left is not None:
            self.parent.left.parent = self
        self.parent.left = self
        # if self.parent is not root
        if self.parent.parent is not None:
            if self.parent.parent.left is not None:
                if self.parent.parent.left == self:
                    self.parent.parent.left = self.parent
                    return True

            self.parent.parent.right = self.parent
            return True
        return True
        
    def correct_colors_after_insertion(self, side):
        if self.color == 'black':
            return  True
        # if two brothers are red
        if self.parent.left is not None and self.parent.right is not None:
            if self.parent.left.color == self.parent.right.color:
                self.parent.left.color = 'black'
                self.parent.right.color = 'black'
                self.parent.color = 'red'
                if self.parent.parent is None:
                    self.parent.color = 'black'
                    return True
                else:
                    if self.parent.parent.left is not None:
                        if self.parent == self.parent.parent.left:
                            return self.parent.parent.correct_colors_after_insertion('left')
                    
                    return self.parent.parent.correct_colors_after_insertion('right')


        if self.parent.left == self:
            if side == 'left':
                self.parent.rot_right()             
                self.right.color = 'red'
                self.color = 'black'
                return True
            else:
                self.rot_left()
                # if self was left child before rotation
                # if self.parent.parent.left == self.parent:
                return self.parent.correct_colors_after_insertion('left')

                # return self.parent.correct_colors_after_insertion('right')

                
        else:
            if side == "right":
                self.parent.rot_left()
                self.left.color = 'red'
                self.color = 'black'
                return True
            else:
                self.rot_right()
                # if self was left child before rotation
                # if self.parent.parent.left == self.parent:
                    # return self.parent.correct_colors_after_insertion('right')

                return self.parent.correct_colors_after_insertion('right')


    def insert(self, word):
        # insert root 
        if self.key is None:
            return Node(word, None, 'black')

        if self < word:
            if self.right is None:
                child = Node(word, self)
                self.right = child
                self.correct_colors_after_insertion('right')
            else:
                self.right.insert(word)
        else:
            if self.left is None:
                child = Node(word, self)
                self.left = child
                self.correct_colors_after_insertion('left')
            else:
                self.left.insert(word)       


    
    def delete(self, word, side=None):
        global is_root_removed
        if self < word:
            if self.right is None:
                return False
            return self.right.delete(word, 'right')        
        elif self == word:

            if self.parent is None:
                is_root_removed = True
            # if removed node has no childs
            if self.left is None and self.right is None:
                if is_root_removed:
                    return None
                if side == 'left':
                    self.parent.left is None
                return True

            # if node has only left child
            elif self.right is None:
                if is_root_removed:
                    self.left.color = 'black'
                    self.left.parent = None
                    return True
                if self.parent.color == 'red' and self.left.color == 'red':
                    self.left.color = 'black'
                    
                if side == 'left':
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left

                self.left.parent = self.parent
                return  True

            # if node has only right child
            elif self.left is None:
                if is_root_removed:
                    self.right.color = 'black'
                    self.right.parent = None
                    return True
                if self.parent.color == 'red' and self.right.color == 'red':
                    self.right.color = 'black'

                if side == 'left':
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right

                self.right.parent = self.parent

                return True

            # if right son is successor
            elif self.right.left is None:

                self.left.parent = self.right
                self.right.left = self.left
                if side == 'left':
                    self.parent.left = self.right
                elif side == 'right':
                    self.parent.right = self.right

                self.right.parent = self.parent
                if self.right.color == 'red':
                    self.right.color = self.color
                    return True
                
                # if successor has no children
                elif self.right.right is None:
                    self.right.right = Node(None, self.right)
                    
                self.right.right.second_color = 'black'
                self.right.right.after_delete_fixup('right')
                
                # return True

            # if right son is not successor
            else:
                succ = self.successor()
                self.key = succ.key
                if succ.right is None:
                    succ.right = Node(None, self) 
                succ.parent.left = succ.right            
                succ.right.parent = succ.parent
                if succ.color == 'red':
                    succ.right.color = 'red'
                    self.get_root().remove_none_key_nodes()
                    return True
                else:
                    succ.right.second_color = 'black'

                succ.right.after_delete_fixup('left')
                # self.remove_none_key_nodes()
                # return True
                
            self.get_root().remove_none_key_nodes()
            return True

        # if word < self
        else:
            if self.left is None:
                return False
            return self.left.delete(word, 'left')

    def first_case(self, side):
        if side == 'left':
            if self.parent.right.color == 'red':
                self.parent.right.color = 'black'
                # self.parent.right.rot_left()
                self.parent.rot_left()
                self.parent.color = 'red'
        else:
            if self.parent.left.color == 'red':
                self.parent.left.color = 'black'
                # self.parent.left.rot_right()
                self.parent.rot_right()
                self.parent.color = 'red'

        return True


    def second_case(self, side):
        if side == 'left':
            bro = self.parent.right
            if bro.color == 'black':
                if bro.right is None:
                    bro.right = Node(None, bro, 'black')
                if bro.left is None:
                    bro.left = Node(None, bro, 'black')
                if bro.left.color == 'black' and bro.right.color == 'black':
                    bro.color = 'red'
                    self.second_color = None
                    self.parent.second_color = 'black'
                    if self.parent.parent is None:
                        side = None
                    elif self.parent.parent.left == self.parent:
                        side = 'left'
                    else:
                        side = 'right'

                    self.parent.after_delete_fixup(side) 
                    
                    return True      
        else:
            bro = self.parent.left
            if bro.color == 'black':
                if bro.right is None:
                    bro.right = Node(None, bro, 'black')
                if bro.left is None:
                    bro.left = Node(None, bro, 'black')
                if bro.left.color == 'black' and bro.right.color == 'black':
                    bro.color = 'red'
                    self.second_color = None
                    self.parent.second_color = 'black'
                    if self.parent.parent is None:
                        side = None
                    elif self.parent.parent.left == self.parent:
                        side = 'left'
                    else:
                        side = 'right'
                    self.parent.after_delete_fixup(side)
                    return True

        return False

    def third_case(self, side):
        if side == 'left':
            bro = self.parent.right
            if bro.color == 'black':
                if bro.left.color == 'red' and bro.right.color == 'black':
                    bro.color = 'red'
                    bro.left.color = 'black'
                    bro.rot_right()
        else:
            bro = self.parent.left
            if bro.color == 'black':
                if bro.right.color == 'red' and bro.left.color == 'black':
                    bro.color = 'red'
                    bro.right.color = 'black'
                    bro.rot_left()

        return True

    def fourth_case(self, side):
        if side == 'left':
            bro = self.parent.right
            if bro.color == 'black' and bro.right.color == 'red':
                bro.color = self.parent.color
                bro.right.color = 'black'
                self.parent.color = 'black'
                self.second_color = None
                self.parent.rot_left()
                return True
        else:
            bro = self.parent.left
            if bro.color == 'black' and bro.left.color == 'red':
                bro.color = self.parent.color
                bro.left.color = 'black'
                self.parent.color = 'black'
                self.second_color = None
                self.parent.rot_right()
                return True

        return False

    # remove temporary nodes added during delete method
    def remove_none_key_nodes(self):
        if self.left is not None:
            if self.left.key is None:
                self.left = None
            else:
                self.left.remove_none_key_nodes()
        
        if self.right is not None:
            if self.right.key is None:
                self.right = None
            else:
                self.right.remove_none_key_nodes()

        return True

    def after_delete_fixup(self, side):
        if self.parent == None:
            self.color = 'black'
            return True
        self.first_case(side)
        if self.second_case(side):
            return True
        self.third_case(side)
        if self.fourth_case(side):
            return True

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

    def inorder(self):
        if self.left is not None:
            for x in self.left.inorder():
                yield x
        
        yield str(self)
        
        if self.right is not None:
            for x in self.right.inorder():
                yield x


class RBTree():

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
        if self.root is None:
            return
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


        