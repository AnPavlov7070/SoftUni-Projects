# define function to add two numbers
def add (x, y):
    return x + y
# define function to subtract two numbers
def subtract (x, y):
    return x - y
# define function to multiply two numbers
def multiply (x, y):
    return x * y
# define function to divide two numbers
def divide (x, y):
    return x / y

# Print Menu
print ("Select Operation")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

# User's choices
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations based on user's choice

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")