"""
1032. Stream of Characters

Implement the StreamChecker class, which receives a list of words and checks if the stream of characters queried so far forms any word in the list as a suffix.

Constraints:
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 2000
- All words[i] consist of lowercase English letters.
- 1 <= queries.length <= 40000
- queries[i] is a single lowercase English letter.

Example:
Input: ["cd","f","kl"], queries = ['a','b','c','d','e','f','g','h','i','j','k','l']
Output: [false,false,false,true,false,true,false,false,false,false,true,true]
"""
from collections import deque

class StreamChecker:
    def __init__(self, words):
        self.trie = {}
        self.maxlen = 0
        for word in words:
            node = self.trie
            for c in word[::-1]:
                node = node.setdefault(c, {})
            node['#'] = True
            self.maxlen = max(self.maxlen, len(word))
        self.stream = deque()

    def query(self, letter):
        self.stream.appendleft(letter)
        if len(self.stream) > self.maxlen:
            self.stream.pop()
        node = self.trie
        for c in self.stream:
            if c in node:
                node = node[c]
                if '#' in node:
                    return True
            else:
                break
        return False

# Example usage:
words = ["cd","f","kl"]
streamChecker = StreamChecker(words)
queries = ['a','b','c','d','e','f','g','h','i','j','k','l']
print([streamChecker.query(q) for q in queries])  # Output: [False, False, False, True, False, True, False, False, False, False, True, True]
