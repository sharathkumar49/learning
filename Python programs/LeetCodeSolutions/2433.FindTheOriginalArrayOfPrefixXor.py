"""
LeetCode 2433. Find The Original Array of Prefix Xor

Given a prefix xor array, return the original array.

Constraints:
- 1 <= pref.length <= 10^5
"""

def findArray(pref):
    res = [pref[0]]
    for i in range(1, len(pref)):
        res.append(pref[i]^pref[i-1])
    return res

# Example usage:
# print(findArray([5,2,0,3,1]))  # Output: [5,7,2,3,2]
