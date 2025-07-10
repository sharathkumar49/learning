"""
LeetCode 1620. Coordinate With Maximum Network Quality

Given a list of towers and an integer radius, return the coordinate with the highest network quality. If there are multiple, return the lexicographically smallest one.

Example 1:
Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
Output: [2,1]

Constraints:
- 1 <= towers.length <= 50
- 0 <= xi, yi <= 50
- 1 <= qi <= 100
- 1 <= radius <= 50
"""

def bestCoordinate(towers, radius):
    def quality(x, y):
        q = 0
        for xi, yi, qi in towers:
            d = ((x-xi)**2 + (y-yi)**2)**0.5
            if d <= radius:
                q += int(qi/(1+d))
        return q
    maxq = 0
    ans = [0,0]
    for x in range(51):
        for y in range(51):
            q = quality(x, y)
            if q > maxq or (q == maxq and [x,y] < ans):
                maxq = q
                ans = [x, y]
    return ans

# Example usage:
# towers = [[1,2,5],[2,1,7],[3,1,9]]
# radius = 2
# print(bestCoordinate(towers, radius))  # Output: [2,1]
