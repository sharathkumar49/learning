"""
LeetCode 1551. Minimum Operations to Make Array Equal

Given an integer n, return the minimum number of operations to make all elements of arr equal, where arr = [1, 3, 5, ..., 2n - 1]. In one operation, you can choose two indices and increment one and decrement the other by 1.

Constraints:
- 1 <= n <= 10^4

Example:
Input: n = 3
Output: 2
"""
def minOperations(n):
    return (n*n)//4

# Example usage:
n = 3
print(minOperations(n))  # Output: 2
