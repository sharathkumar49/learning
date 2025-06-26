# Facebook: Find the Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

def max_product(nums):
    if not nums:
        return 0
    max_prod = min_prod = result = nums[0]
    for n in nums[1:]:
        if n < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(n, max_prod * n)
        min_prod = min(n, min_prod * n)
        result = max(result, max_prod)
    return result

if __name__ == "__main__":
    arr1 = [2,3,-2,4]
    print(max_product(arr1))  # Output: 6
    arr2 = [-2,0,-1]
    print(max_product(arr2))  # Output: 0
    arr3 = [-2,3,-4]
    print(max_product(arr3))  # Output: 24
