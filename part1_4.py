def swap_variables():
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    num2, num1 = num1, num2
    print("First variable:", num1)
    print("Second variable:", num2)


if __name__ == "__main__":
    swap_variables()
