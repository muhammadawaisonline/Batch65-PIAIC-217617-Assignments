
def remove_odds(arr):
    
    i = 0
    while i < len(arr):
        if arr[i] % 2 != 0:  
            arr.pop(i)  
        else:
            i += 1  
    return arr


numbers = [12, 7, 5, 16, 9, 2, 14]
print("Original array:", numbers)


modified_array = remove_odds(numbers)
print("Array after removing odds:", modified_array)
