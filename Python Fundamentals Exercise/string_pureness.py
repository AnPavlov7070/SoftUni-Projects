string_number = int(input())

for _ in range(string_number):
    string = input()

    if ',' in string or '.' in string or '_' in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
