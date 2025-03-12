
# Method 1:
def remove_duplicates(arr):
    unique_list = []
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

integer_array = [1, 2, 3, 4, 2, 3, 5, 6, 6]
unique_array = remove_duplicates(integer_array)
print(unique_array)



# Method 2:
def removeDuplicates(int_array):
    # arr = [i for i in int_array if i not in int_array[]]
    arr = [ele for i, ele in enumerate(int_array) if ele not in int_array[:i]]
    return arr


integer_array = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 7, 7, 8, 9, 9,]
unique_array = removeDuplicates(integer_array)
print(unique_array)




