"""
LeetCode 1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 5
Output: [-7,-1,1,3,4]
"""
def sumZero(n):
    res = [i for i in range(1, n//2+1)] + [-i for i in range(1, n//2+1)]
    if n % 2:
        res.append(0)
    return res

# Example usage:
n = 5
print(sumZero(n))  # Output: [-2,-1,0,1,2] (any valid answer)
