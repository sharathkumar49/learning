"""
643. Maximum Average Subarray I
Difficulty: Easy

Given an array consisting of n integers, find the contiguous subarray of length k that has the maximum average value. Return this value.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75

Constraints:
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
"""

def findMaxAverage(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k

# Example usage
if __name__ == "__main__":
    print(findMaxAverage([1,12,-5,-6,50,3], 4))  # Output: 12.75
