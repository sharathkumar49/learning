"""
1180. Count Substrings with Only One Distinct Letter

Given a string s, return the number of substrings with only one distinct letter.

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.

Example:
Input: s = "aaaba"
Output: 8

"""
def countLetters(s):
    res = 0
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        l = j - i
        res += l * (l + 1) // 2
        i = j
    return res

# Example usage
if __name__ == "__main__":
    print(countLetters("aaaba"))  # Output: 8
