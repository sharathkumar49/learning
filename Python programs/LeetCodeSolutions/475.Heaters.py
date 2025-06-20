"""
475. Heaters

Given positions of houses and heaters on a horizontal line, find the minimum radius of heaters so that all houses are covered.

Constraints:
- 1 <= houses.length, heaters.length <= 3 * 10^4
- 1 <= houses[i], heaters[i] <= 10^9

Example:
Input: houses = [1,2,3], heaters = [2]
Output: 1
"""

import bisect

class Solution:
    def findRadius(self, houses: list, heaters: list) -> int:
        heaters.sort()
        res = 0
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            left = heaters[i-1] if i > 0 else float('-inf')
            right = heaters[i] if i < len(heaters) else float('inf')
            res = max(res, min(abs(house-left), abs(house-right)))
        return res

# Example usage:
sol = Solution()
houses = [1,2,3]
heaters = [2]
print(sol.findRadius(houses, heaters))  # Output: 1
