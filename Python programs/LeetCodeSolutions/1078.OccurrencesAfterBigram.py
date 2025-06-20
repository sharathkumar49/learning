"""
1078. Occurrences After Bigram

Given a string text and two words first and second, return all words that immediately follow the occurrence of first and second in text.

Constraints:
- 1 <= text.length <= 1000
- text consists of lowercase English letters and spaces
- 1 <= first.length, second.length <= 100
- first and second consist of lowercase English letters

Example:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
"""
from typing import List

def findOcurrences(text: str, first: str, second: str) -> List[str]:
    words = text.split()
    res = []
    for i in range(len(words) - 2):
        if words[i] == first and words[i+1] == second:
            res.append(words[i+2])
    return res

# Example usage:
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(findOcurrences(text, first, second))  # Output: ['girl', 'student']
