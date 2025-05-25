# Adobe: Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

def max_product(nums):
    res = max(nums)
    cur_min, cur_max = 1, 1
    for n in nums:
        if n == 0:
            cur_min, cur_max = 1, 1
            continue
        tmp = cur_max * n
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(tmp, n * cur_min, n)
        res = max(res, cur_max)
    return res

if __name__ == "__main__":
    print(max_product([2,3,-2,4]))  # Output: 6
    print(max_product([-2,0,-1]))   # Output: 0
