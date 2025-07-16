"""
LeetCode 2231. Largest Number After Digit Swaps by Parity

Given an integer num, return the largest number you can get by swapping digits of the same parity.

Example:
Input: num = 1234
Output: 3412

Constraints:
- 1 <= num <= 10^9
"""

def largestInteger(num):
    digits = [int(d) for d in str(num)]
    odds = sorted([d for d in digits if d%2], reverse=True)
    evens = sorted([d for d in digits if d%2==0], reverse=True)
    res = []
    for d in digits:
        if d%2:
            res.append(odds.pop(0))
        else:
            res.append(evens.pop(0))
    return int(''.join(map(str, res)))

# Example usage:
# print(largestInteger(1234))  # Output: 3412
