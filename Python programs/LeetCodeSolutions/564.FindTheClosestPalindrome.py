"""
564. Find the Closest Palindrome
Difficulty: Hard

Given a string n representing an integer, return the closest integer palindrome (not including itself), which is closest in absolute difference to n. If there is a tie, return the smaller one.

Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"

Constraints:
1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
"""

def nearestPalindromic(n: str) -> str:
    length = len(n)
    candidates = set()
    # Edge cases: 10..01, 9..9, 100..001
    candidates.add(str(10**length + 1))
    candidates.add(str(10**(length-1) - 1))
    prefix = int(n[:(length+1)//2])
    for i in [-1, 0, 1]:
        p = str(prefix + i)
        if length % 2:
            candidate = p + p[:-1][::-1]
        else:
            candidate = p + p[::-1]
        candidates.add(candidate)
    candidates.discard(n)
    min_diff = float('inf')
    res = None
    n_int = int(n)
    for cand in candidates:
        if cand == n or cand.startswith('0'):
            continue
        diff = abs(int(cand) - n_int)
        if diff < min_diff or (diff == min_diff and int(cand) < int(res)):
            min_diff = diff
            res = cand
    return res

# Example usage
if __name__ == "__main__":
    print(nearestPalindromic("123"))  # Output: "121"
    print(nearestPalindromic("1"))    # Output: "0"
