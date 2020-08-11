def reverse_and_capitalize_vowels(string=''):
    if string == '':
        string = input("Input: ")
    else:
        print("Input:", string)

    rev = string[::-1]
    cap = map(capitalize_if_vowel, rev)
    ret = ''.join(list(cap))
    print("Output:", ret)
    return ret


def capitalize_if_vowel(char):
    if char in 'aeiou':
        return char.upper()
    else:
        return char


if __name__ == "__main__":
    reverse_and_capitalize_vowels()

    '''
    # tests
    print('##### TESTS #####')
    print(reverse_and_capitalize_vowels('Python Exam') == 'mAxE nOhtyP')
    print(reverse_and_capitalize_vowels('Hello World') == 'dlrOW OllEH')
    '''
