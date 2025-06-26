# Microsoft: Find the Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray of which the sum ≥ target. If no such subarray, return 0.

def min_sub_array_len(target, nums):
    left = 0
    total = 0
    res = float('inf')
    for right, n in enumerate(nums):
        total += n
        while total >= target:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if res == float('inf') else res

if __name__ == "__main__":
    print(min_sub_array_len(7, [2,3,1,2,4,3]))  # Output: 2
    print(min_sub_array_len(4, [1,4,4]))        # Output: 1
    print(min_sub_array_len(11, [1,1,1,1,1,1,1,1]))  # Output: 0
