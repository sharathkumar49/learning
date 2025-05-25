# Microsoft: Find the Shortest Unsorted Continuous Subarray
# Given an integer array, find the shortest subarray which, if sorted, results in the whole array being sorted.

def find_unsorted_subarray(nums):
    n = len(nums)
    start, end = -1, -2
    min_num, max_num = nums[-1], nums[0]
    for i in range(1, n):
        max_num = max(max_num, nums[i])
        if nums[i] < max_num:
            end = i
    for i in range(n-2, -1, -1):
        min_num = min(min_num, nums[i])
        if nums[i] > min_num:
            start = i
    return end - start + 1

if __name__ == "__main__":
    arr1 = [2,6,4,8,10,9,15]
    print(find_unsorted_subarray(arr1))  # Output: 5
    arr2 = [1,2,3,4]
    print(find_unsorted_subarray(arr2))  # Output: 0
