defensive_naylon = 1.50
paint = 14.50
paint_thinner = 5
bags = 0.40

needed_defensive_naylon = int(input())
needed_paint = int(input())
needed_paint_thinner = int(input())
time_needed_for_workers = int(input())

nylon_extra_quantity = 2
paint_extra_quantity = 0.10 * needed_paint

total_material_price = (needed_defensive_naylon + nylon_extra_quantity) * defensive_naylon \
    + (needed_paint + paint_extra_quantity) * paint \
    + needed_paint_thinner * paint_thinner \
    + bags

works_per_hour = total_material_price * 0.30

total_price = total_material_price + works_per_hour * time_needed_for_workers

print(total_price)