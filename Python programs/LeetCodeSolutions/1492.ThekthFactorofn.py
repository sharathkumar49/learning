"""
LeetCode 1492. The kth Factor of n

Given two positive integers n and k, return the kth factor of n. If n has less than k factors, return -1.

Constraints:
- 1 <= k <= n <= 1000

Example:
Input: n = 12, k = 3
Output: 3
"""
def kthFactor(n, k):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            if count == k:
                return i
    return -1

# Example usage:
n = 12
k = 3
print(kthFactor(n, k))  # Output: 3
