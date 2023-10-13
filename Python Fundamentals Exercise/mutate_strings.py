first_string = input()
second_string = input()

previous_string = first_string
print(previous_string)

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        first_string = first_string[:i] + second_string[i] + first_string[i+1:]
        if first_string != previous_string:
            print(first_string)
        previous_string = first_string
