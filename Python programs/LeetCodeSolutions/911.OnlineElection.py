"""
911. Online Election
https://leetcode.com/problems/online-election/

You are given two integer arrays persons and times. On the ith vote at time times[i], the person persons[i] was leading in the election. For each query at a time t, return the person who was leading at time t.
Implement the TopVotedCandidate class:
- TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
- int q(int t) Returns the number of the person who was leading the election at time t.

Constraints:
- 1 <= persons.length <= 5000
- times is a strictly increasing array with length persons.length.
- 0 <= persons[i] < persons.length
- 0 <= times[i] <= 10^9
- times[0] <= t <= 10^9
- At most 10^4 calls will be made to q.

Example:
Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
"""
from bisect import bisect_right
from typing import List

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        self.times = times
        count = {}
        leader = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if leader == -1 or count[p] >= count[leader]:
                leader = p
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        i = bisect_right(self.times, t) - 1
        return self.leaders[i]

# Example usage
if __name__ == "__main__":
    persons = [0,1,1,0,0,1,0]
    times = [0,5,10,15,20,25,30]
    tvc = TopVotedCandidate(persons, times)
    print(tvc.q(3))   # Output: 0
    print(tvc.q(12))  # Output: 1
    print(tvc.q(25))  # Output: 1
    print(tvc.q(15))  # Output: 0
    print(tvc.q(24))  # Output: 0
    print(tvc.q(8))   # Output: 1
