"""
LeetCode 2122. Recover the Original Array

Given an array nums formed by adding and subtracting k to elements of the original array, return the original array.

Example:
Input: nums = [2,10,6,4,8,12], Output: [6,8,10]

Constraints:
- 2 <= nums.length <= 2000
- nums.length is even
- 1 <= nums[i] <= 10^9
"""

def recoverArray(nums):
    nums.sort()
    n = len(nums)//2
    for k in range(1, (nums[-1]-nums[0])//2+1):
        if (nums[1]-nums[0])%2 == 1:
            continue
        s = nums[:]
        res = []
        for _ in range(n):
            x = s[0]
            s.remove(x)
            if x+k not in s:
                break
            s.remove(x+k)
            res.append(x+k//2)
        if len(res) == n:
            return res
    return []

# Example usage:
# print(recoverArray([2,10,6,4,8,12]))  # Output: [6,8,10]
