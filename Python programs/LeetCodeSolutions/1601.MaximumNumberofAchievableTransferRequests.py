"""
LeetCode 1601. Maximum Number of Achievable Transfer Requests

Given n buildings and a list of transfer requests, return the maximum number of requests that can be satisfied such that the net change of employees in every building is zero.

Example 1:
Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5

Constraints:
- 1 <= n <= 20
- 1 <= requests.length <= 16
- 0 <= fromi, toi < n
"""

def maximumRequests(n, requests):
    res = 0
    for mask in range(1<<len(requests)):
        cnt = [0]*n
        num = 0
        for i in range(len(requests)):
            if mask & (1<<i):
                cnt[requests[i][0]] -= 1
                cnt[requests[i][1]] += 1
                num += 1
        if all(x == 0 for x in cnt):
            res = max(res, num)
    return res

# Example usage:
# n = 5
# requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
# print(maximumRequests(n, requests))  # Output: 5
