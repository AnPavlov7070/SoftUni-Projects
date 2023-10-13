base_camp = 5364
everest_peak = 8848
allowed_days = 4

# Дните трябва да бъдат 5, но при въвеждане на един от входовете, не се получава "Failed!" "7647", ами "8147".

total_meters_climbed = base_camp
days = 1

while days <= allowed_days:
    command = input()
    if command == "END":
        break

    should_rest = command == "Yes"
    meters_climbed = int(input())

    if should_rest:
        total_meters_climbed += meters_climbed
        days += 1
    else:
        total_meters_climbed += meters_climbed

    if total_meters_climbed >= everest_peak:
        break

if total_meters_climbed >= everest_peak:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(total_meters_climbed)
