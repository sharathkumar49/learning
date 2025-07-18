"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example usage:
if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))           # Output: 5
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))    # Output: 4
