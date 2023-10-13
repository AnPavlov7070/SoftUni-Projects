import math

w_points = 2000
f_points = 1200
sf_points = 720

count_tournaments = int(input())
starting_points = int(input())

total_wins = 0
points_gained = 0

for _ in range(count_tournaments):
    tournament_result = input()
    if tournament_result == "W":
        points_gained += w_points
        total_wins += 1
    elif tournament_result == "L":
        points_gained += f_points
    elif tournament_result == "SF":
        points_gained += sf_points

total_points = starting_points + points_gained
average_points = math.floor(points_gained / count_tournaments)
percent_wins = total_wins / count_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins :.2f}%")

