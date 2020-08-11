def reverse_and_change_vowels(string):
    rev = string[::-1]
    cap = map(change_vowel, rev)
    return ''.join(list(cap))


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
    print(reverse_and_change_vowels('Mabuhay Energy Corporation') == 'n01t4r0pr0C ygr3n3 y4hUb4M')