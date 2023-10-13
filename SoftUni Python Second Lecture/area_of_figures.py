import math

figure = input()

if figure == 'square':
    side = float(input())
    area = side ** 2
    print(area)
elif figure == 'rectangle':
    length = float(input())
    width = float(input())
    area = length * width
    print(area)
elif figure == 'circle':
    radius = float(input())
    area = math.pi * radius ** 2
    print(area)
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = 0.5 * side * height
    print(area)
else:
    print("Invalid figure")


