"""
LeetCode 737. Sentence Similarity II

Given two sentences words1 and words2, and a list of similar word pairs, determine if two sentences are similar. The similarity relation is transitive.

Example 1:
Input: words1 = ["great","acting","skills"], words2 = ["fine","drama","talent"], pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true

Example 2:
Input: words1 = ["great"], words2 = ["great"], pairs = []
Output: true

Constraints:
- 1 <= words1.length, words2.length <= 1000
- 0 <= pairs.length <= 2000
- 1 <= words1[i], words2[i], pairs[i][j].length <= 20
"""
from typing import List

def areSentencesSimilarTwo(words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
    if len(words1) != len(words2):
        return False
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)
    for a, b in pairs:
        union(a, b)
    for w1, w2 in zip(words1, words2):
        if w1 != w2 and find(w1) != find(w2):
            return False
    return True

# Example usage
if __name__ == "__main__":
    print(areSentencesSimilarTwo(["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))  # Output: True
    print(areSentencesSimilarTwo(["great"], ["great"], []))  # Output: True
