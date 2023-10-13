number = input()
sorted_digits = sorted(number, reverse=True)
largest_number = ''.join(sorted_digits)
print(largest_number)
