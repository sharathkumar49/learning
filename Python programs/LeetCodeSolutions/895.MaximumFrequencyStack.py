"""
895. Maximum Frequency Stack
https://leetcode.com/problems/maximum-frequency-stack/

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
Implement the FreqStack class:
- FreqStack() constructs an empty frequency stack.
- void push(int val) pushes an integer val onto the top of the stack.
- int pop() removes and returns the most frequent element in the stack. If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Constraints:
- 0 <= val <= 10^9
- At most 2 * 10^4 calls will be made to push and pop.

Example:
Input: ["FreqStack","push","push","push","push","push","pop","pop","pop","pop"], [[],[5],[7],[5],[7],[4],[],[],[],[]]
Output: [null,null,null,null,null,null,5,7,5,4]
"""
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val

# Example usage
if __name__ == "__main__":
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(5)
    fs.push(7)
    fs.push(4)
    print(fs.pop())  # Output: 5
    print(fs.pop())  # Output: 7
    print(fs.pop())  # Output: 5
    print(fs.pop())  # Output: 4
