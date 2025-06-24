"""
1237. Find Positive Integer Solution for a Given Equation

Given a function f(x, y) that is strictly increasing in both x and y, and a target z, return all positive integer pairs (x, y) such that f(x, y) == z.

Constraints:
- 1 <= x, y <= 1000
- 1 <= z <= 1000

Example:
Input: z = 5, f(x, y) = x + y
Output: [[1,4],[2,3],[3,2],[4,1]]

"""
# Note: f(x, y) is a black-box function provided by the problem.
def findSolution(customfunction, z):
    res = []
    for x in range(1, 1001):
        for y in range(1, 1001):
            if customfunction.f(x, y) == z:
                res.append([x, y])
            elif customfunction.f(x, y) > z:
                break
    return res

# Example usage
# Not executable without customfunction API
