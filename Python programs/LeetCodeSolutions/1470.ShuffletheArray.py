"""
LeetCode 1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn], return the array in the form [x1,y1,x2,y2,...,xn,yn].

Constraints:
- 1 <= n <= 500
- nums.length == 2n
- 1 <= nums[i] <= 10^3

Example:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
"""
def shuffle(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

# Example usage:
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))  # Output: [2,3,5,4,1,7]
