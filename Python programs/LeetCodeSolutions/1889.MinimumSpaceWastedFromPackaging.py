"""
LeetCode 1889. Minimum Space Wasted From Packaging

You are given an integer array packages and a 2D integer array boxes. Each boxes[i] is a list of box sizes from supplier i. Return the minimum total wasted space, or -1 if impossible.

Example:
Input: packages = [2,3,5], boxes = [[4,8],[2,8]]
Output: 6

Constraints:
- 1 <= packages.length <= 10^5
- 1 <= packages[i] <= 10^5
- 1 <= boxes.length <= 100
- 1 <= boxes[i].length <= 10^5
- 1 <= boxes[i][j] <= 10^5
"""

import bisect

def minWastedSpace(packages, boxes):
    packages.sort()
    res = float('inf')
    total = sum(packages)
    for box in boxes:
        box.sort()
        if box[-1] < packages[-1]: continue
        waste = 0
        i = 0
        for b in box:
            j = bisect.bisect_right(packages, b, i)
            waste += (j - i) * b
            i = j
        if i == len(packages):
            res = min(res, waste - total)
    return res if res < float('inf') else -1

# Example usage:
# print(minWastedSpace([2,3,5], [[4,8],[2,8]]))  # Output: 6
