"""
LeetCode 756. Pyramid Transition Matrix

You are stacking blocks to form a pyramid. Each block has a color, and the colors are represented by a single letter. You are given a bottom row of blocks and a list of allowed triples, where allowed[i] = "ABC" means that if you have blocks A and B on the bottom, you can place C on top of them.
Return true if you can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true

Example 2:
Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false

Constraints:
- 2 <= bottom.length <= 6
- 0 <= allowed.length <= 200
- allowed[i].length == 3
- The letters in all strings are from the set {'A','B','C','D','E','F','G'}
"""
from typing import List
from collections import defaultdict

def pyramidTransition(bottom: str, allowed: List[str]) -> bool:
    d = defaultdict(list)
    for a, b, c in allowed:
        d[a+b].append(c)
    def dfs(row):
        if len(row) == 1:
            return True
        for i in range(len(row)-1):
            if row[i:i+2] not in d:
                return False
        def build(next_row, i):
            if i == len(row)-1:
                return dfs(next_row)
            for c in d[row[i:i+2]]:
                if build(next_row+c, i+1):
                    return True
            return False
        return build('', 0)
    return dfs(bottom)

# Example usage
if __name__ == "__main__":
    print(pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"]))  # Output: True
    print(pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"]))  # Output: False
