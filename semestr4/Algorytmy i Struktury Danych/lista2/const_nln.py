import numpy

def main():
    data = []
    filename = "data_to_zad3.txt"
    with open(filename, "r") as file:
        data.extend([[x for x in line.split()] for line in file])

    dual_quick_const = 0
    dual_tests_amount = 0
    quick_const = 0
    quick_tests_amount = 0

    for arr in data:
        if str(arr[4]) == "dual_quick":
            dual_quick_const += float(int(arr[1])/(int(arr[0])*numpy.log(int(arr[0]))))
            dual_tests_amount += 1
        elif str(arr[4]) == "quick":
            quick_const += float(int(arr[1])/(int(arr[0])*numpy.log(int(arr[0]))))
            quick_tests_amount += 1

    print("Dual const: ", dual_quick_const/dual_tests_amount)
    print("Quick const: ", quick_const/quick_tests_amount)

if __name__ == '__main__':
    main()