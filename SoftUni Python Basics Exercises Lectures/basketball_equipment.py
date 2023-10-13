# Баскетболни кецове – цената им е 40% по-малка от таксата за една година

# Баскетболен екип – цената му е 20% по-евтина от тази на кецовете

# Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип

# Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

price_training_for_year = int(input())

basketball_shoes = price_training_for_year * 0.60
basketball_kit = basketball_shoes * 0.80
basketball_ball = basketball_kit / 4
basketball_accessories = basketball_ball / 5
total_price = price_training_for_year + basketball_shoes + basketball_kit + basketball_ball + basketball_accessories
print(total_price)