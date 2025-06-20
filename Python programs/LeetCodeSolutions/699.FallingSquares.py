"""
LeetCode 699. Falling Squares

Given a list of positions where squares drop down onto an infinite number line, return an array representing the height of the tallest stack after each square falls.

Example 1:
Input: positions = [[1,2],[2,3],[6,1]]
Output: [2,5,5]

Example 2:
Input: positions = [[100,100],[200,100]]
Output: [100,100]

Constraints:
- 1 <= positions.length <= 1000
- 1 <= positions[i][0] <= 10^8
- 1 <= positions[i][1] <= 10^6
"""
from typing import List

def fallingSquares(positions: List[List[int]]) -> List[int]:
    ans = []
    intervals = []
    max_height = 0
    for left, size in positions:
        right = left + size
        base = 0
        for l, r, h in intervals:
            if l < right and left < r:
                base = max(base, h)
        height = base + size
        intervals.append((left, right, height))
        max_height = max(max_height, height)
        ans.append(max_height)
    return ans

# Example usage
if __name__ == "__main__":
    print(fallingSquares([[1,2],[2,3],[6,1]]))      # Output: [2,5,5]
    print(fallingSquares([[100,100],[200,100]]))    # Output: [100,100]
