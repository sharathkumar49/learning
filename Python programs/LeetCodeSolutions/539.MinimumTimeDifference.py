"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time points in the list.

Constraints:
- 2 <= timePoints.length <= 2 * 10^4
- timePoints[i] is in the format "HH:MM".

Example:
Input: timePoints = ["23:59","00:00"]
Output: 1
"""

class Solution:
    def findMinDifference(self, timePoints: list) -> int:
        minutes = sorted(int(t[:2])*60 + int(t[3:]) for t in timePoints)
        minutes.append(minutes[0] + 1440)
        return min(b - a for a, b in zip(minutes, minutes[1:]))

# Example usage:
sol = Solution()
print(sol.findMinDifference(["23:59","00:00"]))  # Output: 1
