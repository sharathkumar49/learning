"""
LeetCode 1331. Rank Transform of an Array

Given an array arr, return an array of its rank transform. The rank is the position in the sorted list of unique elements.

Constraints:
- 1 <= arr.length <= 10^5
- -10^9 <= arr[i] <= 10^9

Example:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
"""
def arrayRankTransform(arr):
    rank = {v: i+1 for i, v in enumerate(sorted(set(arr)))}
    return [rank[x] for x in arr]

# Example usage:
arr = [40,10,20,30]
print(arrayRankTransform(arr))  # Output: [4,1,2,3]
