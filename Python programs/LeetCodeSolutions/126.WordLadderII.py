"""
126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/

Given two words, beginWord and endWord, and a dictionary's word list, return all the shortest transformation sequence(s) from beginWord to endWord, such that:
- Only one letter can be changed at a time
- Each transformed word must exist in the word list

Constraints:
- 1 <= beginWord.length <= 5
- endWord.length == beginWord.length
- 1 <= wordList.length <= 500
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters
- beginWord != endWord

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
"""
from typing import List
from collections import defaultdict, deque

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []
    layer = {}
    layer[beginWord] = [[beginWord]]
    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == endWord:
                return layer[word]
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]
        wordSet -= set(new_layer.keys())
        layer = new_layer
    return []

# Example usage:
if __name__ == "__main__":
    print(findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    # Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
