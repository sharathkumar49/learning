"""
LeetCode 2722. Join Two Arrays by ID

Given two arrays of objects, join them by id.

Constraints:
- 1 <= arr1.length, arr2.length <= 10^5
"""

def join(arr1, arr2):
    d = {x['id']: x for x in arr1}
    for x in arr2:
        if x['id'] in d:
            d[x['id']].update(x)
        else:
            d[x['id']] = x
    return sorted(d.values(), key=lambda x: x['id'])
# Example usage:
# print(join([{"id":1,"x":2},{"id":2,"x":3}], [{"id":2,"y":4}]))  # Output: [{"id":1,"x":2},{"id":2,"x":3,"y":4}]
