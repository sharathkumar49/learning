"""
267. Palindrome Permutation II
https://leetcode.com/problems/palindrome-permutation-ii/

Given a string s, return all the palindromic permutations (without duplicates) of it. You may return the answer in any order. If no palindromic permutation exists, return an empty list.

Constraints:
- 1 <= s.length <= 16
- s consists of only lowercase English letters.

Example 1:
Input: s = "aabb"
Output: ["abba","baab"]

Example 2:
Input: s = "abc"
Output: []
"""
def generatePalindromes(s):
    from collections import Counter
    def backtrack(path, counter):
        if len(path) == half_len:
            half = ''.join(path)
            res.append(half + mid + half[::-1])
            return
        for c in counter:
            if counter[c] > 0:
                counter[c] -= 1
                path.append(c)
                backtrack(path, counter)
                path.pop()
                counter[c] += 1
    count = Counter(s)
    mid = ''
    odd = 0
    for c in count:
        if count[c] % 2:
            mid += c
            odd += 1
    if odd > 1:
        return []
    half = []
    for c in count:
        half += [c] * (count[c] // 2)
    res = []
    half_len = len(half)
    backtrack([], Counter(half))
    return list(set(res))

# Example usage:
if __name__ == "__main__":
    print(sorted(generatePalindromes("aabb")))  # Output: ['abba', 'baab']
    print(generatePalindromes("abc"))           # Output: []
