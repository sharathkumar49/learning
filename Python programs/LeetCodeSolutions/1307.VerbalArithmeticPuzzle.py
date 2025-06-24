"""
LeetCode 1307. Verbal Arithmetic Puzzle

Given an array of words and a result word, assign each letter a digit 0-9 so that the sum of the words equals the result. No two letters can have the same digit, and no word can have a leading zero. Return true if a solution exists.

Constraints:
- 2 <= words.length <= 5
- 1 <= words[i].length, result.length <= 7
- All words and result contain only uppercase English letters.

Example:
Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
"""
def isSolvable(words, result):
    from itertools import permutations
    chars = set(''.join(words) + result)
    if len(chars) > 10:
        return False
    first = set(w[0] for w in words + [result])
    chars = list(chars)
    n = len(chars)
    nums = range(10)
    for perm in permutations(nums, n):
        d = dict(zip(chars, perm))
        if any(d[w[0]] == 0 for w in words + [result]):
            continue
        s = sum(int(''.join(str(d[c]) for c in w)) for w in words)
        r = int(''.join(str(d[c]) for c in result))
        if s == r:
            return True
    return False

# Example usage:
words = ["SEND","MORE"]
result = "MONEY"
print(isSolvable(words, result))  # Output: True
