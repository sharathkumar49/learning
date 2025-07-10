"""
LeetCode 1656. Design an Ordered Stream

Design an OrderedStream class that supports the following operations:
- OrderedStream(n): Initializes the stream with n slots.
- insert(idKey, value): Inserts the value at the idKey and returns the largest possible chunk of values in order.

Example 1:
Input: ["OrderedStream","insert","insert","insert","insert","insert"], [[5],[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]
Output: [null,["aaaaa"],["bbbbb","ccccc"],["ddddd","eeeee"]]

Constraints:
- 1 <= n <= 1000
- 1 <= idKey <= n
- value consists of lowercase English letters.
"""

class OrderedStream:
    def __init__(self, n):
        self.stream = ['']*n
        self.ptr = 0
    def insert(self, idKey, value):
        self.stream[idKey-1] = value
        res = []
        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res

# Example usage:
# os = OrderedStream(5)
# print(os.insert(3, "ccccc"))
# print(os.insert(1, "aaaaa"))
# print(os.insert(2, "bbbbb"))
# print(os.insert(5, "eeeee"))
# print(os.insert(4, "ddddd"))
