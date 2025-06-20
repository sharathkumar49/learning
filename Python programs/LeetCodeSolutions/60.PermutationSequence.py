# 60. Permutation Sequence
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# Given n and k, return the kth permutation sequence.
#
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
#
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
#
# Constraints:
# 1 <= n <= 9
# 1 <= k <= n!

def getPermutation(n, k):
    import math
    nums = [str(i) for i in range(1, n+1)]
    k -= 1
    res = ''
    for i in range(n, 0, -1):
        idx, k = divmod(k, math.factorial(i-1))
        res += nums.pop(idx)
    return res

# Example usage
n = 3
k = 3
print("Permutation sequence:", getPermutation(n, k))  # Output: "213"
