"""
LeetCode 2162. Minimum Cost to Set Cooking Time

Given startAt, moveCost, pushCost, and targetSeconds, return the minimum cost to set the microwave timer to targetSeconds. The timer is set by pushing digits, and moving the finger to a new digit costs moveCost, pushing a digit costs pushCost. The timer can be set in MMSS format (max 99:99).

Example:
Input: startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600
Output: 6

Constraints:
- 0 <= startAt <= 9
- 1 <= moveCost, pushCost <= 10^4
- 1 <= targetSeconds <= 6039
"""

def minCostSetTime(startAt, moveCost, pushCost, targetSeconds):
    def cost(seq):
        cur = str(startAt)
        res = 0
        for d in seq:
            if cur != d:
                res += moveCost
            res += pushCost
            cur = d
        return res
    res = float('inf')
    for m in range(100):
        s = targetSeconds - m*60
        if 0 <= s < 100:
            seq = str(m).zfill(2) + str(s).zfill(2)
            seq = seq.lstrip('0') or '0'
            res = min(res, cost(seq))
    return res

# Example usage:
# print(minCostSetTime(1,2,1,600))  # Output: 6
