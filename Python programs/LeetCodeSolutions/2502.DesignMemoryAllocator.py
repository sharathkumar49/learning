"""
LeetCode 2502. Design Memory Allocator

Design a memory allocator with allocate and free operations.

Constraints:
- 1 <= n, operations.length <= 10^5
"""
class Allocator:
    def __init__(self, n):
        self.mem = [0]*n
    def allocate(self, size, mID):
        for i in range(len(self.mem)-size+1):
            if all(x==0 for x in self.mem[i:i+size]):
                for j in range(i,i+size):
                    self.mem[j]=mID
                return i
        return -1
    def free(self, mID):
        cnt = 0
        for i in range(len(self.mem)):
            if self.mem[i]==mID:
                self.mem[i]=0
                cnt+=1
        return cnt
# Example usage:
# allocator = Allocator(10)
# print(allocator.allocate(1,1))  # Output: 0
# print(allocator.free(1))        # Output: 1
