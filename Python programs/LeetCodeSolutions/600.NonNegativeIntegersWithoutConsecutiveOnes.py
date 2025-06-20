"""
600. Non-negative Integers without Consecutive Ones
Difficulty: Hard

Given a positive integer n, return the number of non-negative integers less than or equal to n, whose binary representations do not contain consecutive ones.

Example 1:
Input: n = 5
Output: 5
Explanation: The integers are 0, 1, 2, 4, and 5.

Constraints:
1 <= n <= 10^9
"""

def findIntegers(n):
    fib = [1, 2] + [0]*30
    for i in range(2, 32):
        fib[i] = fib[i-1] + fib[i-2]
    res, k, prev_bit = 0, 30, 0
    while k >= 0:
        if n & (1 << k):
            res += fib[k]
            if prev_bit:
                return res
            prev_bit = 1
        else:
            prev_bit = 0
        k -= 1
    return res + 1

# Example usage
if __name__ == "__main__":
    print(findIntegers(5))  # Output: 5
