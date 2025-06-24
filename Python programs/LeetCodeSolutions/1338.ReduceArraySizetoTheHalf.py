"""
LeetCode 1338. Reduce Array Size to The Half

Given an array arr, return the minimum number of sets you need to remove so that at least half of the integers are removed.

Constraints:
- 2 <= arr.length <= 10^5
- arr.length is even
- 1 <= arr[i] <= 10^5

Example:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
"""
def minSetSize(arr):
    from collections import Counter
    count = Counter(arr)
    arr_sorted = sorted(count.values(), reverse=True)
    removed, res, half = 0, 0, len(arr)//2
    for c in arr_sorted:
        removed += c
        res += 1
        if removed >= half:
            break
    return res

# Example usage:
arr = [3,3,3,3,5,5,5,2,2,7]
print(minSetSize(arr))  # Output: 2
