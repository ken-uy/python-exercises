try:
    age = int(input("Give me your age: "))

    if age < 18:
        print("You are a minor")
    elif age >= 60:
        print("You are a senior citizen")
    else:
        print(f"You are {age} years old")
except ValueError:
    print("Please input a number. Try again")
