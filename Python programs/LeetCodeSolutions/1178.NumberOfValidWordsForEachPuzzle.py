"""
1178. Number of Valid Words for Each Puzzle

Given a list of words and a list of puzzles, return a list of the number of valid words for each puzzle. A word is valid for a puzzle if it contains the first letter of the puzzle and every letter in the word is in the puzzle.

Constraints:
- 1 <= words.length <= 10^5
- 1 <= puzzles.length <= 10^4
- 1 <= words[i].length <= 7
- 1 <= puzzles[i].length == 7

Example:
Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]

"""
def findNumOfValidWords(words, puzzles):
    from collections import Counter
    def mask(word):
        m = 0
        for c in set(word):
            m |= 1 << (ord(c) - 97)
        return m
    word_count = Counter(mask(w) for w in words if len(set(w)) <= 7)
    res = []
    for p in puzzles:
        m = mask(p)
        first = 1 << (ord(p[0]) - 97)
        count = 0
        sub = m
        while sub:
            if sub & first and sub in word_count:
                count += word_count[sub]
            sub = (sub - 1) & m
        res.append(count)
    return res

# Example usage
if __name__ == "__main__":
    words = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    print(findNumOfValidWords(words, puzzles))  # Output: [1,1,3,2,4,0]
