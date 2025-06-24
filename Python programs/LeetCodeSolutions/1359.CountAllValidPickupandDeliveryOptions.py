"""
LeetCode 1359. Count All Valid Pickup and Delivery Options

Given n orders, return the number of valid pickup and delivery sequences modulo 10^9+7.

Constraints:
- 1 <= n <= 500

Example:
Input: n = 3
Output: 90
"""
def countOrders(n):
    MOD = 10**9+7
    res = 1
    for i in range(1, n+1):
        res = res * i * (2*i-1) % MOD
    return res

# Example usage:
n = 3
print(countOrders(n))  # Output: 90
