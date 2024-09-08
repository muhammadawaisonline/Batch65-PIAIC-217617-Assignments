def get_citizen_data():
    name: str = input("What's Your Name: ")
    age: int = int(input("What's Your Age: "))
    nationality:str = input("What's Your Nationality: ").lower()
    eligible_for_vote(name, age, nationality)

def eligible_for_vote(name:str, age:int, nationality:str):
    
    
    if age < 18:
        print(f" {name}: You are not eligible to vote because you are under 18")
        return False
    elif nationality != "pakistani":
        print(f" {name}: Please obtain valid ID to Vote")
    else:
        print(f" {name}: You are eligible to vote")
get_citizen_data()