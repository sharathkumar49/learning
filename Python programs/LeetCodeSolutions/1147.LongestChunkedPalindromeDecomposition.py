"""
1147. Longest Chunked Palindrome Decomposition

Given a string text, return the largest number of chunks such that the concatenation of all the chunks is equal to the original string, and each chunk is a palindrome.

Constraints:
- 1 <= text.length <= 1000
- text consists only of lowercase English letters.

Example:
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7

"""
def longestDecomposition(text):
    n = len(text)
    ans = 0
    l, r = 0, n
    while l < r:
        k = 1
        while l + k <= r - k and text[l:l+k] != text[r-k:r]:
            k += 1
        if l + k > r - k:
            ans += 1
            break
        ans += 2
        l += k
        r -= k
    return ans

# Example usage
if __name__ == "__main__":
    print(longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))  # Output: 7
