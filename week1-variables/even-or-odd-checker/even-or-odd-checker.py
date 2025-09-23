try:
    number = int(input("Give me a number to check if its even or odd: "))

    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is Odd")
except ValueError:
    print("Please give me a number. Try again")
