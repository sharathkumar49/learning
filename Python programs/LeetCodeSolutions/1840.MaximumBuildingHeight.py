"""
LeetCode 1840. Maximum Building Height

You want to build n buildings in a line. The height of the i-th building is h_i. The restrictions are:
- h_1 = 0
- For each adjacent pair of buildings, the difference in their heights is at most 1.
- There are some restrictions given as a list, where each restriction is [i, maxHeight], meaning h_i <= maxHeight.

Return the maximum possible height of the tallest building.

Example 1:
Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2

Constraints:
- 2 <= n <= 10^9
- 0 <= restrictions.length <= min(n - 1, 10^5)
- 2 <= restrictions[i][0] <= n
- 0 <= restrictions[i][1] < n
- All restrictions[i][0] are unique.
"""

def maxBuilding(n, restrictions):
    restrictions.append([1, 0])
    restrictions.append([n, n - 1])
    restrictions.sort()
    m = len(restrictions)
    for i in range(1, m):
        d = restrictions[i][0] - restrictions[i-1][0]
        restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + d)
    for i in range(m-2, -1, -1):
        d = restrictions[i+1][0] - restrictions[i][0]
        restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + d)
    ans = 0
    for i in range(1, m):
        l, r = restrictions[i-1], restrictions[i]
        d = r[0] - l[0]
        h = (l[1] + r[1] + d) // 2
        ans = max(ans, h)
    return ans

# Example usage:
# n = 5
# restrictions = [[2,1],[4,1]]
# print(maxBuilding(n, restrictions))  # Output: 2
