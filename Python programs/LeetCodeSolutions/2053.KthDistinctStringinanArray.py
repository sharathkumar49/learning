"""
LeetCode 2053. Kth Distinct String in an Array

Given an array of strings arr and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string.

Example:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i].length <= 30
"""

def kthDistinct(arr, k):
    from collections import Counter
    count = Counter(arr)
    for s in arr:
        if count[s] == 1:
            k -= 1
            if k == 0:
                return s
    return ""

# Example usage:
# print(kthDistinct(["d","b","c","b","c","a"], 2))  # Output: "a"
