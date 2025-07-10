"""
LeetCode 1539. Kth Missing Positive Number

Given an array arr of sorted unique positive integers and an integer k, return the kth missing positive number.

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
- 1 <= k <= 1000

Example:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
"""
def findKthPositive(arr, k):
    cur = 1
    for a in arr:
        while cur < a:
            k -= 1
            if k == 0:
                return cur
            cur += 1
        cur = a + 1
    return cur + k - 1

# Example usage:
arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k))  # Output: 9
