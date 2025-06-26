"""
LeetCode 1432. Max Difference You Can Get From Changing an Integer

Given an integer num, return the maximum difference you can get by changing at most two digits (one change for max, one for min).

Constraints:
- 1 <= num <= 10^8

Example:
Input: num = 555
Output: 888
"""
def maxDiff(num):
    s = str(num)
    for d in s:
        if d != '9':
            max_num = int(s.replace(d, '9'))
            break
    else:
        max_num = num
    for d in s:
        if d != '1':
            min_num = int(s.replace(d, '1'))
            break
    else:
        min_num = num
    return max_num - min_num

# Example usage:
num = 555
print(maxDiff(num))  # Output: 888
