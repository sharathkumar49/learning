"""
1124. Longest Well-Performing Interval

Given hours, return the length of the longest well-performing interval. An interval is well-performing if the number of tiring days is strictly greater than the number of non-tiring days.

Constraints:
- 1 <= hours.length <= 10^4
- 0 <= hours[i] <= 16

Example:
Input: hours = [9,9,6,0,6,6,9]
Output: 3
"""
from typing import List

def longestWPI(hours: List[int]) -> int:
    score = 0
    seen = {0: -1}
    res = 0
    for i, h in enumerate(hours):
        score += 1 if h > 8 else -1
        if score > 0:
            res = i + 1
        elif score - 1 in seen:
            res = max(res, i - seen[score - 1])
        if score not in seen:
            seen[score] = i
    return res

# Example usage:
hours = [9,9,6,0,6,6,9]
print(longestWPI(hours))  # Output: 3
