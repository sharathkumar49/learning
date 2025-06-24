"""
LeetCode 1429. First Unique Number

Implement the FirstUnique class:
- FirstUnique(int[] nums) initializes the object with the numbers in the queue.
- int showFirstUnique() returns the value of the first unique integer of the queue, and -1 if there is no such integer.
- void add(int value) insert value to the queue.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^8

Example:
Input: [2,3,5], add(5), add(2), add(3), showFirstUnique()
Output: -1
"""
from collections import deque, Counter
class FirstUnique:
    def __init__(self, nums):
        self.q = deque()
        self.count = Counter()
        for n in nums:
            self.add(n)
    def showFirstUnique(self):
        while self.q and self.count[self.q[0]] > 1:
            self.q.popleft()
        return self.q[0] if self.q else -1
    def add(self, value):
        self.count[value] += 1
        if self.count[value] == 1:
            self.q.append(value)

# Example usage:
firstUnique = FirstUnique([2,3,5])
print(firstUnique.showFirstUnique())  # Output: 2
firstUnique.add(5)
print(firstUnique.showFirstUnique())  # Output: 2
firstUnique.add(2)
print(firstUnique.showFirstUnique())  # Output: 3
firstUnique.add(3)
print(firstUnique.showFirstUnique())  # Output: -1
