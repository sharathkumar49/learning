"""
LeetCode 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the cake to the ith horizontal cut and similarly for verticalCuts, return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays. Since the answer can be a large number, return it modulo 10^9 + 7.

Constraints:
- 2 <= h, w <= 10^9
- 1 <= horizontalCuts.length, verticalCuts.length <= 10^5
- 1 <= horizontalCuts[i] < h
- 1 <= verticalCuts[i] < w

Example:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
"""
def maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts = sorted([0] + horizontalCuts + [h])
    verticalCuts = sorted([0] + verticalCuts + [w])
    max_h = max(horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts)-1))
    max_w = max(verticalCuts[i+1] - verticalCuts[i] for i in range(len(verticalCuts)-1))
    return (max_h * max_w) % (10**9 + 7)

# Example usage:
h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
print(maxArea(h, w, horizontalCuts, verticalCuts))  # Output: 4
