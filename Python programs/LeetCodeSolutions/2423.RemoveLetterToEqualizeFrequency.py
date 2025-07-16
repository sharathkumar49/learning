"""
LeetCode 2423. Remove Letter To Equalize Frequency

Given a string, return True if you can remove one letter to equalize frequency of all letters.

Constraints:
- 2 <= word.length <= 100
"""

def equalFrequency(word):
    from collections import Counter
    for i in range(len(word)):
        w = word[:i]+word[i+1:]
        vals = list(Counter(w).values())
        if len(set(vals)) == 1:
            return True
    return False

# Example usage:
# print(equalFrequency("abcc"))  # Output: True
