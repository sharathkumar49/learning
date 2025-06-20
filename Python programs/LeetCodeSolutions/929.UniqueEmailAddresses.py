"""
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/

Every valid email consists of a local name and a domain name, separated by the '@' sign. Given a list of emails, return the number of unique email addresses after normalization.
Normalization rules:
- In the local name, everything after a '+' is ignored.
- All '.' in the local name are ignored.

Constraints:
- 1 <= emails.length <= 100
- 1 <= emails[i].length <= 100
- emails[i] consist of lowercase English letters, '+', '.', and '@'.

Example:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
"""
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)

# Example usage
if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(emails))  # Output: 2
