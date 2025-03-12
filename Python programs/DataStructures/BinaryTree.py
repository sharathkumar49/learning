import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper



@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        print("mid_index: ", mid_index)
        mid_number = numbers_list[mid_index]
        print("mid_number: ", mid_number)
        if mid_number == number_to_find:
            print("mid_number is equal to number_to_find")
            print(mid_number)
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
            print("here in the list mid_number < number_to_find")
            print("left_index: ", left_index)
        else:
            right_index = mid_index - 1
            print("here in the else part")
            print("right_index: ", right_index)

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 21
    # numbers_list = range(9999999)
    # number_to_find = 9999997
    numbers_list = [1,4,6,9,10,5,7]
    number_to_find = 5
    # index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    # index = linear_search(numbers_list, number_to_find)
    # print(f"Number found at index {index} using binary search")
    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")