chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

total_chicken_menus = chicken_menus * chicken_menu
total_fish_menus = fish_menus * fish_menu
total_vegetarian_menus = vegetarian_menus * vegetarian_menu

total_menus_price = total_chicken_menus + total_fish_menus + total_vegetarian_menus
dessert_price = 0.20 * total_menus_price

delivery_price = 2.50

total_order_price = total_menus_price + dessert_price + delivery_price
print(total_order_price)