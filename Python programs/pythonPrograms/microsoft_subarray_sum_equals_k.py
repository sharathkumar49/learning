# Microsoft: Subarray Sum Equals K
# Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k.
from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix = defaultdict(int)
    prefix[0] = 1
    for n in nums:
        curr_sum += n
        count += prefix[curr_sum - k]
        prefix[curr_sum] += 1
    return count

if __name__ == "__main__":
    arr1 = [1,1,1]
    print(subarray_sum(arr1, 2))  # Output: 2
    arr2 = [1,2,3]
    print(subarray_sum(arr2, 3))  # Output: 2
