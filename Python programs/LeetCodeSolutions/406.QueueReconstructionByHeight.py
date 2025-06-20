"""
406. Queue Reconstruction by Height

You are given an array of people, people[i] = [hi, ki], representing the height of the ith person and the number of people in front who have a height greater than or equal to hi. Reconstruct and return the queue that is represented by the input array.

Constraints:
- 1 <= people.length <= 2000
- 0 <= hi <= 10^6
- 0 <= ki < people.length
"""
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

# Example usage:
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))  # Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
