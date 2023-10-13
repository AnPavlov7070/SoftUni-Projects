lenght = int(input())
width = int(input())
height = int(input())
percent_non_empty_tank = float(input())

total = lenght * width * height
total_liters = total / 1000

water_needed = total_liters * (100 - percent_non_empty_tank) / 100

print(water_needed)

