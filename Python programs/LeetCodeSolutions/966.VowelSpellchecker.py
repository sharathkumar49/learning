"""
966. Vowel Spellchecker
https://leetcode.com/problems/vowel-spellchecker/

Given a wordlist, and a list of queries, return the answer for each query. The answer is the first word in the wordlist that matches the query by:
- Exact match
- Case-insensitive match
- Vowel error match (replace all vowels with '*')
If no match, return "".

Constraints:
- 1 <= wordlist.length <= 5000
- 1 <= queries.length <= 5000
- 1 <= wordlist[i].length, queries[i].length <= 7

Example:
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe",""]
"""
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)
        words = set(wordlist)
        lower = {}
        vowel = {}
        for w in wordlist:
            lw = w.lower()
            vw = devowel(lw)
            if lw not in lower:
                lower[lw] = w
            if vw not in vowel:
                vowel[vw] = w
        res = []
        for q in queries:
            if q in words:
                res.append(q)
            elif q.lower() in lower:
                res.append(lower[q.lower()])
            elif devowel(q.lower()) in vowel:
                res.append(vowel[devowel(q.lower())])
            else:
                res.append("")
        return res

# Example usage
if __name__ == "__main__":
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    print(Solution().spellchecker(wordlist, queries))
    # Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe",""]
