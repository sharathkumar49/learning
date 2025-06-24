"""
1172. Dinner Plate Stacks

Implement a DinnerPlates class that simulates stacks of plates. Each stack has a fixed capacity. Support push, pop, and popAtStack operations efficiently.

Constraints:
- 1 <= capacity <= 20000
- At most 2 * 10^5 operations will be performed.

Example:
Input: ["DinnerPlates","push","push","push","popAtStack","pop","pop"], [[2],[1],[2],[3],[1],[],[]]
Output: [null,null,null,null,2,3,1]

"""
import heapq
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []
    def push(self, val: int) -> None:
        while self.available and self.available[0] < len(self.stacks) and len(self.stacks[self.available[0]]) == self.capacity:
            heapq.heappop(self.available)
        if not self.available:
            self.stacks.append([])
            idx = len(self.stacks) - 1
        else:
            idx = self.available[0]
        self.stacks[idx].append(val)
        if len(self.stacks[idx]) < self.capacity:
            heapq.heappush(self.available, idx)
    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        if len(self.stacks[-1]) < self.capacity:
            heapq.heappush(self.available, len(self.stacks) - 1)
        return val
    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            val = self.stacks[index].pop()
            heapq.heappush(self.available, index)
            return val
        return -1

# Example usage
if __name__ == "__main__":
    dp = DinnerPlates(2)
    dp.push(1)
    dp.push(2)
    dp.push(3)
    print(dp.popAtStack(1))  # Output: 2
    print(dp.pop())          # Output: 3
    print(dp.pop())          # Output: 1
