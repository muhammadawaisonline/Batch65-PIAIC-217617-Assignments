array = [1, 2, 3, 4, 5]
index = 2
value = 99
def insert_value(arr, index, value):
   
    arr.insert(index, value)
    return arr
modified_array = insert_value(array, index, value)
print("Modified array:", modified_array)
