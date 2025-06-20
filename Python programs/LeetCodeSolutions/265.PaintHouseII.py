"""
265. Paint House II
https://leetcode.com/problems/paint-house-ii/

There is a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
Return the minimum cost to paint all houses.

Constraints:
- costs.length == n
- costs[i].length == k
- 1 <= n <= 100
- 2 <= k <= 20
- 1 <= costs[i][j] <= 20

Example 1:
Input: costs = [[1,5,3],[2,9,4]]
Output: 5

Example 2:
Input: costs = [[1,3],[2,4]]
Output: 5
"""
def minCostII(costs):
    if not costs:
        return 0
    n, k = len(costs), len(costs[0])
    for i in range(1, n):
        for j in range(k):
            costs[i][j] += min(costs[i-1][l] for l in range(k) if l != j)
    return min(costs[-1])

# Example usage:
if __name__ == "__main__":
    print(minCostII([[1,5,3],[2,9,4]]))  # Output: 5
    print(minCostII([[1,3],[2,4]]))      # Output: 5
