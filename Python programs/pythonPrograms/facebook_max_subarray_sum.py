# Facebook: Find the Maximum Subarray Sum (Kadane's Algorithm)
# Given an integer array nums, find the contiguous subarray with the largest sum.

def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    arr1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray(arr1))  # Output: 6
    arr2 = [1]
    print(max_subarray(arr2))  # Output: 1
    arr3 = [5,4,-1,7,8]
    print(max_subarray(arr3))  # Output: 23
