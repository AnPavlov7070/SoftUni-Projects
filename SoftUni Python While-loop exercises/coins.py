change = float(input())
coin_1_cent = 0.01
coin_2_cents = 0.02
coin_5_cents = 0.05
coin_10_cents = 0.10
coin_20_cents = 0.20
coin_50_cents = 0.50
coin_1_lev = 1
coin_2_lev = 2
total_coins_used = 0
while change != 0:
    if coin_2_lev <= change:
        change -= coin_2_lev
    elif coin_1_lev <= change:
        change -= coin_1_lev
    elif coin_50_cents <= change:
        change -= coin_50_cents
    elif coin_20_cents <= change:
        change -= coin_20_cents
    elif coin_10_cents <= change:
        change -= coin_10_cents
    elif coin_5_cents <= change:
        change -= coin_5_cents
    elif coin_2_cents <= change:
        change -= coin_2_cents
    elif coin_1_cent <= change:
        change -= coin_1_cent
    total_coins_used += 1
    change = round(change, 2)
print(total_coins_used)

