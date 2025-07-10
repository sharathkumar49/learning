"""
LeetCode 1578. Minimum Time to Make Rope Colorful

Alice has n balloons arranged on a rope. Each balloon is colored by a character from the string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. The time needed to remove the ith balloon is given by the integer neededTime[i].

Return the minimum time Bob needs to make the rope colorful.

Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: Remove the balloons at indices 2 and 4. Total time = 3 + 0 = 3.

Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful.

Constraints:
- n == colors.length == neededTime.length
- 1 <= n <= 10^5
- 1 <= neededTime[i] <= 10^4
- colors contains only lowercase English letters.
"""

def minCost(colors, neededTime):
    res = 0
    for i in range(1, len(colors)):
        if colors[i] == colors[i-1]:
            res += min(neededTime[i], neededTime[i-1])
            neededTime[i] = max(neededTime[i], neededTime[i-1])
    return res

# Example usage:
# colors = "abaac"
# neededTime = [1,2,3,4,5]
# print(minCost(colors, neededTime))  # Output: 3
