def print_triangle():
    height = int(input("Input a Number: "))
    n = 1
    stars = ''
    preceding_letters = ''
    counting_letter = ord('A') - 1
    while n <= height:
        stars += '* '
        if counting_letter < ord('Z'):
            counting_letter += 1
        else:
            counting_letter = ord('A')
            preceding_letters += chr(ord('A') + len(preceding_letters))

        print(stars, preceding_letters + chr(counting_letter))
        n += 1


if __name__ == "__main__":
    print_triangle()
