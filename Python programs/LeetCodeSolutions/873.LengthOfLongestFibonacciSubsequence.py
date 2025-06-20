"""
873. Length of Longest Fibonacci Subsequence

Given an array arr, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5

Example 2:
Input: arr = [1,3,7,11,12,14,18]
Output: 3

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] < 10^9
"""
def lenLongestFibSubseq(arr):
    s = set(arr)
    n = len(arr)
    maxlen = 0
    for i in range(n):
        for j in range(i+1, n):
            x, y, l = arr[i], arr[j], 2
            while x + y in s:
                x, y = y, x + y
                l += 1
            if l > 2:
                maxlen = max(maxlen, l)
    return maxlen

# Example usage:
print(lenLongestFibSubseq([1,2,3,4,5,6,7,8]))  # Output: 5
print(lenLongestFibSubseq([1,3,7,11,12,14,18]))  # Output: 3
