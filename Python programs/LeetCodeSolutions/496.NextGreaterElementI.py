"""
496. Next Greater Element I

Given two arrays nums1 and nums2, return an array of the next greater element for each element in nums1 in nums2. The next greater element for an element x in nums1 is the first greater element to the right of x in nums2. If it does not exist, return -1 for that number.

Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
"""

class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        nge = {}
        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)
        return [nge.get(num, -1) for num in nums1]

# Example usage:
sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]
