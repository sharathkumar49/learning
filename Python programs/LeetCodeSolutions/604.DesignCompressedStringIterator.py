"""
604. Design Compressed String Iterator
Difficulty: Easy

Design and implement a data structure for a compressed string iterator. It should support the following operations:
- next(): Returns the next character in the uncompressed string, or a space if there is no uncompressed character left.
- hasNext(): Returns true if there is a next character in the uncompressed string, or false otherwise.

Example:
Input: "L1e2t1C1o1d1e1"
Output: ["L","e","e","t","C","o","d","e"]

Constraints:
1 <= S.length <= 100
S contains only lowercase letters and digits.
"""

class StringIterator:
    def __init__(self, compressedString: str):
        import re
        self.chunks = re.findall(r'([a-zA-Z])(\d+)', compressedString)
        self.idx = 0
        self.count = 0
    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.count == 0:
            self.char, cnt = self.chunks[self.idx]
            self.count = int(cnt)
            self.idx += 1
        self.count -= 1
        return self.char
    def hasNext(self) -> bool:
        return self.count > 0 or self.idx < len(self.chunks)

# Example usage
# it = StringIterator("L1e2t1C1o1d1e1")
# while it.hasNext():
#     print(it.next(), end='')  # Output: LeetCode
