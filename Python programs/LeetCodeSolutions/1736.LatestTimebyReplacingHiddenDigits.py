"""
LeetCode 1736. Latest Time by Replacing Hidden Digits

Given a time string in the format "hh:mm", some digits are hidden (represented by '?'). Return the latest valid time by replacing the hidden digits.

Example 1:
Input: time = "2?:?0"
Output: "23:50"

Constraints:
- time is in the format "hh:mm"
- '?' can be any digit
"""

def maximumTime(time):
    time = list(time)
    if time[0] == '?':
        time[0] = '2' if time[1] in '?0123' else '1'
    if time[1] == '?':
        time[1] = '3' if time[0] == '2' else '9'
    if time[3] == '?':
        time[3] = '5'
    if time[4] == '?':
        time[4] = '9'
    return ''.join(time)

# Example usage:
# time = "2?:?0"
# print(maximumTime(time))  # Output: "23:50"
