"""
LeetCode 1310. XOR Queries of a Subarray

Given an array arr and a list of queries, return the XOR of elements from L to R for each query.

Constraints:
- 1 <= arr.length <= 3 * 10^4
- 1 <= arr[i] <= 10^9
- 1 <= queries.length <= 3 * 10^4
- queries[i].length == 2

Example:
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
"""
def xorQueries(arr, queries):
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1] ^ x)
    return [prefix[r+1] ^ prefix[l] for l, r in queries]

# Example usage:
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr, queries))  # Output: [2, 7, 14, 8]
