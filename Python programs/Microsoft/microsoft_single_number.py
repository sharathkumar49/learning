# Microsoft: Find the Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

if __name__ == "__main__":
    arr1 = [2,2,1]
    print(single_number(arr1))  # Output: 1
    arr2 = [4,1,2,1,2]
    print(single_number(arr2))  # Output: 4
    arr3 = [1]
    print(single_number(arr3))  # Output: 1
