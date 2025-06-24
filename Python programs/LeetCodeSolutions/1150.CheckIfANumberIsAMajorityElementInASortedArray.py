"""
1150. Check If a Number Is a Majority Element in a Sorted Array

Given an array nums sorted in non-decreasing order and a target, return True if target is a majority element (appears more than n/2 times), else False.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
- 1 <= target <= 10^9

Example:
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: True

"""
def isMajorityElement(nums, target):
    n = len(nums)
    from bisect import bisect_left, bisect_right
    left = bisect_left(nums, target)
    right = bisect_right(nums, target)
    return right - left > n // 2

# Example usage
if __name__ == "__main__":
    print(isMajorityElement([2,4,5,5,5,5,5,6,6], 5))  # Output: True
