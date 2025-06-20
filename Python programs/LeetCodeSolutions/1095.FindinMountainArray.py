"""
1095. Find in Mountain Array

(This problem is designed for the LeetCode interactive judge. The MountainArray API is not implemented here.)

Given a mountain array, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

Constraints:
- 3 <= mountainArr.length() <= 10000
- 0 <= target <= 10^9
- 0 <= mountainArr.get(index) <= 10^9

Example:
Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
"""
# Note: The MountainArray API is not implemented in this code.
# This is a template for LeetCode's interactive judge.

def findInMountainArray(target, mountain_arr):
    # mountain_arr should implement get(index) and length()
    def find_peak():
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left
    def binary_search(left, right, target, asc=True):
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if asc:
                if val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if val > target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    peak = find_peak()
    idx = binary_search(0, peak, target, True)
    if idx != -1:
        return idx
    return binary_search(peak + 1, mountain_arr.length() - 1, target, False)

# Example usage:
# Not executable without MountainArray API
# mountainArr = MountainArray([1,2,3,4,5,3,1])
# target = 3
# print(findInMountainArray(target, mountainArr))  # Output: 2
