"""
LeetCode 2141. Maximum Running Time of N Computers

You have n computers. You are given the integer n and a 0-indexed integer array batteries where the i-th battery can run a computer for batteries[i] minutes. You are to assign each battery to a computer. The computers can be connected to any number of batteries, and a battery can be used by only one computer at a time. The computers start running simultaneously and run until they run out of power. Return the maximum number of minutes you can run all the n computers simultaneously.

Example:
Input: n = 2, batteries = [3,3,3]
Output: 4

Constraints:
- 1 <= n <= batteries.length <= 10^5
- 1 <= batteries[i] <= 10^9
"""

def maxRunTime(n, batteries):
    batteries.sort()
    total = sum(batteries)
    left, right = 0, total // n
    while left < right:
        mid = (right + left + 1) // 2
        if sum(min(b, mid) for b in batteries) >= n * mid:
            left = mid
        else:
            right = mid - 1
    return left

# Example usage:
# print(maxRunTime(2, [3,3,3]))  # Output: 4
