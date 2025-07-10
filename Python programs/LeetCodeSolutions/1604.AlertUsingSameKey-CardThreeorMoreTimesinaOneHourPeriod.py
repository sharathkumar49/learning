"""
LeetCode 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

Given two string arrays keyName and keyTime, return a list of key card users who used their key card three or more times in a one-hour period. The answer should be returned in lexicographical order.

Example 1:
Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]

Constraints:
- 1 <= keyName.length, keyTime.length <= 10^5
- keyName.length == keyTime.length
- keyTime[i] is in "HH:MM" format.
"""

def alertNames(keyName, keyTime):
    from collections import defaultdict
    times = defaultdict(list)
    for name, t in zip(keyName, keyTime):
        h, m = map(int, t.split(':'))
        times[name].append(h*60 + m)
    res = []
    for name in times:
        t = sorted(times[name])
        for i in range(len(t)-2):
            if t[i+2] - t[i] <= 60:
                res.append(name)
                break
    return sorted(res)

# Example usage:
# keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
# keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# print(alertNames(keyName, keyTime))  # Output: ['daniel']
