"""
1096. Brace Expansion II

Given a string expression representing a list of words with braces, return all words possible from the expansion, in lexicographical order.

Constraints:
- 1 <= expression.length <= 50
- expression consists of '{', '}', ',' and lowercase English letters.

Example:
Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
"""
from typing import List

def braceExpansionII(expression: str) -> List[str]:
    def parse(expr):
        stack = [[]]
        i = 0
        while i < len(expr):
            if expr[i] == '{':
                j = i
                bal = 0
                while i < len(expr):
                    if expr[i] == '{': bal += 1
                    if expr[i] == '}': bal -= 1
                    if bal == 0: break
                    i += 1
                stack[-1].append(parse(expr[j+1:i]))
            elif expr[i] == ',':
                stack.append([])
            else:
                j = i
                while i < len(expr) and expr[i].isalpha():
                    i += 1
                stack[-1].append([expr[j:i]])
                i -= 1
            i += 1
        res = set()
        for group in stack:
            temp = ['']
            for part in group:
                temp = [x + y for x in temp for y in part]
            res |= set(temp)
        return sorted(res)
    return parse(expression)

# Example usage:
expression = "{a,b}{c,{d,e}}"
print(braceExpansionII(expression))  # Output: ['ac', 'ad', 'ae', 'bc', 'bd', 'be']
