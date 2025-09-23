print(
    """
    Type C to convert temp from Celsius to Fahrenheit
    Type F to convert temp from Fahrenheit to Celsius
    """
)

try:
    conversion_type = input("Input conversion type here: ").strip().lower()
    temp = float(input("Input temp here: "))

    if conversion_type == "c":
        f = (temp * 9 / 5) + 32
        print(f"{temp:.2f}°C = {f:.2f}°F")
    elif conversion_type == "f":
        c = (temp - 32) * 5 / 9
        print(f"{temp:.2f}°C = {c:.2f}°F")
    else:
        print("Please choose from C or F. Try again")

except ValueError:
    print("Temperature must be a number")
