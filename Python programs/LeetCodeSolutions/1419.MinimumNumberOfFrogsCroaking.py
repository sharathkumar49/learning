"""
LeetCode 1419. Minimum Number of Frogs Croaking

Given a string croakOfFrogs, which represents a combination of croaks by frogs, return the minimum number of frogs needed to produce the string. If the string is not valid, return -1.

Constraints:
- 1 <= croakOfFrogs.length <= 10^5
- croakOfFrogs consists of the letters 'c', 'r', 'o', 'a', 'k'.

Example:
Input: croakOfFrogs = "croakcroak"
Output: 1
"""
def minNumberOfFrogs(croakOfFrogs):
    from collections import Counter
    idx = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
    cnt = [0]*5
    frogs = res = 0
    for ch in croakOfFrogs:
        i = idx[ch]
        cnt[i] += 1
        if i == 0:
            frogs += 1
            res = max(res, frogs)
        else:
            if cnt[i-1] == 0:
                return -1
            cnt[i-1] -= 1
        if i == 4:
            frogs -= 1
    return res if sum(cnt[:-1]) == 0 else -1

# Example usage:
croakOfFrogs = "croakcroak"
print(minNumberOfFrogs(croakOfFrogs))  # Output: 1
