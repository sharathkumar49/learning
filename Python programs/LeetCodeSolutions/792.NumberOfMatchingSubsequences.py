"""
792. Number of Matching Subsequences

Given a string s and an array of strings words, return the number of words that are subsequences of s.

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:
- 1 <= s.length <= 5 * 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 50
- s and words[i] consist of only lowercase English letters.
"""
def numMatchingSubseq(s, words):
    from collections import defaultdict, deque
    waiting = defaultdict(deque)
    for w in words:
        waiting[w[0]].append(iter(w[1:]))
    count = 0
    for c in s:
        for _ in range(len(waiting[c])):
            it = waiting[c].popleft()
            nxt = next(it, None)
            if nxt:
                waiting[nxt].append(it)
            else:
                count += 1
    return count

# Example usage:
print(numMatchingSubseq("abcde", ["a","bb","acd","ace"]))  # Output: 3
print(numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))  # Output: 2
