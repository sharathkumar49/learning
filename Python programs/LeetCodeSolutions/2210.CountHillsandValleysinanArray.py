"""
LeetCode 2210. Count Hills and Valleys in an Array

Given an array nums, return the number of hills and valleys in it. A hill or valley is an element which is strictly greater (hill) or strictly smaller (valley) than its adjacent elements.

Example:
Input: nums = [2,4,1,1,6,5]
Output: 3

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def countHillValley(nums):
    count = 0
    # Remove consecutive duplicates
    arr = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i-1]]
    
    for i in range(1, len(arr)-1):
        # Check if current element is hill or valley
        if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or \
           (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
            count += 1
    
    return count

# Example usage:
# print(countHillValley([2,4,1,1,6,5]))  # Output: 3
