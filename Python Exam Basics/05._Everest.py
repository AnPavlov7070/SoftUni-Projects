camp = 5364
goal = 8848
maximum_days = 5


current_height = camp
days = 0
reached_goal = False

while True:
    rest = input()
    if rest == "END" or current_height >= goal or days > maximum_days:
        break

    meters_input = input()
    if meters_input == "":
        break

    meters = int(meters_input)

    current_height += meters
    days += 1

    if current_height >= goal:
        reached_goal = True
        break

    if rest == "Yes":
        continue

if reached_goal:
    print(f"Goal reached for", days, "days!")
elif current_height >= goal:
    print("Goal reached for", days, "days!")
else:
    print("Failed!")
    print(current_height)

