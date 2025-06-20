"""
281. Zigzag Iterator
https://leetcode.com/problems/zigzag-iterator/

Given two 1d vectors, implement an iterator to return their elements alternately.

Constraints:
- 1 <= v1.length, v2.length <= 1000

Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
"""
class ZigzagIterator:
    def __init__(self, v1, v2):
        self.queue = []
        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))
    def next(self):
        if not self.hasNext():
            raise Exception('No more elements')
        it = self.queue.pop(0)
        val = next(it)
        if any(True for _ in [it]):
            self.queue.append(it)
        return val
    def hasNext(self):
        return bool(self.queue)

# Example usage:
if __name__ == "__main__":
    v1 = [1,2]
    v2 = [3,4,5,6]
    it = ZigzagIterator(v1, v2)
    res = []
    while it.hasNext():
        res.append(it.next())
    print(res)  # Output: [1,3,2,4,5,6]
