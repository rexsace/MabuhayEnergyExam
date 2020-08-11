def find_intersection(string1=None, string2=None):
    if string1 is None:
        string1 = input("First: ")
    else:
        print("First:", string1)

    if string2 is None:
        string2 = input("Second: ")
    else:
        print("Second:", string2)

    arr1 = [x.strip('\'\" ') for x in string1.split(',')]
    arr2 = [x.strip('\'\" ') for x in string2.split(',')]
    intersection = [x for x in arr1 if x in arr2]
    if intersection in ([''], []):
        ret = 'false'
    else:
        ret = ', '.join(intersection)
    print("Output:", ret)
    return ret


if __name__ == "__main__":
    find_intersection()

    '''
    # tests
    print('##### TESTS #####')
    print(find_intersection("1, 2, 3", "1, 3, 4") == "1, 3")
    print(find_intersection("1, 3, 4, 7, 13", "1, 2, 4, 13, 15") == "1, 4, 13")
    print(find_intersection("1, 3, 4", "13, 15") == "false")
    print(find_intersection("", "13, 15") == "false")
    print(find_intersection("", "") == "false")
    '''
