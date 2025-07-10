"""
LeetCode 1526. Minimum Number of Increments on Subarrays to Form a Target Array

Given an array target, return the minimum number of increment operations needed to form the target array from an array of zeros.

Constraints:
- 1 <= target.length <= 10^5
- 1 <= target[i] <= 10^5

Example:
Input: target = [1,2,3,2,1]
Output: 3
"""
def minNumberOperations(target):
    res = target[0]
    for i in range(1, len(target)):
        if target[i] > target[i-1]:
            res += target[i] - target[i-1]
    return res

# Example usage:
target = [1,2,3,2,1]
print(minNumberOperations(target))  # Output: 3
