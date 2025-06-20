"""
819. Most Common Word

Given a string paragraph and a list of banned words, return the most frequent word that is not banned. The answer is in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"

Constraints:
- 1 <= paragraph.length <= 1000
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- The answer is unique, and paragraph only contains letters, spaces, or the characters "!?',;.".
"""
def mostCommonWord(paragraph, banned):
    import re
    from collections import Counter
    words = re.findall(r'\w+', paragraph.lower())
    banned_set = set(banned)
    count = Counter(w for w in words if w not in banned_set)
    return count.most_common(1)[0][0]

# Example usage:
print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))  # Output: "ball"
