"""
LeetCode 2158. Amount of New Area Painted Each Day

You are given a list of intervals representing the area painted each day. Return an array where the i-th element is the amount of new area painted on the i-th day.

Example:
Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]

Constraints:
- 1 <= paint.length <= 10^5
- 1 <= paint[i][0] < paint[i][1] <= 5 * 10^4
"""

def amountPainted(paint):
    res = []
    painted = {}
    for start, end in paint:
        i = start
        new = 0
        while i < end:
            nxt = painted.get(i, i)
            if nxt >= end:
                break
            new += 1
            painted[i] = end
            i += 1
        res.append(new)
    return res

# Example usage:
# print(amountPainted([[1,4],[4,7],[5,8]]))  # Output: [3,3,1]
