"""
1235. Maximum Profit in Job Scheduling

Given startTime, endTime, and profit arrays, return the maximum profit in non-overlapping jobs.

Constraints:
- 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
- 1 <= startTime[i] < endTime[i] <= 10^9
- 1 <= profit[i] <= 10^4

Example:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120

"""
def jobScheduling(startTime, endTime, profit):
    import bisect
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [(0, 0)]
    for e, s, p in jobs:
        i = bisect.bisect_right(dp, (s, float('inf')))
        if dp[i-1][1] + p > dp[-1][1]:
            dp.append((e, dp[i-1][1] + p))
    return dp[-1][1]

# Example usage
if __name__ == "__main__":
    print(jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))  # Output: 120
