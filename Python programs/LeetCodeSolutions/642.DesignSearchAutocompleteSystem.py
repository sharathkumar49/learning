"""
642. Design Search Autocomplete System
Difficulty: Hard

Design a search autocomplete system for a search engine. Implement the AutocompleteSystem class:
- AutocompleteSystem(sentences, times): Initializes the system with the given sentences and their corresponding times.
- input(c): Processes the next character of the input and returns the top 3 historical hot sentences that have the prefix the user has typed so far.

Example:
Input: ["AutocompleteSystem","input","input","input","input"]
[[["i love you","island","ironman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"]]
Output: [null,["i love you","island","i love leetcode"],["i love you"],["i love you"],[]]

Constraints:
1 <= sentences.length <= 100
1 <= sentences[i].length <= 100
1 <= times[i] <= 50
"""

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = {}
        self.counts = {}
        self.prefix = ''
        for s, t in zip(sentences, times):
            self.counts[s] = t
            node = self.trie
            for c in s:
                node = node.setdefault(c, {})
            node['#'] = s
    def input(self, c):
        if c == '#':
            self.counts[self.prefix] = self.counts.get(self.prefix, 0) + 1
            node = self.trie
            for ch in self.prefix:
                node = node.setdefault(ch, {})
            node['#'] = self.prefix
            self.prefix = ''
            return []
        self.prefix += c
        node = self.trie
        for ch in self.prefix:
            if ch not in node:
                return []
            node = node[ch]
        res = []
        def dfs(n):
            for k, v in n.items():
                if k == '#':
                    res.append(v)
                else:
                    dfs(v)
        dfs(node)
        res.sort(key=lambda x: (-self.counts[x], x))
        return res[:3]

# Example usage
# ac = AutocompleteSystem(["i love you","island","ironman","i love leetcode"],[5,3,2,2])
# print(ac.input('i'))  # ["i love you","island","i love leetcode"]
# print(ac.input(' '))  # ["i love you"]
# print(ac.input('a'))  # ["i love you"]
# print(ac.input('#'))  # []
