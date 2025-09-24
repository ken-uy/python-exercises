import time

for i in range(10, 0, -1):
    print(f"{i}")
    time.sleep(1)

# while loop
x: int = 1
while x <= 10:
    if x < 10:
        print(x, end=",")
    else:
        print(x)
    x += 1

# argument unpacking
print(*range(1, 11), sep=",")


