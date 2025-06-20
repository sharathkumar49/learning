"""
319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb, then you turn on every third bulb, and so on. You repeat this process for n rounds. Return the number of bulbs that are on after n rounds.

Constraints:
- 0 <= n <= 10^9
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)

# Example usage:
n = 3
print(Solution().bulbSwitch(n))  # Output: 1
