sum_needed = float(input())
money_available = float(input())

days_count = 0
spend_count = 0

while money_available < sum_needed and spend_count < 5:
    command = input()
    money = float(input())
    days_count += 1
    if command == "save":
        money_available += money
        spend_count = 0
    elif command == "spend":
        money_available -= money
        spend_count += 1
        if money_available < 0:
            money_available = 0

if spend_count == 5:
    print(f"You can\'t save the money.")
    print(days_count)

if money_available >= sum_needed:
    print(f"You saved the money for {days_count} days.")