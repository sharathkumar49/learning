"""
LeetCode 2305. Fair Distribution of Cookies

Given cookies and k, return the minimum unfairness.

Example:
Input: cookies = [8,15,10,20,8], k = 2
Output: 31

Constraints:
- 1 <= cookies.length <= 8
- 1 <= k <= cookies.length
"""

def distributeCookies(cookies, k):
    res = float('inf')
    def dfs(i, children):
        nonlocal res
        if i == len(cookies):
            res = min(res, max(children))
            return
        for j in range(k):
            children[j] += cookies[i]
            dfs(i+1, children)
            children[j] -= cookies[i]
    dfs(0, [0]*k)
    return res

# Example usage:
# print(distributeCookies([8,15,10,20,8], 2))  # Output: 31
