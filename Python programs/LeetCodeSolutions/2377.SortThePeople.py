"""
LeetCode 2377. Sort the People

Sort people by their heights.

Constraints:
- 1 <= names.length == heights.length <= 10^3
"""

def sortPeople(names, heights):
    return [name for _, name in sorted(zip(heights, names), reverse=True)]

# Example usage:
# print(sortPeople(["Mary","John","Emma"],[180,165,170]))  # Output: ["Mary","Emma","John"]
