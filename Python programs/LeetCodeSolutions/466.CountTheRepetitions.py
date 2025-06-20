"""
466. Count The Repetitions

Given strings s1, s2 and integers n1, n2, return the maximum integer M such that [s2, M] can be obtained from [s1, n1] by deleting some characters.

Constraints:
- 1 <= s1.length, s2.length <= 100
- 1 <= n1, n2 <= 10^6

Example:
Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
Output: 2
"""

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        s1cnt, index, s2cnt = 0, 0, 0
        recall = dict()
        while True:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt += 1
                        index = 0
            if s1cnt == n1:
                return s2cnt // n2
            if index in recall:
                s1cnt_prev, s2cnt_prev = recall[index]
                pre_loop = (s1cnt_prev, s2cnt_prev)
                in_loop = (s1cnt - s1cnt_prev, s2cnt - s2cnt_prev)
                break
            else:
                recall[index] = (s1cnt, s2cnt)
        ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        rest = (n1 - pre_loop[0]) % in_loop[0]
        for _ in range(rest):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0
        return ans // n2

# Example usage:
sol = Solution()
print(sol.getMaxRepetitions("acb", 4, "ab", 2))  # Output: 2
