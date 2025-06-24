"""
1156. Swap For Longest Repeated Character Substring

Given a string text, return the length of the longest substring consisting of one character that can be obtained by swapping two characters at most once.

Constraints:
- 1 <= text.length <= 20000
- text consists of lowercase English letters.

Example:
Input: text = "ababa"
Output: 3

"""
def maxRepOpt1(text):
    from collections import Counter
    count = Counter(text)
    res = 0
    i = 0
    n = len(text)
    while i < n:
        j = i
        while j < n and text[j] == text[i]:
            j += 1
        l = j - i
        k = j + 1
        while k < n and text[k] == text[i]:
            k += 1
        l2 = k - j if j < n and text[j] != text[i] else 0
        total = l + l2
        if total < count[text[i]]:
            total += 1
        res = max(res, total, l)
        i = j
    return res

# Example usage
if __name__ == "__main__":
    print(maxRepOpt1("ababa"))  # Output: 3
