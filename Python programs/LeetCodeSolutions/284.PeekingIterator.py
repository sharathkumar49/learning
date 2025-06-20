"""
284. Peeking Iterator
https://leetcode.com/problems/peeking-iterator/

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Constraints:
- 1 <= nums.length <= 1000

Example:
Input: [1,2,3]
Output: [1,2,3]
"""
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._peek = next(self.iterator, None)
    def peek(self):
        return self._peek
    def next(self):
        val = self._peek
        self._peek = next(self.iterator, None)
        return val
    def hasNext(self):
        return self._peek is not None

# Example usage:
if __name__ == "__main__":
    nums = [1,2,3]
    it = PeekingIterator(iter(nums))
    res = []
    while it.hasNext():
        res.append(it.peek())
        res.append(it.next())
    print(res)  # Output: [1,1,2,2,3,3]
