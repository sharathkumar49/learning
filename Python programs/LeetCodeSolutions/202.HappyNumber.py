"""
202. Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Constraints:
- 1 <= n <= 2^31 - 1

Example 1:
Input: n = 19
Output: true

Example 2:
Input: n = 2
Output: false
"""
def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(x) ** 2 for x in str(n))
    return n == 1

# Example usage:
if __name__ == "__main__":
    print(isHappy(19))  # Output: True
    print(isHappy(2))   # Output: False
