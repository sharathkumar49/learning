"""
LeetCode 2282. Number of People That Can Be Seen in a Grid

Given heights, return the number of people that can be seen in each row and column.

Example:
Input: heights = [[3,1,4],[2,5,6],[1,2,3]]
Output: [[2,1,2],[1,2,2],[1,1,2]]

Constraints:
- 1 <= heights.length, heights[0].length <= 100
"""

def canSeePeople(heights):
    m, n = len(heights), len(heights[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(j+1, n):
                if heights[i][k] > heights[i][j]:
                    res[i][j] += 1
                    break
            for k in range(i+1, m):
                if heights[k][j] > heights[i][j]:
                    res[i][j] += 1
                    break
    return res

# Example usage:
# print(canSeePeople([[3,1,4],[2,5,6],[1,2,3]]))  # Output: [[2,1,2],[1,2,2],[1,1,2]]
