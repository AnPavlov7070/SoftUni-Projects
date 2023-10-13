sum_at_total = 0
command = input()
while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid cooperation!")
        break
    print(f"Increase: {current_sum:.2f}")
    sum_at_total += current_sum
    command = input()
print(f"Total: {sum_at_total:.2f}")
