"""
LeetCode 1346. Check If N and Its Double Exist

Given an array arr, check if there exists two integers N and M such that N is the double of M (N = 2 * M).

Constraints:
- 2 <= arr.length <= 500
- -10^3 <= arr[i] <= 10^3

Example:
Input: arr = [10,2,5,3]
Output: True
"""
def checkIfExist(arr):
    s = set()
    for x in arr:
        if 2*x in s or (x%2==0 and x//2 in s):
            return True
        s.add(x)
    return False

# Example usage:
arr = [10,2,5,3]
print(checkIfExist(arr))  # Output: True
