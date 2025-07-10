"""
LeetCode 1503. Last Moment Before All Ants Fall Out of a Plank

We have a plank of length n. Some ants are moving left to right, others right to left. Return the last moment when an ant was on the plank.

Constraints:
- 1 <= n <= 10^4
- 1 <= left.length, right.length <= n
- 0 <= left[i] <= n
- 0 <= right[i] <= n

Example:
Input: n = 4, left = [4,3], right = [0,1]
Output: 4
"""
def getLastMoment(n, left, right):
    return max(left+[0]) if right == [] else max(max(left+[0]), n-min(right+[n]))

# Example usage:
n = 4
left = [4,3]
right = [0,1]
print(getLastMoment(n, left, right))  # Output: 4
