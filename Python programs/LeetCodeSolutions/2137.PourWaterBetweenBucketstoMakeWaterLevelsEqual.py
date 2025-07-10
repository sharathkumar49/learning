"""
LeetCode 2137. Pour Water Between Buckets to Make Water Levels Equal

Given an array buckets, return the minimum number of operations to make all buckets have the same water level.

Example:
Input: buckets = [1,2,3]
Output: 2

Constraints:
- 1 <= buckets.length <= 10^5
- 1 <= buckets[i] <= 10^5
"""

def minOperations(buckets):
    target = sum(buckets) // len(buckets)
    return sum(abs(x - target) for x in buckets) // 2

# Example usage:
# print(minOperations([1,2,3]))  # Output: 2
