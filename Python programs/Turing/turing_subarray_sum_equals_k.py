# Turing: Subarray Sum Equals K
# Given an array of integers and an integer k, return the total number of continuous subarrays whose sum equals to k.
from collections import defaultdict

def subarray_sum(nums, k):
    count = defaultdict(int)
    count[0] = 1
    res = 0
    curr_sum = 0
    for n in nums:
        curr_sum += n
        res += count[curr_sum - k]
        count[curr_sum] += 1
    return res

if __name__ == "__main__":
    print(subarray_sum([1,1,1], 2))  # Output: 2
    print(subarray_sum([1,2,3], 3))  # Output: 2
