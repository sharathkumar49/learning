"""
264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

Given an integer n, return the nth ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, and 5.

Constraints:
- 1 <= n <= 1690

Example 1:
Input: n = 10
Output: 12

Example 2:
Input: n = 1
Output: 1
"""
def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    for _ in range(1, n):
        next2, next3, next5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        next_ugly = min(next2, next3, next5)
        ugly.append(next_ugly)
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1
    return ugly[-1]

# Example usage:
if __name__ == "__main__":
    print(nthUglyNumber(10))  # Output: 12
    print(nthUglyNumber(1))   # Output: 1
