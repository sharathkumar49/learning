"""
495. Teemo Attacking

Given a list of time points and a duration, return the total time that a target is under attack.

Constraints:
- 1 <= timeSeries.length <= 10^4
- 0 <= timeSeries[i], duration <= 10^7

Example:
Input: timeSeries = [1,4], duration = 2
Output: 4
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        for i in range(1, len(timeSeries)):
            total += min(timeSeries[i] - timeSeries[i-1], duration)
        return total + duration

# Example usage:
sol = Solution()
print(sol.findPoisonedDuration([1,4], 2))  # Output: 4
