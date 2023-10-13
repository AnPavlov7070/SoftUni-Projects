n = int(input())

for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num

    while digits > 0:
        sum_of_digits += digits % 10
        digits //= 10

    if sum_of_digits in ['5', '7', '11']:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')