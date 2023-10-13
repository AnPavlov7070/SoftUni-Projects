sum_for_square_meter = 7.61
discount = 0.18
yard_greening = float(input()) * sum_for_square_meter
calculating_discount = discount * yard_greening
ending_sum = yard_greening - calculating_discount
print(f'The final price is: {ending_sum} lv.')
print(f'The discount is: {calculating_discount} lv.')
