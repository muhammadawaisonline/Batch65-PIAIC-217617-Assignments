def month_number():
    month:int = int(input("Enter Month Number from 1 to 12: "))

    days_in_month(month)

def days_in_month(month:int):
    match month:
        case 1:
            print(f" {month} is January and days in the month of 2024 are  '31' ")
        case 2:
            print(f" {month} is February and days in the month of 2024 are '29'  (As 2024 is leap Year, otherwise days in February are '28')")
        case 3:
            print(f" {month} is March and days in the month of 2024 are '31'  ")
        case 4:
            print(f" {month} is April and days in the month of 2024 are  '30' ")
        case 5:
            print(f" {month} is May and days in the month of 2024 are  '31' ")
        case 6:
            print(f" {month} is June and days in the month of 2024 are  '30' ")
        case 7:
            print(f" {month} is July and days in the month of 2024 are  '31' ")
        case 8:
            print(f" {month} is August and days in the month of 2024 are  '31' ")
        case 9:
            print(f" {month} is September and days in the month of 2024 are  '30' ")
        case 10:
            print(f" {month} is October and days in the month of 2024 are  '31' ")
        case 11:
            print(f" {month} is November and days in the month of 2024 are  '30' ")
        case _:
            print(f" {month} is December and days in the month of 2024 are  '31' ")

month_number()