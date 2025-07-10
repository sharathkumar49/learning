"""
LeetCode 1515. Best Position for a Service Centre

Given positions of customers in a 2D plane, return the minimum possible sum of Euclidean distances from a service centre to all customers.

Constraints:
- 1 <= positions.length <= 50
- positions[i].length == 2
- 0 <= positions[i][0], positions[i][1] <= 100

Example:
Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.0
"""
def getMinDistSum(positions):
    import random
    def dist(x, y):
        return sum(((x-px)**2 + (y-py)**2)**0.5 for px, py in positions)
    x = sum(p[0] for p in positions) / len(positions)
    y = sum(p[1] for p in positions) / len(positions)
    step = 1
    res = dist(x, y)
    for _ in range(10000):
        found = False
        for dx, dy in [(step,0),(-step,0),(0,step),(0,-step)]:
            nx, ny = x+dx, y+dy
            d = dist(nx, ny)
            if d < res:
                res = d
                x, y = nx, ny
                found = True
        if not found:
            step /= 2
    return res

# Example usage:
positions = [[0,1],[1,0],[1,2],[2,1]]
print(round(getMinDistSum(positions), 5))  # Output: 4.0
