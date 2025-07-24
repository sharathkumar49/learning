"""
LeetCode 2633. Convert Object to JSON String

Implement a function to convert an object to a JSON string.

Constraints:
- 1 <= calls.length <= 10^5
"""
import json
def toJSONString(obj):
    return json.dumps(obj)
# Example usage:
# print(toJSONString({"a":1,"b":[2,3]}))  # Output: '{"a": 1, "b": [2, 3]}'
