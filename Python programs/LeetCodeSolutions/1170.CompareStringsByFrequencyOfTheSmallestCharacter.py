"""
1170. Compare Strings by Frequency of the Smallest Character

Given two string arrays queries and words, for each query, return the number of words such that f(query) < f(word), where f(s) is the frequency of the smallest character in s.

Constraints:
- 1 <= queries.length <= 2000
- 1 <= words.length <= 2000
- 1 <= queries[i].length, words[i].length <= 10

Example:
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]

"""
def numSmallerByFrequency(queries, words):
    def f(s):
        return s.count(min(s))
    w = sorted([f(word) for word in words])
    res = []
    for q in queries:
        fq = f(q)
        l, r = 0, len(w)
        while l < r:
            m = (l + r) // 2
            if w[m] <= fq:
                l = m + 1
            else:
                r = m
        res.append(len(w) - l)
    return res

# Example usage
if __name__ == "__main__":
    print(numSmallerByFrequency(["cbd"], ["zaaaz"]))  # Output: [1]
