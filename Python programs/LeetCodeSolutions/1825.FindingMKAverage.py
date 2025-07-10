"""
LeetCode 1825. Finding MK Average

Design a data structure to calculate the MK Average as described in the problem.

Example 1:
Input: ["MKAverage","addElement","addElement","addElement","calculateMKAverage"], [[3,1],[3],[1],[10],[]]
Output: [null,null,null,3]

Constraints:
- 3 <= m <= 10^5
- 1 <= k*2 < m
- 1 <= num <= 10^5
- At most 10^5 calls will be made to addElement and calculateMKAverage
"""
# This is a complex data structure problem. Below is a simplified version for small m.
class MKAverage:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.q = []
    def addElement(self, num):
        self.q.append(num)
        if len(self.q) > self.m:
            self.q.pop(0)
    def calculateMKAverage(self):
        if len(self.q) < self.m:
            return -1
        arr = sorted(self.q)
        return sum(arr[self.k:-self.k]) // (self.m - 2*self.k)

# Example usage:
# mk = MKAverage(3, 1)
# mk.addElement(3)
# mk.addElement(1)
# mk.addElement(10)
# print(mk.calculateMKAverage())  # Output: 3
