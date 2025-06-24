"""
1209. Remove All Adjacent Duplicates in String II

Given a string s and an integer k, remove all k adjacent duplicates in s. Repeat until no more can be removed.

Constraints:
- 1 <= s.length <= 10^5
- 2 <= k <= 10^4
- s consists of lowercase English letters.

Example:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"

"""
def removeDuplicates(s, k):
    stack = []
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * count for c, count in stack)

# Example usage
if __name__ == "__main__":
    print(removeDuplicates("deeedbbcccbdaa", 3))  # Output: "aa"
