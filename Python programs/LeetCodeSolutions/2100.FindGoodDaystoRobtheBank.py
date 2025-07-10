"""
LeetCode 2100. Find Good Days to Rob the Bank

Given an array security and an integer time, return all days where it is good to rob the bank.

Example:
Input: security = [5,3,3,3,5,6,2], time = 2
Output: [2,3]

Constraints:
- 1 <= security.length <= 10^5
- 0 <= security[i] <= 10^5
- 0 <= time <= 10^5
"""

def goodDaysToRobBank(security, time):
    n = len(security)
    noninc = [0]*n
    nondec = [0]*n
    for i in range(1, n):
        if security[i] <= security[i-1]:
            noninc[i] = noninc[i-1] + 1
    for i in range(n-2, -1, -1):
        if security[i] <= security[i+1]:
            nondec[i] = nondec[i+1] + 1
    return [i for i in range(time, n-time) if noninc[i] >= time and nondec[i] >= time]

# Example usage:
# print(goodDaysToRobBank([5,3,3,3,5,6,2], 2))  # Output: [2,3]
