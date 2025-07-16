"""
LeetCode 2452. Words Within Two Edits of Dictionary

Given a list of queries and a dictionary, return the queries within two edits of any dictionary word.

Constraints:
- 1 <= queries.length, dictionary.length <= 100
- 1 <= queries[i].length == dictionary[j].length <= 100
"""

def twoEditWords(queries, dictionary):
    res = []
    for q in queries:
        for d in dictionary:
            if sum(a!=b for a,b in zip(q,d)) <= 2:
                res.append(q)
                break
    return res

# Example usage:
# print(twoEditWords(["word","note","ants"],["wood","joke","moat"]))  # Output: ["word","note"]
