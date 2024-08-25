
total_number = float(input("Enter your Tatal Number: "))
part = float(input("Enter part of percentage: "))

def percentage_of_number(total_number, part):
    percentage = (part/total_number)*100
    return percentage
percentage = percentage_of_number(total_number, part)

if total_number != 0:
    print(f"{part} percent of {total_number} is: {percentage:.2f} %")
else:
    print("Total number cannot be zero")

