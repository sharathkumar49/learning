"""
LeetCode 2238. Number of Times Number Is Replaced

Given n, return the number of times n is replaced by the sum of its digits until n becomes a single digit.

Example:
Input: n = 38
Output: 2

Constraints:
- 1 <= n <= 10^9
"""

def countReplacements(n):
    count = 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
        count += 1
    return count

# Example usage:
# print(countReplacements(38))  # Output: 2
