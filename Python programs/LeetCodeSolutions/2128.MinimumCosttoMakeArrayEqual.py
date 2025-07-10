"""
LeetCode 2128. Minimum Cost to Make Array Equal

Given an array nums and an integer cost, return the minimum cost to make all elements equal.

Example:
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], cost[i] <= 10^6
"""

def minCost(nums, cost):
    arr = sorted(zip(nums, cost))
    n = len(nums)
    total = sum(cost)
    acc = 0
    for num, c in arr:
        acc += c
        if acc >= (total+1)//2:
            target = num
            break
    return sum(abs(num-target)*c for num, c in arr)

# Example usage:
# print(minCost([1,3,5,2], [2,3,1,14]))  # Output: 8
