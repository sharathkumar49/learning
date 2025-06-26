"""
LeetCode 1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array arr, return the number of triplets (i, j, k) such that the XOR of arr[i] to arr[j-1] is equal to the XOR of arr[j] to arr[k].

Constraints:
- 1 <= arr.length <= 300
- 1 <= arr[i] <= 10^8

Example:
Input: arr = [2,3,1,6,7]
Output: 4
"""
def countTriplets(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        xor = 0
        for k in range(i, n):
            xor ^= arr[k]
            if xor == 0 and k > i:
                res += k - i
    return res

# Example usage:
arr = [2,3,1,6,7]
print(countTriplets(arr))  # Output: 4
