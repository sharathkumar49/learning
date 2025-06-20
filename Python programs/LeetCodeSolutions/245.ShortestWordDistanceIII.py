"""
245. Shortest Word Distance III
https://leetcode.com/problems/shortest-word-distance-iii/

Given an array of strings wordsDict, and two strings word1 and word2, return the shortest distance between these two words in the list. Note that word1 and word2 may be the same.

Constraints:
- 1 <= wordsDict.length <= 3 * 10^4
- 1 <= wordsDict[i].length <= 10
- wordsDict[i] consists of lowercase English letters.
- word1 and word2 are in wordsDict.

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3
"""
def shortestWordDistance(wordsDict, word1, word2):
    min_dist = float('inf')
    idx1 = idx2 = -1
    same = word1 == word2
    for i, word in enumerate(wordsDict):
        if word == word1:
            if same:
                if idx1 != -1:
                    min_dist = min(min_dist, i - idx1)
                idx1 = i
            else:
                idx1 = i
        elif word == word2:
            idx2 = i
        if idx1 != -1 and idx2 != -1 and not same:
            min_dist = min(min_dist, abs(idx1 - idx2))
    return min_dist

# Example usage:
if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print(shortestWordDistance(words, "makes", "coding"))  # Output: 1
    print(shortestWordDistance(words, "makes", "makes"))   # Output: 3
