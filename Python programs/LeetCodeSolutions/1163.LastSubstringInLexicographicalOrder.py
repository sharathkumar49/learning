"""
1163. Last Substring in Lexicographical Order

Given a string s, return the last substring in lexicographical order.

Constraints:
- 1 <= s.length <= 10^5
- s contains only lowercase English letters.

Example:
Input: s = "abab"
Output: "bab"

"""
def lastSubstring(s):
    n = len(s)
    i, j, k = 0, 1, 0
    while j + k < n:
        if s[i + k] == s[j + k]:
            k += 1
        elif s[i + k] < s[j + k]:
            i = max(i + k + 1, j)
            k = 0
            j = i + 1
        else:
            j = j + k + 1
            k = 0
    return s[i:]

# Example usage
if __name__ == "__main__":
    print(lastSubstring("abab"))  # Output: "bab"
