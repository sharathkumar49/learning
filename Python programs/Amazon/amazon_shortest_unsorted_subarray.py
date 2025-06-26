# Amazon: Find the Shortest Unsorted Continuous Subarray
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, the whole array will be sorted.
# Return the length of shortest such subarray.

def find_unsorted_subarray(nums):
    n = len(nums)
    start, end = -1, -2
    min_num, max_num = nums[-1], nums[0]
    for i in range(1, n):
        max_num = max(max_num, nums[i])
        min_num = min(min_num, nums[n-i-1])
        if nums[i] < max_num:
            end = i
        if nums[n-i-1] > min_num:
            start = n-i-1
    return end - start + 1

if __name__ == "__main__":
    print(find_unsorted_subarray([2,6,4,8,10,9,15]))  # Output: 5
    print(find_unsorted_subarray([1,2,3,4]))  # Output: 0
