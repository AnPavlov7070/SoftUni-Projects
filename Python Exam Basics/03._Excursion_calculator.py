num_people = int(input())
season = input()

price_per_person = 0

if season == "spring":
    if num_people <= 5:
        price_per_person = 50.00
    else:
        price_per_person = 48.00
elif season == "summer":
    if num_people <= 5:
        price_per_person = 48.50
    else:
        price_per_person = 45.00
    price_per_person *= 0.85
elif season == "autumn":
    if num_people <= 5:
        price_per_person = 60.00
    else:
        price_per_person = 49.50
elif season == "winter":
    if num_people <= 5:
        price_per_person = 86.00
    else:
        price_per_person = 85.00
    price_per_person *= 1.08

price_at_total = num_people * price_per_person

print(f"{price_at_total:.2f} leva.")
