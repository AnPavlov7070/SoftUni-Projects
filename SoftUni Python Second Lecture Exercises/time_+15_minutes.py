
hours = int(input())
minutes = int(input())

extra_minute = (minutes + 15) % 60
extra_hour = (hours + (minutes + 15) // 60) % 24

print("{:2d}:{:02d}".format(extra_hour, extra_minute))

# This code reads in the hour and minute from the user using the input() function, calculates the new time by adding 15 minutes to the current time, and prints the result in the required format using the print() function and the {:02d} format specifier for the hour and minute values.
#
# Note that this code assumes that the user enters the hour and minute values on separate lines, and that the input values are valid integers between 0 and 23 for the hour, and 0 and 59 for the minute. If the input values are invalid, the program may produce unexpected results or raise an error.