# Microsoft: Find the Minimum Window Subsequence
# Given strings S and T, return the minimum window in S which will contain all the characters in T in order.

def min_window_subsequence(S, T):
    m, n = len(S), len(T)
    min_len = float('inf')
    start = -1
    i = 0
    while i < m:
        if S[i] == T[0]:
            j = 0
            k = i
            while k < m and j < n:
                if S[k] == T[j]:
                    j += 1
                k += 1
            if j == n:
                end = k - 1
                j -= 1
                k -= 1
                while j >= 0:
                    if S[k] == T[j]:
                        j -= 1
                    k -= 1
                if end - k < min_len:
                    min_len = end - k
                    start = k + 1
        i += 1
    return "" if start == -1 else S[start:start+min_len]

if __name__ == "__main__":
    S1 = "abcdebdde"
    T1 = "bde"
    print(min_window_subsequence(S1, T1))  # Output: "bcde"
    S2 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
    T2 = "u"
    print(min_window_subsequence(S2, T2))  # Output: ""
