"""
786. K-th Smallest Prime Fraction

You are given a sorted array arr of positive integers, where all the integers are unique. You are also given an integer k. Return the k-th smallest fraction formed by arr[i]/arr[j] where 0 <= i < j < arr.length.

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]

Example 2:
Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:
- 2 <= arr.length <= 1000
- 1 <= arr[i] <= 3 * 10^4
- arr[0] < arr[1] < ... < arr[arr.length - 1]
- 1 <= k <= arr.length * (arr.length - 1) / 2
"""
import heapq

def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    heap = []
    for i in range(n):
        for j in range(i+1, n):
            heapq.heappush(heap, (arr[i]/arr[j], arr[i], arr[j]))
    for _ in range(k-1):
        heapq.heappop(heap)
    return [heap[0][1], heap[0][2]]

# Example usage:
print(kthSmallestPrimeFraction([1,2,3,5], 3))  # Output: [2,5]
print(kthSmallestPrimeFraction([1,7], 1))      # Output: [1,7]
