def reverse_and_capitalize_vowels(string):
    rev = string[::-1]
    cap = map(capitalize_if_vowel, rev)
    return ''.join(list(cap))


def capitalize_if_vowel(char):
    if char in 'aeiou':
        return char.upper()
    else:
        return char


if __name__ == "__main__":
    print(reverse_and_capitalize_vowels('Python Exam') == 'mAxE nOhtyP')
    print(reverse_and_capitalize_vowels('Hello World') == 'dlrOW OllEH')