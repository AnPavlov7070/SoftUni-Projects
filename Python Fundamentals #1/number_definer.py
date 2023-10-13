number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if abs(number) < 1: #абсолютна стойност
         print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("negative")

else:
    if abs(number) < 1: #абсолютна стойност
         print("small negative")
    elif number > 1000000:
        print("large negative")
    else:
        print("negative")

