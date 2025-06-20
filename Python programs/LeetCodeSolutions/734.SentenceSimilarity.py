"""
LeetCode 734. Sentence Similarity

Given two sentences words1 and words2, and a list of similar word pairs, determine if two sentences are similar.

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

def areSentencesSimilar(words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
    if len(words1) != len(words2):
        return False
    sim = set(map(tuple, pairs))
    for w1, w2 in zip(words1, words2):
        if w1 != w2 and (w1, w2) not in sim and (w2, w1) not in sim:
            return False
    return True

# Example usage
if __name__ == "__main__":
    print(areSentencesSimilar(["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))  # Output: True
    print(areSentencesSimilar(["great"], ["great"], []))  # Output: True
