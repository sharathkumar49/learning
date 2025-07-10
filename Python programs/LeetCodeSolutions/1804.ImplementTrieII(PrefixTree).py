"""
LeetCode 1804. Implement Trie II (Prefix Tree)

Implement a trie with insert, countWordsEqualTo, countWordsStartingWith, and erase.

Example 1:
Input: ["Trie","insert","insert","countWordsEqualTo","countWordsStartingWith","erase","countWordsEqualTo"], [[],["apple"],["apple"],["apple"],["app"],["apple"],["apple"]]
Output: [null,null,null,2,2,null,1]

Constraints:
- 1 <= calls.length <= 10^4
- 1 <= word.length <= 2000
- word consists of lowercase English letters
"""
class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.prefix = 0
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
            node.prefix += 1
        node.count += 1
    def countWordsEqualTo(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count
    def countWordsStartingWith(self, prefix):
        node = self
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.prefix
    def erase(self, word):
        node = self
        stack = []
        for c in word:
            stack.append((node, c))
            node = node.children[c]
        node.count -= 1
        for parent, c in reversed(stack):
            parent.children[c].prefix -= 1
            if parent.children[c].prefix == 0:
                del parent.children[c]
                break

# Example usage:
# trie = Trie()
# trie.insert("apple")
# trie.insert("apple")
# print(trie.countWordsEqualTo("apple"))  # Output: 2
# print(trie.countWordsStartingWith("app"))  # Output: 2
# trie.erase("apple")
# print(trie.countWordsEqualTo("apple"))  # Output: 1
