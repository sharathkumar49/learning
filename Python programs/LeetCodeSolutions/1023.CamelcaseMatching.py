"""
1023. Camelcase Matching

Given an array of queries and a pattern, return a boolean array where each element is true if the query matches the pattern.

A query matches the pattern if we can insert lowercase letters into the pattern to get the query.

Constraints:
- 1 <= queries.length <= 100
- 1 <= queries[i].length, pattern.length <= 100

Example:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
"""
from typing import List

def camelMatch(queries: List[str], pattern: str) -> List[bool]:
    def match(query):
        i = 0
        for c in query:
            if i < len(pattern) and c == pattern[i]:
                i += 1
            elif c.isupper():
                return False
        return i == len(pattern)
    return [match(q) for q in queries]

# Example usage:
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
print(camelMatch(queries, pattern))  # Output: [True, False, True, True, False]
