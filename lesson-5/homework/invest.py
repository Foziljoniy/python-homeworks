def invest(amount, rate, years):
    """
    Calculates and prints the growth of an investment over time.
    """
    for year in range(1, years + 1):
        amount *= (1 + rate)
        print(f"year {year}: ${amount:.2f}")

# Prompt user for input
initial_amount = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return (as a decimal): "))
num_years = int(input("Enter the number of years: "))

# Call the function to display the investment growth
invest(initial_amount, annual_rate, num_years)