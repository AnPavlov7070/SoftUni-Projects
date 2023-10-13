# define
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
price_for_delivery = 2.50

# input
count_chicken_menu = int(input()) * chicken_menu
count_fish_menu = int(input()) * fish_menu
count_vegetarian_menu = int(input()) * vegetarian_menu

menu_final_price = count_chicken_menu + count_fish_menu + count_vegetarian_menu
dessert_price = menu_final_price * 0.20
whole_cost = menu_final_price + dessert_price + price_for_delivery
print(whole_cost)
