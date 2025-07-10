"""
LeetCode 2021. Brightest Position on Street

Given n street lights, each with a position and range, return the position with the maximum brightness.

Example:
Input: lights = [[1,2],[2,1],[3,1]]
Output: 2

Constraints:
- 1 <= n <= 10^5
- 1 <= position, range <= 10^9
"""

def brightestPosition(lights):
    from collections import defaultdict
    events = defaultdict(int)
    for pos, rng in lights:
        events[pos - rng] += 1
        events[pos + rng + 1] -= 1
    max_bright = curr = 0
    res = 0
    for x in sorted(events):
        curr += events[x]
        if curr > max_bright:
            max_bright = curr
            res = x
    return res

# Example usage:
# print(brightestPosition([[1,2],[2,1],[3,1]]))  # Output: 2
