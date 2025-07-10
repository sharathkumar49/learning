"""
LeetCode 1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high, return the count of odd numbers between low and high (inclusive).

Constraints:
- 0 <= low <= high <= 10^9

Example:
Input: low = 3, high = 7
Output: 3
"""
def countOdds(low, high):
    return (high + 1) // 2 - (low // 2)

# Example usage:
low = 3
high = 7
print(countOdds(low, high))  # Output: 3
