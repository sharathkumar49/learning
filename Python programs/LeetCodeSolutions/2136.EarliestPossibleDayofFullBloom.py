"""
LeetCode 2136. Earliest Possible Day of Full Bloom

Given plantTime and growTime for n seeds, return the earliest day all seeds are in full bloom.

Example:
Input: plantTime = [1,4,3], growTime = [2,3,1]
Output: 9

Constraints:
- 1 <= plantTime.length == growTime.length <= 10^5
- 1 <= plantTime[i], growTime[i] <= 10^5
"""

def earliestFullBloom(plantTime, growTime):
    seeds = sorted(zip(growTime, plantTime), reverse=True)
    res = curr = 0
    for g, p in seeds:
        curr += p
        res = max(res, curr + g)
    return res

# Example usage:
# print(earliestFullBloom([1,4,3], [2,3,1]))  # Output: 9
