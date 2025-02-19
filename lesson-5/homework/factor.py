def find_factors(n):
    """Prints all factors of the given positive integer n."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

# Prompt user for input
num = int(input("Enter a positive integer: "))

# Check if input is positive
if num > 0:
    find_factors(num)
else:
    print("Please enter a positive integer.")