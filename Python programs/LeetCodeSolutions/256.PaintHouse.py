"""
256. Paint House
https://leetcode.com/problems/paint-house/

There is a row of n houses, each house can be painted with one of the three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
Return the minimum cost to paint all houses.

Constraints:
- costs.length == n
- costs[i].length == 3
- 1 <= n <= 100
- 1 <= costs[i][j] <= 20

Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10

Example 2:
Input: costs = [[7,6,2]]
Output: 2
"""
def minCost(costs):
    if not costs:
        return 0
    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])
    return min(costs[-1])

# Example usage:
if __name__ == "__main__":
    print(minCost([[17,2,17],[16,16,5],[14,3,19]]))  # Output: 10
    print(minCost([[7,6,2]]))                       # Output: 2
