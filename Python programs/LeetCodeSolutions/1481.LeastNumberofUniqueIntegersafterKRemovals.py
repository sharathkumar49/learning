"""
LeetCode 1481. Least Number of Unique Integers after K Removals

Given an array arr and an integer k, return the least number of unique integers after removing exactly k elements.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= arr.length
- 1 <= arr[i] <= 10^9

Example:
Input: arr = [5,5,4], k = 1
Output: 1
"""
def findLeastNumOfUniqueInts(arr, k):
    from collections import Counter
    count = Counter(arr)
    freq = sorted(count.values())
    res = len(freq)
    for f in freq:
        if k >= f:
            k -= f
            res -= 1
        else:
            break
    return res

# Example usage:
arr = [5,5,4]
k = 1
print(findLeastNumOfUniqueInts(arr, k))  # Output: 1
