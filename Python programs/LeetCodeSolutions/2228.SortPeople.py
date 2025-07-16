"""
LeetCode 2228. Sort People

Given names and heights, return names sorted by heights in descending order.

Example:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]

Constraints:
- 1 <= names.length == heights.length <= 1000
- 1 <= heights[i] <= 10^5
"""

def sortPeople(names, heights):
    return [name for _, name in sorted(zip(heights, names), reverse=True)]

# Example usage:
# print(sortPeople(["Mary","John","Emma"], [180,165,170]))  # Output: ["Mary","Emma","John"]
