"""
941. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

An array arr is a mountain if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[arr.length - 1].

Constraints:
- 3 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^6
- arr is guaranteed to be a mountain array.

Example:
Input: arr = [0,2,1,0]
Output: 1
"""
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

# Example usage
if __name__ == "__main__":
    arr = [0,2,1,0]
    print(Solution().peakIndexInMountainArray(arr))  # Output: 1
