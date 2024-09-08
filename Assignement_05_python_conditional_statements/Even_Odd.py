n: int = int(input("Enter Your Number: "))

def get_number(n: int):
    
    if n == 0:
        print(f"Your Number is {n}")
    elif n > 0:
        print(f" {n} is Positive")
    elif n < 0:
        print(f"{n} is negative")

    if n != 0: 
        if  n % 2 == 0:
            print(f" {n} is devisible by 2 and ", end='')
            print(f" {n} is Even")
        elif  n % 3 == 0 or n % 3 == -0:
            print(f" {n} is divisible by 3 and ", end='')
            print(f" {n} is Odd")
        elif n % 2 != 0 or n % 3 != 0:
            print(f" {n} is not divisible by 2 and 3.")

    
         

get_number(n)