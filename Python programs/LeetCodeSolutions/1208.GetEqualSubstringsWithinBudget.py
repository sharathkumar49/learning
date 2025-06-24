"""
1208. Get Equal Substrings Within Budget

Given two strings s and t of equal length, and an integer maxCost, return the maximum length of a substring of s that can be changed to t with a cost less than or equal to maxCost. The cost is the sum of |s[i] - t[i]| for each character.

Constraints:
- 1 <= s.length <= 10^5
- t.length == s.length
- 0 <= maxCost <= 10^6

Example:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3

"""
def equalSubstring(s, t, maxCost):
    n = len(s)
    left = 0
    cost = 0
    res = 0
    for right in range(n):
        cost += abs(ord(s[right]) - ord(t[right]))
        while cost > maxCost:
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        res = max(res, right - left + 1)
    return res

# Example usage
if __name__ == "__main__":
    print(equalSubstring("abcd", "bcdf", 3))  # Output: 3
