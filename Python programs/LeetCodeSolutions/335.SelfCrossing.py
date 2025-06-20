"""
335. Self Crossing

You are given an array of integers distance.
A self-crossing occurs when a path crosses itself. Return true if the path crosses itself at any point, otherwise return false.

Constraints:
- 1 <= distance.length <= 10^5
- 1 <= distance[i] <= 10^6
"""
from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
            if i >= 5 and distance[i-2] >= distance[i-4] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] <= distance[i-3] and distance[i-1] + distance[i-5] >= distance[i-3]:
                return True
        return False

# Example usage:
distance = [2,1,1,2]
print(Solution().isSelfCrossing(distance))  # Output: True
