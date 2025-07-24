"""
LeetCode 2628. JSON Deep Equal

Implement a function to check deep equality of two JSON-like objects.

Constraints:
- 1 <= calls.length <= 10^5
"""

def jsonDeepEqual(a, b):
    if type(a) != type(b): return False
    if isinstance(a, dict):
        if a.keys() != b.keys(): return False
        return all(jsonDeepEqual(a[k], b[k]) for k in a)
    if isinstance(a, list):
        if len(a) != len(b): return False
        return all(jsonDeepEqual(x, y) for x, y in zip(a, b))
    return a == b
# Example usage:
# print(jsonDeepEqual({"a":1,"b":[2,3]}, {"a":1,"b":[2,3]}))  # Output: True
