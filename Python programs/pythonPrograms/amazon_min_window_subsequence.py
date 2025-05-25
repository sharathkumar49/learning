# Amazon: Find the Minimum Window Subsequence
# Given strings S and T, return the minimum window in S which will contain all the characters in T in order.
# If there is no such window in S that covers all characters in T, return the empty string "".

def min_window_subsequence(S, T):
    m, n = len(S), len(T)
    min_len = float('inf')
    start = -1
    i = 0
    while i < m:
        if S[i] == T[0]:
            t_idx = 0
            j = i
            while j < m:
                if S[j] == T[t_idx]:
                    t_idx += 1
                    if t_idx == n:
                        end = j
                        t_idx -= 1
                        while t_idx >= 0:
                            if S[j] == T[t_idx]:
                                t_idx -= 1
                            j -= 1
                        j += 1
                        if end - j + 1 < min_len:
                            min_len = end - j + 1
                            start = j
                        break
                j += 1
        i += 1
    return "" if start == -1 else S[start:start+min_len]

if __name__ == "__main__":
    print(min_window_subsequence("abcdebdde", "bde"))  # Output: "bcde"
