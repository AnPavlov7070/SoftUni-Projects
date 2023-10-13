def count_binary_digits(number, binary_digit):
    binary_representation = bin(number)[2:]  # Convert to binary and remove the '0b' prefix
    return binary_representation.count(str(binary_digit))


while True:
    try:
        # Read user input inside the loop
        n = int(input("Enter a positive integer (or 0 to exit): "))

        # Exit the loop if the user enters 0
        if n == 0:
            break

        b = int(input("Enter a binary digit (0 or 1): "))

        if b not in (0, 1):
            raise ValueError("Binary digit must be 0 or 1.")

        # Calculate and display the count of the binary digit
        count_b = count_binary_digits(n, b)
        print(f"The number of binary digit {b} in the binary representation of {n} is: {count_b}")

    except ValueError as e:
        print("Invalid input. Please enter a valid positive integer and a binary digit (0 or 1).")

print("Exiting the program.")
