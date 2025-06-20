"""
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/

There is a new alien language that uses the English alphabet. However, the order among letters is unknown to you. You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language. If the order is invalid, return "".

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
"""
def alienOrder(words):
    from collections import defaultdict, deque
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""
        for a, b in zip(w1, w2):
            if a != b:
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1
                break
    queue = deque([c for c in indegree if indegree[c] == 0])
    res = []
    while queue:
        c = queue.popleft()
        res.append(c)
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return ''.join(res) if len(res) == len(indegree) else ''

# Example usage:
if __name__ == "__main__":
    print(alienOrder(["wrt","wrf","er","ett","rftt"]))  # Output: "wertf"
    print(alienOrder(["z","x"]))                            # Output: "zx"
    print(alienOrder(["z","x","z"]))                      # Output: ""
