"""
1181. Before and After Puzzle

Given a list of phrases, return the list of all pairs of phrases that can be joined by overlapping words (the last word of one is the first word of another). Return the result in lexicographical order.

Constraints:
- 1 <= phrases.length <= 100
- 1 <= phrases[i].length <= 100

Example:
Input: phrases = ["writing code","code rocks"]
Output: ["writing code rocks"]

"""
def beforeAndAfterPuzzles(phrases):
    res = set()
    first = {}
    last = {}
    for p in phrases:
        f = p.split()[0]
        l = p.split()[-1]
        first.setdefault(f, []).append(p)
        last.setdefault(l, []).append(p)
    for l in last:
        if l in first:
            for a in last[l]:
                for b in first[l]:
                    if a != b:
                        res.add(a + b[len(l):])
    return sorted(res)

# Example usage
if __name__ == "__main__":
    print(beforeAndAfterPuzzles(["writing code","code rocks"]))  # Output: ['writing code rocks']
