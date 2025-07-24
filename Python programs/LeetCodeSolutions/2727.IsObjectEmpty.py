"""
LeetCode 2727. Is Object Empty

Implement a function to check if an object is empty.

Constraints:
- 1 <= calls.length <= 10^5
"""

def isEmpty(obj):
    if isinstance(obj, dict):
        return len(obj) == 0
    if isinstance(obj, list):
        return len(obj) == 0
    return not obj
# Example usage:
# print(isEmpty({}))  # Output: True
# print(isEmpty([]))  # Output: True
# print(isEmpty({"a":1}))  # Output: False
