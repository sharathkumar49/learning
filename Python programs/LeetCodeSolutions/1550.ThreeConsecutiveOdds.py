"""
LeetCode 1550. Three Consecutive Odds

Given an array arr, return true if there are three consecutive odd numbers, otherwise return false.

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000

Example:
Input: arr = [2,6,4,1]
Output: False
"""
def threeConsecutiveOdds(arr):
    for i in range(len(arr)-2):
        if arr[i]%2 and arr[i+1]%2 and arr[i+2]%2:
            return True
    return False

# Example usage:
arr = [2,6,4,1]
print(threeConsecutiveOdds(arr))  # Output: False
