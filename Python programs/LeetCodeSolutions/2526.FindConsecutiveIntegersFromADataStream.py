"""
LeetCode 2526. Find Consecutive Integers From a Data Stream

Design a class to find consecutive integers from a data stream.

Constraints:
- 1 <= value, k <= 10^5
"""
class DataStream:
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.cnt = 0
    def consec(self, num):
        if num == self.value:
            self.cnt += 1
        else:
            self.cnt = 0
        return self.cnt >= self.k
# Example usage:
# ds = DataStream(4,3)
# print(ds.consec(4))  # Output: False
# print(ds.consec(4))  # Output: False
# print(ds.consec(4))  # Output: True
