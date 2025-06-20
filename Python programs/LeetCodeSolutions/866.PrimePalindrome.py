"""
866. Prime Palindrome

Find the smallest prime palindrome greater than or equal to n.

Example 1:
Input: n = 6
Output: 7

Example 2:
Input: n = 13
Output: 101

Constraints:
- 1 <= n <= 10^8
"""
def primePalindrome(n):
    def is_prime(x):
        if x < 2: return False
        if x == 2: return True
        if x % 2 == 0: return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True
    for l in range(1, 6):
        for root in range(10 ** (l - 1), 10 ** l):
            s = str(root)
            x = int(s + s[-2::-1])
            if x >= n and is_prime(x):
                return x
    for x in range(10 ** 6, 10 ** 7):
        if str(x) == str(x)[::-1] and is_prime(x) and x >= n:
            return x
    return -1

# Example usage:
print(primePalindrome(6))   # Output: 7
print(primePalindrome(13))  # Output: 101
