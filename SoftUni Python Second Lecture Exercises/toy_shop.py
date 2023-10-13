puzzle = 2.60
speaking_doll = 3
bear = 4.10
minion = 8.20
truck = 2

total_cost = puzzle + speaking_doll + bear + minion + truck

travel_cost = float(input())
puzzles = int(input())
speaking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum = (puzzles * puzzle) + (speaking_dolls * speaking_doll) + (bears * bear) + (minions * minion) + (trucks * truck)
toys_overall = puzzles + speaking_dolls + bears + minions + trucks


discount = 0
if toys_overall >= 50:

    discount = 0.25
    ending_sum = sum - discount
    rent = ending_sum * 0.10
    win = ending_sum - rent
    result = win - travel_cost
    print(f'Yes! {result :.2f} lv left.')


else:
    rent = 0.10 * sum
    win = sum - rent
    result = travel_cost - win
    print(f'Not enough money! {result :.2f} lv needed.')


