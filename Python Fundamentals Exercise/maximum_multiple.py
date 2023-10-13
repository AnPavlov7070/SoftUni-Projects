divisor = int(input())
boundary = int(input())

n = boundary - (boundary % divisor)

if n == 0:
    print("No such number exists.")
else:
    print(n)