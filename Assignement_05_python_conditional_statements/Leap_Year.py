def year():
    year:int = int(input("Enter Year: "))

    if is_leap_year(year):
        print(f" {year} is leap year")
    else:
        print(f" {year} is not leap year")
       


def is_leap_year(year: int):
    if year % 400 == 0:        
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return False
    else:
        return False
    
year()