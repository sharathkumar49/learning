"""
LeetCode 2007. Find Original Array From Doubled Array

Given an array changed, return the original array if changed is a doubled array, or [] if not possible.

Example:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]

Constraints:
- 1 <= changed.length <= 10^5
- changed.length is even
- 1 <= changed[i] <= 10^5
"""

def findOriginalArray(changed):
    from collections import Counter
    if len(changed) % 2:
        return []
    count = Counter(changed)
    original = []
    for x in sorted(count):
        if count[x] > count[2*x]:
            return []
        for _ in range(count[x]):
            original.append(x)
            count[2*x] -= 1
    return original

# Example usage:
# print(findOriginalArray([1,3,4,2,6,8]))  # Output: [1,3,4]
