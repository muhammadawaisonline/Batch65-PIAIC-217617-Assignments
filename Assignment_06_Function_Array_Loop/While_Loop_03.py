def factorial(n):
   
    result = 1
    
    
    while n > 0:
        result *= n  
        n -= 1  
    
    return result


number = 5
print(f"The factorial of {number} is {factorial(number)}")
