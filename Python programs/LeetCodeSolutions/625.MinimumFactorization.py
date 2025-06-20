"""
625. Minimum Factorization
Difficulty: Medium

Given a positive integer num, return the smallest positive integer whose multiplication of each digit equals num. If there is no answer or the answer is greater than 2^31 - 1, return 0.

Example 1:
Input: num = 48
Output: 68

Example 2:
Input: num = 15
Output: 35

Constraints:
1 <= num <= 2^31 - 1
"""

def smallestFactorization(num):
    if num < 10:
        return num
    res = []
    for d in range(9, 1, -1):
        while num % d == 0:
            res.append(str(d))
            num //= d
    if num != 1:
        return 0
    ans = int(''.join(res[::-1]))
    return ans if ans < 2**31 else 0

# Example usage
if __name__ == "__main__":
    print(smallestFactorization(48))  # Output: 68
    print(smallestFactorization(15))  # Output: 35
