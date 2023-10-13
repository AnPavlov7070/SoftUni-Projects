processor_price = float(input())
graphics_card = float(input())
RAM_memory = float(input())
RAM_memory_count = int(input())
discount = float(input())

processor_in_lev = processor_price * 1.57
graphics_card_in_lev = graphics_card * 1.57
RAM_in_lev = RAM_memory * 1.57
ram_overall = RAM_in_lev * RAM_memory_count
processor_price_overall = processor_in_lev - (processor_in_lev * discount)
graphics_card_overall = graphics_card_in_lev - (graphics_card_in_lev * discount)

overall_price = processor_price_overall + graphics_card_overall + ram_overall
print(f"Money needed - {overall_price :.2f} leva.")


