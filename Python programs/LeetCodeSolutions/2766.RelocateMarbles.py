"""
LeetCode 2766. Relocate Marbles

Given nums and moves, return the final positions of marbles after all moves.

Constraints:
- 1 <= nums.length, moves.length <= 10^5
"""

def relocateMarbles(nums, moves):
    s = set(nums)
    for a, b in moves:
        if a in s:
            s.remove(a)
            s.add(b)
    return sorted(s)
# Example usage:
# print(relocateMarbles([1,2,3],[ [1,4],[2,5] ]))  # Output: [3,4,5]
