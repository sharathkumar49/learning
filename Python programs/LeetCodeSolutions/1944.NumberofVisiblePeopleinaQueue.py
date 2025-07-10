"""
LeetCode 1944. Number of Visible People in a Queue

Given an array heights, return an array where answer[i] is the number of people visible to the right of the i-th person.

Example:
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]

Constraints:
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^6
"""

def canSeePersonsCount(heights):
    res = [0]*len(heights)
    stack = []
    for i in range(len(heights)-1, -1, -1):
        while stack and heights[i] > stack[-1]:
            stack.pop()
            res[i] += 1
        if stack:
            res[i] += 1
        stack.append(heights[i])
    return res

# Example usage:
# print(canSeePersonsCount([10,6,8,5,11,9]))  # Output: [3,1,2,1,1,0]
