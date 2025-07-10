"""
LeetCode 1497. Check If Array Pairs Are Divisible by k

Given an array of integers arr and an integer k, return true if it is possible to divide the array into pairs such that the sum of each pair is divisible by k.

Constraints:
- arr.length is even
- 1 <= arr.length <= 10^5
- -10^9 <= arr[i] <= 10^9
- 1 <= k <= 10^5

Example:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: True
"""
def canArrange(arr, k):
    from collections import Counter
    count = Counter([a % k for a in arr])
    for r in count:
        if r == 0:
            if count[r] % 2 != 0:
                return False
        else:
            if count[r] != count.get(k - r, 0):
                return False
    return True

# Example usage:
arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
print(canArrange(arr, k))  # Output: True
