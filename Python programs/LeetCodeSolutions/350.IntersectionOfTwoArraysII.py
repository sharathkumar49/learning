# 350. Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

def intersect(nums1, nums2):
    from collections import Counter
    c1, c2 = Counter(nums1), Counter(nums2)
    res = []
    for num in c1:
        if num in c2:
            res.extend([num] * min(c1[num], c2[num]))
    return res

# Example usage
nums1 = [1,2,2,1]
nums2 = [2,2]
print("Intersection:", intersect(nums1, nums2))  # Output: [2,2]
