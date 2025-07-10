"""
LeetCode 1534. Count Good Triplets

Given an array arr and integers a, b, c, return the number of good triplets.
A triplet (i, j, k) is good if:
- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c

Constraints:
- 3 <= arr.length <= 100
- 0 <= arr[i] <= 1000
- 0 <= a, b, c <= 1000

Example:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
"""
def countGoodTriplets(arr, a, b, c):
    n = len(arr)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                    res += 1
    return res

# Example usage:
arr = [3,0,1,1,9,7]
a, b, c = 7, 2, 3
print(countGoodTriplets(arr, a, b, c))  # Output: 4
