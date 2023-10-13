deposited_sum = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100
interest = deposited_sum * annual_interest_rate
interest_for_one_month = interest / 12
the_whole_sum = deposited_sum + deposit_term * interest_for_one_month
print(the_whole_sum)