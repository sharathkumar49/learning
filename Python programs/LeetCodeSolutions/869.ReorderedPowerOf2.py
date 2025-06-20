"""
869. Reordered Power of 2

Given an integer n, return true if you can reorder the digits of n to get a power of 2.

Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 10
Output: false

Constraints:
- 1 <= n <= 10^9
"""
def reorderedPowerOf2(n):
    from collections import Counter
    c = Counter(str(n))
    for i in range(31):
        if c == Counter(str(1 << i)):
            return True
    return False

# Example usage:
print(reorderedPowerOf2(1))   # Output: True
print(reorderedPowerOf2(10))  # Output: False
