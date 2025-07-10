"""
LeetCode 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits

Given a string num representing a large integer and an integer k, return the minimum integer you can obtain by performing at most k adjacent swaps on the digits.

Constraints:
- 1 <= num.length <= 3 * 10^4
- num consists of only digits and does not contain leading zeros.
- 1 <= k <= 10^9

Example:
Input: num = "4321", k = 4
Output: "1342"
"""
def minInteger(num, k):
    from collections import defaultdict, deque
    n = len(num)
    pos = defaultdict(deque)
    for i, d in enumerate(num):
        pos[d].append(i)
    res = []
    bit = [0]*(n+1)
    def update(i):
        i += 1
        while i <= n:
            bit[i] += 1
            i += i & -i
    def query(i):
        i += 1
        s = 0
        while i:
            s += bit[i]
            i -= i & -i
        return s
    for _ in range(n):
        for d in map(str, range(10)):
            if pos[d]:
                idx = pos[d][0]
                cost = idx - query(idx-1)
                if cost <= k:
                    k -= cost
                    res.append(d)
                    update(idx)
                    pos[d].popleft()
                    break
    return ''.join(res)

# Example usage:
num = "4321"
k = 4
print(minInteger(num, k))  # Output: "1342"
