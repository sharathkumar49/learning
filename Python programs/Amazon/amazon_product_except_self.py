# Amazon: Product of Array Except Self
# Given an array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve without division and in O(n) time.

def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

if __name__ == "__main__":
    arr1 = [1,2,3,4]
    print(product_except_self(arr1))  # Output: [24,12,8,6]
    arr2 = [0,0]
    print(product_except_self(arr2))  # Output: [0,0]
    arr3 = [1,2,0,4]
    print(product_except_self(arr3))  # Output: [0,0,8,0]
