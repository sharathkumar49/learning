"""
1177. Can Make Palindrome from Substring

Given a string s and queries, each query is [left, right, k]. For each query, return True if the substring s[left:right+1] can be rearranged into a palindrome after replacing at most k characters.

Constraints:
- 1 <= s.length <= 10^5
- 1 <= queries.length <= 10^5
- 0 <= left <= right < s.length
- 0 <= k <= s.length

Example:
Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2]]
Output: [True,False,False,True]

"""
def canMakePaliQueries(s, queries):
    n = len(s)
    prefix = [[0]*26]
    for c in s:
        prefix.append(prefix[-1][:])
        prefix[-1][ord(c)-97] += 1
    res = []
    for l, r, k in queries:
        odd = 0
        for i in range(26):
            if (prefix[r+1][i] - prefix[l][i]) % 2:
                odd += 1
        res.append(odd//2 <= k)
    return res

# Example usage
if __name__ == "__main__":
    print(canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2]]))  # Output: [True, False, False, True]
