"""
805. Split Array With Same Average

Given an integer array nums, return true if you can split the array into two non-empty subsets with the same average.

Example 1:
Input: nums = [1,2,3,4,5,6,7,8]
Output: true

Example 2:
Input: nums = [3,1]
Output: false

Constraints:
- 1 <= nums.length <= 30
- 0 <= nums[i] <= 10^4
"""
def splitArraySameAverage(nums):
    n, s = len(nums), sum(nums)
    possible = [set() for _ in range(n//2+1)]
    possible[0].add(0)
    for num in nums:
        for i in range(len(possible)-1, 0, -1):
            for prev in possible[i-1]:
                possible[i].add(prev+num)
    for k in range(1, n//2+1):
        if s*k % n == 0 and (s*k)//n in possible[k]:
            return True
    return False

# Example usage:
print(splitArraySameAverage([1,2,3,4,5,6,7,8]))  # Output: True
print(splitArraySameAverage([3,1]))  # Output: False
