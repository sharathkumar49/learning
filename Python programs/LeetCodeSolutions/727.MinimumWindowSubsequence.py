"""
LeetCode 727. Minimum Window Subsequence

Given strings S and T, return the minimum window in S which will contain all the characters in T in order.

Example 1:
Input: S = "abcdebdde", T = "bde"
Output: "bcde"

Constraints:
- 1 <= S.length, T.length <= 2000
- S and T consist of only lowercase English letters.
"""
def minWindow(S: str, T: str) -> str:
    m, n = len(S), len(T)
    res = ""
    i = 0
    while i < m:
        if S[i] == T[0]:
            j = 0
            k = i
            while k < m:
                if S[k] == T[j]:
                    j += 1
                    if j == n:
                        break
                k += 1
            if j == n:
                end = k
                j -= 1
                while k >= i:
                    if S[k] == T[j]:
                        j -= 1
                        if j < 0:
                            break
                    k -= 1
                if not res or end - k < len(res):
                    res = S[k+1:end+1]
        i += 1
    return res

# Example usage
if __name__ == "__main__":
    print(minWindow("abcdebdde", "bde"))  # Output: "bcde"
