"""
315. Count of Smaller Numbers After Self

Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        arr = list(enumerate(nums))
        def merge_sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])
                m, n = len(left), len(right)
                i = j = 0
                merged = []
                while i < m or j < n:
                    if j == n or (i < m and left[i][1] <= right[j][1]):
                        res[left[i][0]] += j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                return merged
            else:
                return enum
        merge_sort(arr)
        return res

# Example usage:
nums = [5,2,6,1]
print(Solution().countSmaller(nums))  # Output: [2,1,1,0]
