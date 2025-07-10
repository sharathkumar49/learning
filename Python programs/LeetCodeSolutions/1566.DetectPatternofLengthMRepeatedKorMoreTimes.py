"""
LeetCode 1566. Detect Pattern of Length M Repeated K or More Times

Given an array arr, an integer m, and an integer k, return true if there is a pattern of length m that is repeated k or more times.

Constraints:
- 1 <= arr.length <= 100
- 1 <= m <= arr.length
- 2 <= k <= 100

Example:
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: True
"""
def containsPattern(arr, m, k):
    n = len(arr)
    for i in range(n - m * k + 1):
        if all(arr[i + j] == arr[i + j % m] for j in range(m * k)):
            return True
    return False

# Example usage:
arr = [1,2,4,4,4,4]
m = 1
k = 3
print(containsPattern(arr, m, k))  # Output: True
