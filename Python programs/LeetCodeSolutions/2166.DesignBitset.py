"""
LeetCode 2166. Design Bitset

Design a Bitset with the following operations: fix, unfix, flip, all, one, count, toString. Implement the class and its methods as described in the problem statement.

Example:
Input: ["Bitset","fix","fix","flip","all","unfix","flip","one","count","toString"], [[5], [3], [1], [], [], [0], [], [], [], []]
Output: [null,null,null,null,false,null,null,true,2,"01010"]

Constraints:
- 1 <= size <= 10^5
- At most 10^5 calls will be made to Bitset methods.
"""

class Bitset:
    def __init__(self, size):
        self.n = size
        self.bits = [0]*size
        self.flipped = False
        self.count_ones = 0
    def fix(self, idx):
        if self.bits[idx] ^ self.flipped == 0:
            self.bits[idx] ^= 1
            self.count_ones += 1
    def unfix(self, idx):
        if self.bits[idx] ^ self.flipped == 1:
            self.bits[idx] ^= 1
            self.count_ones -= 1
    def flip(self):
        self.flipped ^= 1
        self.count_ones = self.n - self.count_ones
    def all(self):
        return self.count_ones == self.n
    def one(self):
        return self.count_ones > 0
    def count(self):
        return self.count_ones
    def toString(self):
        return ''.join(str(b^self.flipped) for b in self.bits)

# Example usage:
# bs = Bitset(5)
# bs.fix(3)
# bs.fix(1)
# bs.flip()
# print(bs.all())      # False
# bs.unfix(0)
# bs.flip()
# print(bs.one())      # True
# print(bs.count())    # 2
# print(bs.toString()) # "01010"
