"""
LeetCode 1441. Build an Array With Stack Operations

Given an array target and an integer n, return the stack operations to build the array target from [1, 2, ..., n].

Constraints:
- 1 <= target.length <= 100
- 1 <= n <= 100
- 1 <= target[i] <= n
- target is strictly increasing.

Example:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
"""
def buildArray(target, n):
    res = []
    curr = 1
    for t in target:
        while curr < t:
            res.append("Push")
            res.append("Pop")
            curr += 1
        res.append("Push")
        curr += 1
    return res

# Example usage:
target = [1,3]
n = 3
print(buildArray(target, n))  # Output: ['Push', 'Push', 'Pop', 'Push']
