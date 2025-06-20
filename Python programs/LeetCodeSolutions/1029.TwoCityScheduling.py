"""
1029. Two City Scheduling

There are 2N people, each person wants to fly to one of two cities. The cost of flying the i-th person to city A is costs[i][0], and to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Constraints:
- 2 * n == costs.length
- 2 <= costs.length <= 100
- 1 <= costs[i][0], costs[i][1] <= 1000

Example:
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: Send the first and fourth person to city A and the second and third to city B.
"""
from typing import List

def twoCitySchedCost(costs: List[List[int]]) -> int:
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    return sum(x[0] for x in costs[:n]) + sum(x[1] for x in costs[n:])

# Example usage:
costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))  # Output: 110
