def find_intersection():
    string1 = input("First: ")
    string2 = input("Second: ")
    arr1 = [x.strip('\'\" ') for x in string1.split(',')]
    arr2 = [x.strip('\'\" ') for x in string2.split(',')]
    ret = [x for x in arr1 if x in arr2]
    print("Output: ", end='')
    if ret:
        print(', '.join(ret))
    else:
        print("false")


if __name__ == "__main__":
    find_intersection()
