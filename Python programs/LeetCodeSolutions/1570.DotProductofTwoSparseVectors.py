"""
LeetCode 1570. Dot Product of Two Sparse Vectors

Implement class SparseVector with a dotProduct method.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 0 <= nums1[i], nums2[i] <= 100

Example:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
"""
class SparseVector:
    def __init__(self, nums):
        self.data = {i: v for i, v in enumerate(nums) if v}
    def dotProduct(self, vec):
        return sum(self.data.get(i, 0) * v for i, v in vec.data.items())

# Example usage:
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))  # Output: 8
