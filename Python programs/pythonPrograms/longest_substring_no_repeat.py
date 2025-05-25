# Longest substring without repeating characters
def longest_substring(s):
    seen = {}
    start = max_len = 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__ == "__main__":
    s = input("String: ")
    print("Length:", longest_substring(s))
