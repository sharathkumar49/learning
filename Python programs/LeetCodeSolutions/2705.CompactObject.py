"""
LeetCode 2705. Compact Object

Implement a function to remove falsy values from an object recursively.

Constraints:
- 1 <= calls.length <= 10^5
"""

def compactObject(obj):
    if isinstance(obj, list):
        return [compactObject(x) for x in obj if x]
    if isinstance(obj, dict):
        return {k: compactObject(v) for k, v in obj.items() if v}
    return obj
# Example usage:
# print(compactObject({"a":None,"b":[False,1],"c":0}))  # Output: {'b': [1]}
