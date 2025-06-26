# Microsoft: Find the Word Ladder Length
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord.
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, length+1))
    return 0

if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]
    print(ladder_length(begin, end, word_list))  # Output: 5
    begin2 = "hit"
    end2 = "cog"
    word_list2 = ["hot","dot","dog","lot","log"]
    print(ladder_length(begin2, end2, word_list2))  # Output: 0
