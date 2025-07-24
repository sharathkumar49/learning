"""
LeetCode 2521. Distinct Prime Factors of Product of Array

Given an array, return the number of distinct prime factors of the product.

Constraints:
- 1 <= nums.length <= 10^5
"""

def distinctPrimeFactors(nums):
    from math import isqrt
    s = set()
    for x in nums:
        d = 2
        while d*d <= x:
            while x%d==0:
                s.add(d)
                x//=d
            d+=1
        if x>1:
            s.add(x)
    return len(s)
# Example usage:
# print(distinctPrimeFactors([2,4,3,7,10,6]))  # Output: 4
