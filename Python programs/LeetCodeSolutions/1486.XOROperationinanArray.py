"""
LeetCode 1486. XOR Operation in an Array

Given two integers n and start, return the result of the XOR of all elements nums[i] = start + 2*i for 0 <= i < n.

Constraints:
- 1 <= n <= 1000
- 0 <= start <= 1000

Example:
Input: n = 5, start = 0
Output: 8
"""
def xorOperation(n, start):
    res = 0
    for i in range(n):
        res ^= start + 2 * i
    return res

# Example usage:
n = 5
start = 0
print(xorOperation(n, start))  # Output: 8
