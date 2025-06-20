"""
658. Find K Closest Elements
Difficulty: Medium

Given a sorted array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 10^4
-10^4 <= arr[i], x <= 10^4
"""

def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

# Example usage
if __name__ == "__main__":
    print(findClosestElements([1,2,3,4,5], 4, 3))   # Output: [1,2,3,4]
    print(findClosestElements([1,2,3,4,5], 4, -1))  # Output: [1,2,3,4]
