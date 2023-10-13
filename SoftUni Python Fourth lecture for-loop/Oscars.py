actor = input()
points_to_start = float(input())
judges_count = int(input())


points_at_total = points_to_start
for i in range(judges_count):
    name_judge = input()
    judge_points = float(input())
    points_at_total += len(name_judge) * judge_points / 2
    if points_at_total > 1250.5:
        break

if points_at_total > 1250:
    print(f"Congratulations, {actor} got a nominee for leading role with {points_at_total :.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5 - points_at_total :.1f} more!")


