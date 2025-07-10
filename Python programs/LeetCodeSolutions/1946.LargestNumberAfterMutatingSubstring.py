"""
LeetCode 1946. Largest Number After Mutating Substring

Given a string num and an integer array change, return the largest string after mutating a substring.

Example:
Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
Output: "832"

Constraints:
- 1 <= num.length <= 10^5
- num consists of digits only.
- change.length == 10
- 0 <= change[i] <= 9
"""

def maximumNumber(num, change):
    num = list(num)
    i = 0
    while i < len(num) and int(num[i]) >= change[int(num[i])]:
        i += 1
    while i < len(num) and int(num[i]) <= change[int(num[i])]:
        num[i] = str(change[int(num[i])])
        i += 1
    return ''.join(num)

# Example usage:
# print(maximumNumber("132", [9,8,5,0,3,6,4,2,6,8]))  # Output: "832"
