"""
LeetCode 751. IP to CIDR

Given a start IP address and a number n, return a list of CIDR blocks to cover the range of n IP addresses starting from the start IP.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]

Constraints:
- 0 <= ip.length <= 15
- 1 <= n <= 1000
- ip is a valid IPv4 address.
"""
from typing import List

def ipToCIDR(ip: str, n: int) -> List[str]:
    def ip2int(ip):
        res = 0
        for x in ip.split('.'):
            res = res*256 + int(x)
        return res
    def int2ip(x):
        return '.'.join(str((x >> (8*i)) % 256) for i in [3,2,1,0])
    res = []
    x = ip2int(ip)
    while n > 0:
        step = x & -x
        while step > n:
            step //= 2
        mask = 32 - step.bit_length() + 1
        res.append(f"{int2ip(x)}/{mask}")
        x += step
        n -= step
    return res

# Example usage
if __name__ == "__main__":
    print(ipToCIDR("255.0.0.7", 10))  # Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
