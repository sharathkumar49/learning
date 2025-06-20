"""
244. Shortest Word Distance II
https://leetcode.com/problems/shortest-word-distance-ii/

Design a class that receives a list of words and implements a method that returns the shortest distance between two different words (word1 and word2).

Constraints:
- 2 <= wordsDict.length <= 3 * 10^4
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.
- word1 != word2
- At most 5000 calls will be made to shortest.

Example 1:
Input
["WordDistance","shortest","shortest"]
[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]
Output
[null,3,1]
"""
class WordDistance:
    def __init__(self, wordsDict):
        self.idx = {}
        for i, word in enumerate(wordsDict):
            if word not in self.idx:
                self.idx[word] = []
            self.idx[word].append(i)
    def shortest(self, word1, word2):
        l1, l2 = self.idx[word1], self.idx[word2]
        i = j = 0
        min_dist = float('inf')
        while i < len(l1) and j < len(l2):
            min_dist = min(min_dist, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return min_dist

# Example usage:
if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    wd = WordDistance(words)
    print(wd.shortest("coding", "practice"))  # Output: 3
    print(wd.shortest("makes", "coding"))     # Output: 1
