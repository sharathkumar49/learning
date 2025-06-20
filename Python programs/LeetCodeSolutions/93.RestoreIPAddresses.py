"""
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

Given a string s containing only digits, return all possible valid IP addresses that can be obtained by inserting dots into s.
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Constraints:
- 1 <= s.length <= 20
- s consists of digits only.

Example:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
"""
from typing import List

def restoreIpAddresses(s: str) -> List[str]:
    res = []
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return
        for l in range(1, 4):
            if start + l > len(s):
                break
            part = s[start:start+l]
            if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start+l, path + [part])
    backtrack(0, [])
    return res

# Example usage:
if __name__ == "__main__":
    print(restoreIpAddresses("25525511135"))  # Output: ["255.255.11.135","255.255.111.35"]
