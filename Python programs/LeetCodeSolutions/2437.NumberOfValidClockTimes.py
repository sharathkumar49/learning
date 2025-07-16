"""
LeetCode 2437. Number of Valid Clock Times

Given a time string with '?', return the number of valid clock times.

Constraints:
- time is in format "hh:mm"
"""

def countTime(time):
    res = 0
    for h in range(24):
        for m in range(60):
            t = f"{h:02d}:{m:02d}"
            if all(tc == '?' or tc == sc for tc, sc in zip(time, t)):
                res += 1
    return res

# Example usage:
# print(countTime("?5:00"))  # Output: 2
