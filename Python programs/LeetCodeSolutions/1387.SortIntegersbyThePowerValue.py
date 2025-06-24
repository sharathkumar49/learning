"""
LeetCode 1387. Sort Integers by The Power Value

The power of an integer x is defined as the number of steps to transform x into 1 using the following steps:
- if x is even, x = x / 2
- if x is odd, x = 3 * x + 1

Given three integers lo, hi, and k, return the k-th integer in the range [lo, hi] sorted by the power value.

Constraints:
- 1 <= lo <= hi <= 1000
- 1 <= k <= hi - lo + 1

Example:
Input: lo = 12, hi = 15, k = 2
Output: 13
"""
def getKth(lo, hi, k):
    def power(x):
        steps = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            steps += 1
        return steps
    arr = [(power(i), i) for i in range(lo, hi+1)]
    arr.sort()
    return arr[k-1][1]

# Example usage:
lo = 12
hi = 15
k = 2
print(getKth(lo, hi, k))  # Output: 13
