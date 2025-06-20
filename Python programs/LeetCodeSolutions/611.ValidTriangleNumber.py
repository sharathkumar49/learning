"""
611. Valid Triangle Number
Difficulty: Medium

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3

Example 2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

def triangleNumber(nums):
    nums.sort()
    n = len(nums)
    count = 0
    for k in range(n-1, 1, -1):
        i, j = 0, k-1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                count += j - i
                j -= 1
            else:
                i += 1
    return count

# Example usage
if __name__ == "__main__":
    print(triangleNumber([2,2,3,4]))  # Output: 3
    print(triangleNumber([4,2,3,4]))  # Output: 4
