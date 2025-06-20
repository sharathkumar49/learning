"""
LeetCode 755. Pour Water

You are given an elevation map represented by an integer array heights and an integer V representing the amount of water, and an integer K representing the index at which water is poured.
Return the resulting heights after pouring V units of water at index K.

Example 1:
Input: heights = [2,1,1,2,1,2,2], V = 4, K = 3
Output: [2,2,2,3,2,2,2]

Example 2:
Input: heights = [1,2,3,4], V = 2, K = 2
Output: [2,3,3,4]

Constraints:
- 1 <= heights.length <= 100
- 1 <= V <= 2000
- 0 <= heights[i] <= 100
- 0 <= K < heights.length
"""
from typing import List

def pourWater(heights: List[int], V: int, K: int) -> List[int]:
    n = len(heights)
    for _ in range(V):
        i = K
        while i > 0 and heights[i] >= heights[i-1]:
            i -= 1
        while i < K and heights[i] == heights[i+1]:
            i += 1
        if heights[i] < heights[K]:
            heights[i] += 1
            continue
        i = K
        while i < n-1 and heights[i] >= heights[i+1]:
            i += 1
        while i > K and heights[i] == heights[i-1]:
            i -= 1
        if heights[i] < heights[K]:
            heights[i] += 1
        else:
            heights[K] += 1
    return heights

# Example usage
if __name__ == "__main__":
    print(pourWater([2,1,1,2,1,2,2], 4, 3))  # Output: [2,2,2,3,2,2,2]
    print(pourWater([1,2,3,4], 2, 2))        # Output: [2,3,3,4]
