import binary_tree
import rb_tree
import hmap
import sys
import re
import time

struct = None
insert_num = 0
delete_num = 0
find_num = 0
min_num = 0
max_num = 0
greatest_elem_number = 0
curr_elem_num = 0
succ_num = 0


'''
remove not letter chars 
from beginning and end of give string
'''
def fix_word(word):
    is_letter = re.compile('[^a-zA-Z]')
    while is_letter.match(word[0]) is not None:
        word = word[1:]
    while is_letter.match(word[-1]) is not None:
        word = word[:-1]

    return word

def insert(word):
    global struct
    global insert_num
    global curr_elem_num
    global greatest_elem_number

    insert_num += 1
    curr_elem_num += 1
    if curr_elem_num > greatest_elem_number:
        greatest_elem_number = curr_elem_num
    word = fix_word(word)
    return struct.insert(word)

def delete(word):
    global struct
    global delete_num
    global curr_elem_num

    delete_num += 1
    word = fix_word(word)
    struct.delete(word)
    curr_elem_num -= 1
    return

def find(word):
    global struct
    global find_num

    find_num += 1
    word = fix_word(word)
    print(struct.find(word))

def min():
    global struct
    global min_num

    min_num += 1
    print(struct.min())

def max():
    global struct
    global max_num

    max_num += 1
    print(struct.max())

def load(filename):
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split():
                    insert(word)

def successor(node):
    global struct
    global succ_num

    succ_num += 1
    result = struct.successor(node)

    if not result:
        print()
    else:
        print(result)


def inorder():
    global struct
    if len(list(struct.inorder())):
        print(list(struct.inorder()))

def set_struct_type(obj):
    global struct

    struct = obj

def main():
    global struct
    global insert_num
    global delete_num
    global min_num
    global max_num
    global succ_num
    global find_num
    global curr_elem_num
    global greatest_elem_number

    start = time.time()
    args = list(sys.argv)
    struct_type = str(args[2])
    if struct_type == 'bst':
        struct = binary_tree.BinaryTree()
    elif struct_type == 'rbt':
        struct = rb_tree.RBTree()
    elif struct_type == 'hmap':
        struct = hmap.HashMap()
    else: 
        struct = None
        return 0
    functions_number = int(input())
    while functions_number:
        function = input()
        args = None
        try:
            name, args = function.split(" ")
        except:
            name = function.split(" ")[0]
        print(name)
        if args is not None:
            eval(name)(args)
        else:
            eval(name)()
        functions_number -= 1

    end = time.time()
    print("Czas działania: %s" % (str(end-start)), file=sys.stderr)
    print("Liczba operacji:", file=sys.stderr)
    print("Insert: %d, delete: %d, min: %d, max: %d, find: %d, successor: %d" % (insert_num, delete_num, min_num, max_num, find_num, succ_num), file=sys.stderr)
    print("Maksymalne zapełnienie struktury: %d" % (greatest_elem_number), file=sys.stderr)
    print("Końcowe zapełnienie struktury: %d" % (curr_elem_num), file=sys.stderr)

if __name__ == "__main__":
    main()