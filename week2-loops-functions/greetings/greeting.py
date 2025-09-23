# def greet(name) -> str:
#     return f"Hello, {name}!"


# print(greet("Gee"))


def is_even(number: int) -> bool:
    """Return True when number is even, False if odd"""
    return number % 2 == 0


while True:
    print("\n1. Check number \n2. Quit")
    try:
        choice: str = input("1 or 2: ").strip()

        if choice == "1":
            n: int = int(input("Input number: "))
            print("Even!" if is_even(n) else "Odd!")
        elif choice == "2":
            break
        else:
            print(f"Invalid choice: Try again!")
    except ValueError:
        print(f"Invalid input: Enter an integer")
