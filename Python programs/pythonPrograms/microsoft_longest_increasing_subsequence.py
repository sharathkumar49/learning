# Microsoft: Longest Increasing Subsequence (DP)
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == "__main__":
    arr1 = [10,9,2,5,3,7,101,18]
    print(length_of_lis(arr1))  # Output: 4
    arr2 = [0,1,0,3,2,3]
    print(length_of_lis(arr2))  # Output: 4
    arr3 = [7,7,7,7,7,7,7]
    print(length_of_lis(arr3))  # Output: 1
