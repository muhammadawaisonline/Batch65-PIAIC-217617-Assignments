


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahranheit(celsius):
    return (celsius * 9/5) + 32

choice = input("Type 'F' to convert Fahrenheit to Celsius or 'C' to convert Celsius to Fahrenheit: ").upper()

if choice == 'F':
    fahrenheit = float(input("Enter Temprature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
elif choice == 'C':
    celsius = float(input("Enter Temperature in Celsius: "))
    fahrenheit = celsius_to_fahranheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F ")
else:
    print("Invalid Choice: Please enter 'F' or 'C' ")




""" def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Example usage
choice = input("Type 'F' to convert Fahrenheit to Celsius or 'C' to convert Celsius to Fahrenheit: ").upper()

if choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
elif choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
else:
    print("Invalid choice. Please enter 'F' or 'C'.")
 """