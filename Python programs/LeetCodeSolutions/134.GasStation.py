"""
134. Gas Station
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, where the amount of gas at the i-th station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the i-th station to its next (i+1)-th station.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Constraints:
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4

Example:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
"""
from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    total, start = 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1
            total = 0
    return start

# Example usage:
if __name__ == "__main__":
    print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
    print(canCompleteCircuit([2,3,4], [3,4,3]))          # Output: -1
