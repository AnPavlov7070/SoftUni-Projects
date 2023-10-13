year = int(input("Enter a year: "))

while True:
    year += 1
    if len(set(str(year))) == 4:  # Check if all digits are distinct for a 4-digit year
        print(f"The next happy year is {year}.")
        break