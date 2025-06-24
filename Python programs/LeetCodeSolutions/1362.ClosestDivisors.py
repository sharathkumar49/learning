"""
LeetCode 1362. Closest Divisors

Given an integer num, find two integers whose product is num + 1 or num + 2 and whose difference is minimum.

Constraints:
- 1 <= num <= 10^9

Example:
Input: num = 123
Output: [5,25]
"""
def closestDivisors(num):
    import math
    def get(x):
        for i in range(int(math.isqrt(x)), 0, -1):
            if x % i == 0:
                return [i, x//i]
    res1 = get(num+1)
    res2 = get(num+2)
    return res1 if abs(res1[0]-res1[1]) <= abs(res2[0]-res2[1]) else res2

# Example usage:
num = 123
print(closestDivisors(num))  # Output: [5, 25]
