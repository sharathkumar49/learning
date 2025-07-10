"""
LeetCode 1762. Buildings With an Ocean View

Given an array heights, return the indices of the buildings that have an ocean view (to the right, no taller building).

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]

Constraints:
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9
"""

def findBuildings(heights):
    res = []
    max_h = 0
    for i in range(len(heights)-1, -1, -1):
        if heights[i] > max_h:
            res.append(i)
            max_h = heights[i]
    return res[::-1]

# Example usage:
# heights = [4,2,3,1]
# print(findBuildings(heights))  # Output: [0,2,3]
