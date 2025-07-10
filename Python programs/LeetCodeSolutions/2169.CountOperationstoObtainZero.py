"""
LeetCode 2169. Count Operations to Obtain Zero

Given two integers num1 and num2, perform the following operation until either is 0: subtract the smaller from the larger. Return the number of operations performed.

Example:
Input: num1 = 2, num2 = 3
Output: 3

Constraints:
- 0 <= num1, num2 <= 10^5
"""

def countOperations(num1, num2):
    res = 0
    while num1 and num2:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        res += 1
    return res

# Example usage:
# print(countOperations(2, 3))  # Output: 3
