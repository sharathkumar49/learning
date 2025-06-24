"""
1258. Synonymous Sentences

Given a list of synonym pairs and a sentence, return all possible synonymous sentences sorted lexicographically.

Constraints:
- 1 <= synonyms.length <= 10
- 1 <= synonyms[i].length == 2
- 1 <= sentence.length <= 10^5

Example:
Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], sentence = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]

"""
def generateSentences(synonyms, text):
    from collections import defaultdict
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    for a, b in synonyms:
        parent[find(a)] = find(b)
    groups = defaultdict(set)
    for word in parent:
        groups[find(word)].add(word)
    words = text.split()
    res = []
    def dfs(i, path):
        if i == len(words):
            res.append(' '.join(path))
            return
        w = words[i]
        if w in parent:
            for syn in sorted(groups[find(w)]):
                dfs(i+1, path+[syn])
        else:
            dfs(i+1, path+[w])
    dfs(0, [])
    return sorted(res)

# Example usage
if __name__ == "__main__":
    synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
    sentence = "I am happy today but was sad yesterday"
    print(generateSentences(synonyms, sentence))
