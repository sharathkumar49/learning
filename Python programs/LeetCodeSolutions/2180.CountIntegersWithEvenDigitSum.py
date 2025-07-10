"""
LeetCode 2180. Count Integers With Even Digit Sum

Given an integer num, return the number of positive integers less than or equal to num whose digit sums are even.

Example:
Input: num = 30
Output: 14

Constraints:
- 1 <= num <= 1000
"""

def countEven(num):
    def digit_sum(x):
        return sum(int(d) for d in str(x))
    return sum(digit_sum(i)%2==0 for i in range(1, num+1))

# Example usage:
# print(countEven(30))  # Output: 14
