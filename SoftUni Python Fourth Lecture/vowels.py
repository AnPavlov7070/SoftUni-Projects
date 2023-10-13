some_string = input()
points = 0
for character in some_string:
    if character == "a":
        points += 1
    elif character == "e":
        points += 2
    elif character == "i":
        points += 3
    elif character == "o":
        points += 4
    elif character == "u":
        points += 5
print(points)