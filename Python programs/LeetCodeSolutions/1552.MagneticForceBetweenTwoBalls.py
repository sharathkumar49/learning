"""
LeetCode 1552. Magnetic Force Between Two Balls

Given an array position and an integer m, return the largest minimum magnetic force between any two balls placed in the baskets.

Constraints:
- 2 <= position.length <= 10^5
- 1 <= position[i] <= 10^9
- 2 <= m <= position.length

Example:
Input: position = [1,2,3,4,7], m = 3
Output: 3
"""
def maxDistance(position, m):
    position.sort()
    def can(d):
        cnt, prev = 1, position[0]
        for x in position[1:]:
            if x - prev >= d:
                cnt += 1
                prev = x
        return cnt >= m
    l, r = 1, position[-1] - position[0]
    while l < r:
        mid = (l + r + 1) // 2
        if can(mid):
            l = mid
        else:
            r = mid - 1
    return l

# Example usage:
position = [1,2,3,4,7]
m = 3
print(maxDistance(position, m))  # Output: 3
