"""
LeetCode 1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number

You are given a string num representing a number and an integer k. Return the minimum number of adjacent swaps required to reach the k-th smallest wonderful integer greater than num, where a wonderful integer is a permutation of num's digits.

Example 1:
Input: num = "5489355142", k = 4
Output: 2

Constraints:
- 2 <= num.length <= 1000
- 1 <= k <= 1000
"""

def getMinSwaps(num, k):
    from copy import deepcopy
    def next_perm(arr):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        if i < 0:
            return False
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:] = reversed(arr[i+1:])
        return True
    arr = list(num)
    target = list(num)
    for _ in range(k):
        next_perm(target)
    res = 0
    arr2 = deepcopy(arr)
    for i in range(len(arr2)):
        if arr2[i] != target[i]:
            j = i
            while arr2[j] != target[i]:
                j += 1
            while j > i:
                arr2[j], arr2[j-1] = arr2[j-1], arr2[j]
                res += 1
                j -= 1
    return res

# Example usage:
# num = "5489355142"
# k = 4
# print(getMinSwaps(num, k))  # Output: 2
