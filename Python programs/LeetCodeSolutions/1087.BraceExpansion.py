"""
1087. Brace Expansion

Given a string S representing a list of words with braces, return all words possible from the expansion, in lexicographical order.

Constraints:
- 1 <= S.length <= 50
- S consists of '{', '}', ',' and lowercase English letters.

Example:
Input: S = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
"""
from typing import List

def expand(S: str) -> List[str]:
    res = ['']
    i = 0
    while i < len(S):
        if S[i] == '{':
            j = i
            while S[j] != '}':
                j += 1
            options = S[i+1:j].split(',')
            res = [prefix + c for prefix in res for c in sorted(options)]
            i = j + 1
        else:
            res = [prefix + S[i] for prefix in res]
            i += 1
    return res

# Example usage:
S = "{a,b}c{d,e}f"
print(expand(S))  # Output: ['acdf', 'acef', 'bcdf', 'bcef']
