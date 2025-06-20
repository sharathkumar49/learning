"""
624. Maximum Distance in Arrays
Difficulty: Easy

You are given m arrays, each sorted in ascending order, find the maximum distance between the minimum value in one array and the maximum value in another array.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4

Constraints:
2 <= m <= 10^5
1 <= arrays[i].length <= 500
-10^4 <= arrays[i][j] <= 10^4
"""

def maxDistance(arrays):
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    res = 0
    for arr in arrays[1:]:
        res = max(res, abs(arr[-1] - min_val), abs(max_val - arr[0]))
        min_val = min(min_val, arr[0])
        max_val = max(max_val, arr[-1])
    return res

# Example usage
if __name__ == "__main__":
    print(maxDistance([[1,2,3],[4,5],[1,2,3]]))  # Output: 4
