"""
LeetCode 1342. Number of Steps to Reduce a Number to Zero

Given an integer num, return the number of steps to reduce it to zero. If the number is even, divide by 2, else subtract 1.

Constraints:
- 0 <= num <= 10^6

Example:
Input: num = 14
Output: 6
"""
def numberOfSteps(num):
    steps = 0
    while num:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

# Example usage:
num = 14
print(numberOfSteps(num))  # Output: 6
