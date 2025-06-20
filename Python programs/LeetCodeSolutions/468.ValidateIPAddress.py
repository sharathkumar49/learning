"""
468. Validate IP Address

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

Constraints:
- s consists only of English letters, digits and the characters '.' and ':'

Example:
Input: queryIP = "172.16.254.1"
Output: "IPv4"
"""

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s):
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return False
            return True
        def isIPv6(s):
            parts = s.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in '0123456789abcdefABCDEF' for c in part):
                    return False
            return True
        if isIPv4(queryIP):
            return "IPv4"
        if isIPv6(queryIP):
            return "IPv6"
        return "Neither"

# Example usage:
sol = Solution()
print(sol.validIPAddress("172.16.254.1"))  # Output: "IPv4"
