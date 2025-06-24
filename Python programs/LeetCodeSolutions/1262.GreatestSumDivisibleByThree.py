"""
1262. Greatest Sum Divisible by Three

Given an array nums, return the maximum sum of elements divisible by three.

Constraints:
- 1 <= nums.length <= 4 * 10^4
- 1 <= nums[i] <= 10^4

Example:
Input: nums = [3,6,5,1,8]
Output: 18

"""
def maxSumDivThree(nums):
    dp = [0, float('-inf'), float('-inf')]
    for num in nums:
        for i in dp[:]:
            dp[(i+num)%3] = max(dp[(i+num)%3], i+num)
    return dp[0]

# Example usage
if __name__ == "__main__":
    print(maxSumDivThree([3,6,5,1,8]))  # Output: 18
