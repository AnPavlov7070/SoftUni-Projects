start_interval = int(input())
end_interval = int(input())
magical_number = int(input())
combination_found = False
counter_combination = 0
for first_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        counter_combination += 1
        if first_number + second_number == magical_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{counter_combination} ({first_number} + {second_number} = {magical_number})")
else:
    print(f"{counter_combination} combinations - neither equals {magical_number}")

