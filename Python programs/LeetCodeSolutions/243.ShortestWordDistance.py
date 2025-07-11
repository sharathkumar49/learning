"""
243. Shortest Word Distance
https://leetcode.com/problems/shortest-word-distance/

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Constraints:
- 2 <= wordsDict.length <= 3 * 10^4
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.
- word1 != word2

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
"""
def shortestDistance(wordsDict, word1, word2):
    idx1 = idx2 = -1
    min_dist = float('inf')
    for i, word in enumerate(wordsDict):
        if word == word1:
            idx1 = i
        elif word == word2:
            idx2 = i
        if idx1 != -1 and idx2 != -1:
            min_dist = min(min_dist, abs(idx1 - idx2))
    return min_dist

# Example usage:
if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print(shortestDistance(words, "coding", "practice"))  # Output: 3
    print(shortestDistance(words, "makes", "coding"))     # Output: 1
