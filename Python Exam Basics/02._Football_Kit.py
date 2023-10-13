tshirt_price = float(input())
sum_needed_for_the_ball = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (tshirt_price + shorts_price) * 2

overall_sum = tshirt_price + shorts_price + socks_price + shoes_price
sum_after_discount = overall_sum - (overall_sum * 0.15)

if sum_after_discount >= sum_needed_for_the_ball:
   print("Yes, he will earn the world-cup replica ball!")
   print(f"His sum is {sum_after_discount:.2f} lv.")
else:
    needed_amount = sum_needed_for_the_ball - sum_after_discount
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_amount:.2f} lv. more.")


