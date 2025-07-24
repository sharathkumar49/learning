"""
LeetCode 2559. Count Vowel Strings in Ranges

Given words and queries, return the number of vowel strings in each range.

Constraints:
- 1 <= words.length, queries.length <= 10^5
"""

def vowelStrings(words, queries):
    vowels = set('aeiou')
    prefix = [0]
    for w in words:
        prefix.append(prefix[-1]+(w[0] in vowels and w[-1] in vowels))
    return [prefix[r+1]-prefix[l] for l,r in queries]
# Example usage:
# print(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))  # Output: [2,3,0]
