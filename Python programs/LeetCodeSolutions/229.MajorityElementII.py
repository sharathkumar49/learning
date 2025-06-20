"""
229. Majority Element II
https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]
"""
def majorityElement(nums):
    if not nums:
        return []
    count1 = count2 = 0
    candidate1 = candidate2 = None
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums)//3]

# Example usage:
if __name__ == "__main__":
    print(majorityElement([3,2,3]))      # Output: [3]
    print(majorityElement([1]))          # Output: [1]
    print(majorityElement([1,2]))        # Output: [1,2]
