from datetime import datetime


birth_year = int(input("Enter Your Birth Year: "))

def age_calculator(birth_year):
    current_year = datetime.now().year 
    age = current_year - birth_year
    return age

age = age_calculator(birth_year)

print(f"You'r age is {age} years")