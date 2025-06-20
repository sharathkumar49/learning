"""
644. Maximum Average Subarray II
Difficulty: Hard

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. Return this value. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75

Constraints:
1 <= k <= n <= 10^4
-10^4 <= nums[i] <= 10^4
"""

def findMaxAverage(nums, k):
    def check(mid):
        s = [0]
        for num in nums:
            s.append(s[-1] + num - mid)
        min_pre = 0
        for i in range(k, len(s)):
            if s[i] - min_pre >= 0:
                return True
            min_pre = min(min_pre, s[i-k+1])
        return False
    l, r = min(nums), max(nums)
    while r - l > 1e-5:
        m = (l + r) / 2
        if check(m):
            l = m
        else:
            r = m
    return l

# Example usage
if __name__ == "__main__":
    print(findMaxAverage([1,12,-5,-6,50,3], 4))  # Output: 12.75
