def convert_cel_to_far(celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    # Convert Fahrenheit to Celsius
    try:
        fahrenheit = float(input("Enter a temperature in degrees F: "))
        celsius = convert_far_to_cel(fahrenheit)
        print(f"{fahrenheit} degrees F = {celsius:.2f} degrees C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    
    # Convert Celsius to Fahrenheit
    try:
        celsius = float(input("\nEnter a temperature in degrees C: "))
        fahrenheit = convert_cel_to_far(celsius)
        print(f"{celsius} degrees C = {fahrenheit:.2f} degrees F")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

