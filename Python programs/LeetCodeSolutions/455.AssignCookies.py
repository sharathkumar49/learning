"""
455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. Each child i has a greed factor g[i], and each cookie j has a size s[j]. You want to maximize the number of your content children.

Constraints:
- 1 <= g.length <= 3 * 10^4
- 0 <= s.length <= 3 * 10^4
- 1 <= g[i], s[j] <= 2^31 - 1

Example:
Input: g = [1,2,3], s = [1,1]
Output: 1
"""

class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i

# Example usage:
sol = Solution()
print(sol.findContentChildren([1,2,3], [1,1]))  # Output: 1
