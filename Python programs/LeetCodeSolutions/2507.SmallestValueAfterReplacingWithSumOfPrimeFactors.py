"""
LeetCode 2507. Smallest Value After Replacing With Sum of Prime Factors

Given n, repeatedly replace n with the sum of its prime factors until it becomes a prime.

Constraints:
- 2 <= n <= 10^5
"""

def smallestValue(n):
    def prime_factors(x):
        s = 0
        d = 2
        while d*d <= x:
            while x%d==0:
                s+=d
                x//=d
            d+=1
        if x>1:
            s+=x
        return s
    while True:
        s = prime_factors(n)
        if s==n:
            return n
        n = s
# Example usage:
# print(smallestValue(15))  # Output: 5
