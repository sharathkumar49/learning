"""
LeetCode 1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i] - arr2[j]| <= d.

Constraints:
- 1 <= arr1.length, arr2.length <= 500
- 0 <= arr1[i], arr2[j] <= 1000
- 0 <= d <= 100

Example:
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
"""
def findTheDistanceValue(arr1, arr2, d):
    arr2.sort()
    from bisect import bisect_left, bisect_right
    count = 0
    for x in arr1:
        l = bisect_left(arr2, x - d)
        r = bisect_right(arr2, x + d)
        if l == r:
            count += 1
    return count

# Example usage:
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))  # Output: 2
