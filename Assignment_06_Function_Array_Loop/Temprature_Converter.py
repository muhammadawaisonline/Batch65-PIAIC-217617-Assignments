
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def convert_temperatures(celsius_list):
    fahrenheit_list = []
    i = 0
    while i < len(celsius_list):
        fahrenheit = celsius_to_fahrenheit(celsius_list[i])
        fahrenheit_list.append(fahrenheit)
        i += 1
    return fahrenheit_list


celsius_list = list(map(float, input("Enter a list of Celsius temperatures separated by spaces: ").split()))


fahrenheit_list = convert_temperatures(celsius_list)


print("Temperatures in Fahrenheit:", fahrenheit_list)
