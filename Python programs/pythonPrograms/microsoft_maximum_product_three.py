# Microsoft: Find the Maximum Product of Three Numbers
# Given an integer array, find three numbers whose product is maximum and return the maximum product.

def maximum_product(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

if __name__ == "__main__":
    arr1 = [1,2,3]
    print(maximum_product(arr1))  # Output: 6
    arr2 = [1,2,3,4]
    print(maximum_product(arr2))  # Output: 24
    arr3 = [-1,-2,-3]
    print(maximum_product(arr3))  # Output: -6
