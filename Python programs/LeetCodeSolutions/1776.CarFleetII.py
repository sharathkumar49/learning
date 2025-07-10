"""
LeetCode 1776. Car Fleet II

Given a list of cars with positions and speeds, return the time at which each car collides with the next car, or -1 if it never collides.

Example 1:
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]

Constraints:
- 1 <= cars.length <= 10^5
- 1 <= positioni, speedi <= 10^6
- positioni < positioni+1
"""

def getCollisionTimes(cars):
    n = len(cars)
    res = [-1.0]*n
    stack = []
    for i in range(n-1, -1, -1):
        p, s = cars[i]
        while stack:
            j = stack[-1]
            if s <= cars[j][1]:
                stack.pop()
            else:
                t = (cars[j][0] - p) / (s - cars[j][1])
                if res[j] == -1 or t <= res[j]:
                    res[i] = t
                    break
                else:
                    stack.pop()
        stack.append(i)
    return res

# Example usage:
# cars = [[1,2],[2,1],[4,3],[7,2]]
# print(getCollisionTimes(cars))  # Output: [1.0,-1.0,3.0,-1.0]
