"""
811. Subdomain Visit Count

A website domain like "discuss.leetcode.com" consists of various subdomains. Given a list of count-paired domains, return the number of visits to each subdomain.

Example 1:
Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]

Constraints:
- 1 <= cpdomains.length <= 100
- 1 <= cpdomains[i].length <= 100
- cpdomains[i] follows the format "repi d1.d2.d3" where repi is an integer and d1.d2.d3 is a domain name.
"""
def subdomainVisits(cpdomains):
    from collections import Counter
    count = Counter()
    for entry in cpdomains:
        num, domain = entry.split()
        num = int(num)
        frags = domain.split('.')
        for i in range(len(frags)):
            sub = '.'.join(frags[i:])
            count[sub] += num
    return [f"{v} {k}" for k, v in count.items()]

# Example usage:
print(subdomainVisits(["9001 discuss.leetcode.com"]))  # Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
