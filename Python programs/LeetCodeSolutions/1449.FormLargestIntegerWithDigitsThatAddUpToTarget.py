"""
LeetCode 1449. Form Largest Integer With Digits That Add up to Target

Given an array of costs and an integer target, return the largest integer that can be formed with digits 1-9 and the sum of their costs equals target. Return "0" if it is impossible.

Constraints:
- costs.length == 9
- 1 <= costs[i] <= 5000
- 1 <= target <= 5000

Example:
Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"
"""
def largestNumber(cost, target):
    dp = ["0"] + ["" for _ in range(target)]
    for t in range(1, target+1):
        for d in range(9, 0, -1):
            c = cost[d-1]
            if t >= c and dp[t-c] != "":
                cand = dp[t-c] + str(d)
                if len(cand) > len(dp[t]) or (len(cand) == len(dp[t]) and cand > dp[t]):
                    dp[t] = cand
    return dp[target] if dp[target] != "" else "0"

# Example usage:
cost = [4,3,2,5,6,7,2,5,5]
target = 9
print(largestNumber(cost, target))  # Output: "7772"
