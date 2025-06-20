"""
212. Word Search II
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- board and words[i] consist of lowercase English letters.
- All the strings of words are unique.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def findWords(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
    m, n = len(board), len(board[0])
    result = []
    def dfs(i, j, node):
        c = board[i][j]
        if c not in node.children:
            return
        next_node = node.children[c]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None
        board[i][j] = '#'
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                dfs(x, y, next_node)
        board[i][j] = c
    for i in range(m):
        for j in range(n):
            dfs(i, j, root)
    return result

# Example usage:
if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(findWords([row[:] for row in board], words))  # Output: ['oath', 'eat']
    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    print(findWords([row[:] for row in board2], words2))  # Output: []
