"""
LeetCode 1964. Find the Longest Valid Obstacle Course at Each Position

Given an array obstacles, return an array where answer[i] is the length of the longest valid obstacle course ending at position i.

Example:
Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]

Constraints:
- 1 <= obstacles.length <= 10^5
- 1 <= obstacles[i] <= 10^7
"""

def longestObstacleCourseAtEachPosition(obstacles):
    import bisect
    res = []
    dp = []
    for x in obstacles:
        i = bisect.bisect_right(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
        res.append(i+1)
    return res

# Example usage:
# print(longestObstacleCourseAtEachPosition([1,2,3,2]))  # Output: [1,2,3,3]
