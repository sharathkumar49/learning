"""
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/

You are given a sorted unique integer array nums.
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Constraints:
- 0 <= nums.length <= 20
- -2^31 <= nums[i] <= 2^31 - 1

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""
def summaryRanges(nums):
    res = []
    i = 0
    while i < len(nums):
        start = i
        while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
            i += 1
        if start == i:
            res.append(str(nums[i]))
        else:
            res.append(f"{nums[start]}->{nums[i]}")
        i += 1
    return res

# Example usage:
if __name__ == "__main__":
    print(summaryRanges([0,1,2,4,5,7]))      # Output: ['0->2','4->5','7']
    print(summaryRanges([0,2,3,4,6,8,9]))   # Output: ['0','2->4','6','8->9']
