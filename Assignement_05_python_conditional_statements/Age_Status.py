def person_info():
    name: str = input("What's Your name?  ")
    age:int = int(input("What's your age?  "))
    age_status(name, age)


def age_status(name:str, age: int):
    if age in range(0,12):
        print(f" {name}: You are a child as your age is {age}: under 18")
    elif age in range(13,19):
        print(f" {name}: you are teenager as you are {age} years old")
    elif age in range(19, 59):
        print(f"{name}: You are adult as you are {age} years old")
    else:
        print(f"{name}: You are seniors citizen as you are {age} years old") 
person_info()