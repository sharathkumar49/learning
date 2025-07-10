"""
LeetCode 1471. The k Strongest Values in an Array

Given an array arr and an integer k, return the k strongest values in the array. A value x is stronger than a value y if |x - m| > |y - m| or if |x - m| == |y - m| and x > y, where m is the median of the array.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= arr.length
- 1 <= arr[i] <= 10^5

Example:
Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
"""
def getStrongest(arr, k):
    arr.sort()
    n = len(arr)
    m = arr[(n-1)//2]
    arr.sort(key=lambda x: (abs(x-m), x), reverse=True)
    return arr[:k]

# Example usage:
arr = [1,2,3,4,5]
k = 2
print(getStrongest(arr, k))  # Output: [5, 1]
