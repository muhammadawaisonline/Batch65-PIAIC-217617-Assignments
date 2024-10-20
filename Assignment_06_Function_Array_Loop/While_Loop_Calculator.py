
def remove_negatives(arr):
   
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            arr.pop(i)  
        else:
            i += 1  
    return arr


numbers = [12, -7, 5, -3, 9, -1, 14]
print("Original array:", numbers)


modified_array = remove_negatives(numbers)
print("Array after removing negatives:", modified_array)
