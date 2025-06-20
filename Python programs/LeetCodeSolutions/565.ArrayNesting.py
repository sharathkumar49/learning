"""
565. Array Nesting
Difficulty: Medium

You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].
You should build a set s[k] = {nums[k], nums[nums[k]], ... } subjected to the rule: the next element always refers to the value of the previous element.
Return the size of the largest set s[k] formed.

Example 1:
Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: s[0] = {5,6,2,0}

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] < nums.length
All the values of nums are unique.
"""

def arrayNesting(nums):
    visited = [False] * len(nums)
    res = 0
    for i in range(len(nums)):
        if not visited[i]:
            start, count = i, 0
            while not visited[start]:
                visited[start] = True
                start = nums[start]
                count += 1
            res = max(res, count)
    return res

# Example usage
if __name__ == "__main__":
    print(arrayNesting([5,4,0,3,1,6,2]))  # Output: 4
