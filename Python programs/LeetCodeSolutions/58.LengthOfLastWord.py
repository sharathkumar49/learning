# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# Example 1:
# Input: s = "Hello World"
# Output: 5
#
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
#
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
#
# Constraints:
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.

def lengthOfLastWord(s):
    return len(s.strip().split(' ')[-1])

# Example usage
s = "Hello World"
print("Length of last word:", lengthOfLastWord(s))  # Output: 5
