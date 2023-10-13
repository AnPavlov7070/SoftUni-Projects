destination = input()
while destination != "End":
    needed_money = float(input())
    current_money = 0
    while current_money < needed_money:
        money_saved = float(input())
        current_money += money_saved
    print(f"Going to {destination}!")
    destination = input()

