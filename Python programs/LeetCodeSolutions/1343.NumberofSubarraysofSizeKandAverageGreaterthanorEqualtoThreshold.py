"""
LeetCode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an array arr, an integer k, and a threshold, return the number of sub-arrays of size k with average >= threshold.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= arr.length
- 0 <= arr[i] <= 10^4
- 0 <= threshold <= 10^4

Example:
Input: arr = [2,1,3,4,1,2,3,4], k = 4, threshold = 1
Output: 6
"""
def numOfSubarrays(arr, k, threshold):
    target = k * threshold
    s = sum(arr[:k])
    res = 1 if s >= target else 0
    for i in range(k, len(arr)):
        s += arr[i] - arr[i-k]
        if s >= target:
            res += 1
    return res

# Example usage:
arr = [2,1,3,4,1,2,3,4]
k = 4
threshold = 1
print(numOfSubarrays(arr, k, threshold))  # Output: 6
