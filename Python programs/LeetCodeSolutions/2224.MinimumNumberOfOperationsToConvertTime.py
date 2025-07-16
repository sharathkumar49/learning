"""
LeetCode 2224. Minimum Number of Operations to Convert Time

Given current and correct time, return the minimum number of operations to convert current to correct time.

Example:
Input: current = "02:30", correct = "04:35"
Output: 3

Constraints:
- current and correct are in "HH:MM" format
"""

def convertTime(current, correct):
    h1, m1 = map(int, current.split(':'))
    h2, m2 = map(int, correct.split(':'))
    diff = (h2*60 + m2) - (h1*60 + m1)
    ops = 0
    for step in [60, 15, 5, 1]:
        ops += diff // step
        diff %= step
    return ops

# Example usage:
# print(convertTime("02:30", "04:35"))  # Output: 3
