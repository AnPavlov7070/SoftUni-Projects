# Декорът за филма е на стойност 10% от бюджета.

# При повече от 150 статиста, има отстъпка за облеклото на стойност 10%

movie_budget = float(input())
statists = int(input())
clothes_one_statist = float(input())

decor = movie_budget * 0.10

if statists > 150:
    clothes_one_statist *= 0.90
else:
    clothes_one_statist *= 1.00

money_needed = decor + statists * clothes_one_statist

Message_for_budget_not_enough = f"Action!\nWingard starts filming with {movie_budget - money_needed :.2f} leva left."
Message_for_budget_enough = f"Not enough money!\nWingard needs {money_needed - movie_budget :.2f} leva more."

if money_needed < movie_budget:
    print(Message_for_budget_not_enough)
else:
    print(Message_for_budget_enough)