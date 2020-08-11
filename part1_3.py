def reverse_and_change_vowels(string=''):
    if string == '':
        string = input("Input: ")
    else:
        print("Input:", string)

    rev = string[::-1]
    cap = map(change_vowel, rev)
    ret = ''.join(list(cap))
    print("Output:", ret)
    return ret


def change_vowel(char):
    if char in 'aA':
        return '4'
    elif char in 'eE':
        return '3'
    elif char in 'iI':
        return '1'
    elif char in 'oO':
        return '0'
    elif char in 'uU':
        return 'U'
    else:
        return char


if __name__ == "__main__":
    reverse_and_change_vowels()

    '''
    # tests
    print('##### TESTS #####')
    print(reverse_and_change_vowels('Mabuhay Energy Corporation') == 'n01t4r0pr0C ygr3n3 y4hUb4M')
    '''
