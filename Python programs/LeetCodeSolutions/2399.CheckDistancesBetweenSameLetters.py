"""
LeetCode 2399. Check Distances Between Same Letters

Given a string and distances, check if the distances between same letters are correct.

Constraints:
- 1 <= s.length == 26
- distances.length == 26
"""

def checkDistances(s, distance):
    for i, c in enumerate(s):
        idx = ord(c)-ord('a')
        if s.find(c) != i:
            if i - s.find(c) - 1 != distance[idx]:
                return False
    return True

# Example usage:
# print(checkDistances("abac", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))  # Output: True
