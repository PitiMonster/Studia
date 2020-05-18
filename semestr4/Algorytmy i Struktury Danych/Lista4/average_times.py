import random
import string
import hmap
import binary_tree
import rb_tree
import time

def random_string(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def gen_test_file(function_name):
    filename = function_name+'_test_data.txt'
    with open(filename, 'w') as file:
        for _ in range(100000):
            if function_name in ['min', 'max']:
                file.write(function_name+"\n")
            else:
                file.write(function_name + " " + random_string(5)+"\n")


def gen_test_files():
    gen_test_file('insert')
    gen_test_file('delete')
    gen_test_file('find')
    gen_test_file('max')
    gen_test_file('min')

def test_function_time():
    hash_map = hmap.HashMap()
    rbtree = rb_tree.RBTree()
    bstree = binary_tree.BinaryTree()
    
    while True:
        try:
            results = {'insert': [], 'delete': [], 'find': [], 'max': [], 'min': []}

            # testing insertion average time
            filename = 'insert_test_data.txt'
            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    rbtree.insert(arg)
                end = time.time()

            results['insert'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    bstree.insert(arg)
                end = time.time()

            results['insert'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    hash_map.insert(arg)
                end = time.time()

            results['insert'].append((end-start)/100000)

            # testing find average time
            filename = 'find_test_data.txt'
            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    rbtree.find(arg)
                end = time.time()

            results['find'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    bstree.find(arg)
                end = time.time()

            results['find'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    hash_map.find(arg)
                end = time.time()

            results['find'].append((end-start)/100000)



            # testing max average time
            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    rbtree.max()
                end = time.time()

            results['max'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    bstree.max()
                end = time.time()

            results['max'].append((end-start)/100000)

            # testing min average time
            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    rbtree.min()
                end = time.time()

            results['min'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    bstree.min()
                end = time.time()

            results['min'].append((end-start)/100000)


            # testing delete average time
            filename = 'find_test_data.txt'
            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    rbtree.delete(arg)
                end = time.time()

            results['delete'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    bstree.delete(arg)
                end = time.time()

            results['delete'].append((end-start)/100000)

            with open(filename, 'r') as file:
                content = file.readlines()
                start = time.time()
                for c in content:
                    _, arg = c.split(" ")
                    hash_map.delete(arg)
                end = time.time()

            results['delete'].append((end-start)/100000)

            print("Insert:")
            print("rbtree: %f" % (results['insert'][0]))
            print("bstree: %f" % ((results['insert'][1])))
            print("hmap: %f" % ((results['insert'][2])))

            print("Delete:")
            print("rbtree: %f" % ((results['delete'][0])))
            print("bstree: %f" % ((results['delete'][1])))
            print("hmap: %f" % ((results['delete'][2])))

            print("Find:")
            print("rbtree: %f" % ((results['find'][0])))
            print("bstree: %f" % ((results['find'][1])))
            print("hmap: %f" % ((results['find'][2])))

            print("Max:")
            print("rbtree: %f" % ((results['max'][0])))
            print("bstree: %f" % ((results['max'][1])))

            print("Min:")
            print("rbtree: %f" % ((results['min'][0])))
            print("bstree: %f" % ((results['min'][1])))
            return 

        except:
            main()

    

def main():
    gen_test_file('insert')
    gen_test_file('delete')
    gen_test_file('find')
    gen_test_file('min')
    gen_test_file('max')
    test_function_time()



if __name__ == "__main__":
    main()


    
