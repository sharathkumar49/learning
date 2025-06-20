"""
659. Split Array into Consecutive Subsequences
Difficulty: Medium

Given an array nums sorted in ascending order, return true if it can be split into one or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:
Input: nums = [1,2,3,3,4,5]
Output: true

Example 2:
Input: nums = [1,2,3,3,4,4,5,5]
Output: true

Constraints:
1 <= nums.length <= 10000
-1000 <= nums[i] <= 1000
"""

def isPossible(nums):
    from collections import Counter, defaultdict
    count = Counter(nums)
    end = defaultdict(int)
    for x in nums:
        if count[x] == 0:
            continue
        if end[x-1] > 0:
            end[x-1] -= 1
            end[x] += 1
        elif count[x+1] > 0 and count[x+2] > 0:
            count[x+1] -= 1
            count[x+2] -= 1
            end[x+2] += 1
        else:
            return False
        count[x] -= 1
    return True

# Example usage
if __name__ == "__main__":
    print(isPossible([1,2,3,3,4,5]))        # Output: True
    print(isPossible([1,2,3,3,4,4,5,5]))    # Output: True
