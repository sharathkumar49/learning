"""
LeetCode 1904. The Number of Full Rounds You Have Played

Given two strings startTime and finishTime in "HH:MM" format, return the number of full 15-minute rounds played between them.

Example:
Input: startTime = "12:01", finishTime = "12:44"
Output: 1

Constraints:
- startTime and finishTime are in the format "HH:MM"
"""

def numberOfRounds(startTime, finishTime):
    def toMin(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    s, f = toMin(startTime), toMin(finishTime)
    if f < s:
        f += 24 * 60
    return max(0, (f // 15 - (s + 14) // 15))

# Example usage:
# print(numberOfRounds("12:01", "12:44"))  # Output: 1
