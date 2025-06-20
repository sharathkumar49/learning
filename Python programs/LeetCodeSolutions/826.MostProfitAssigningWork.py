"""
826. Most Profit Assigning Work

You have n jobs with difficulty and profit, and m workers. Each worker can be assigned at most one job whose difficulty is less than or equal to their ability. Return the maximum profit we can achieve.

Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100

Constraints:
- n == difficulty.length
- n == profit.length
- 1 <= n, m <= 10^4
- 1 <= difficulty[i], profit[i], worker[i] <= 10^5
"""
def maxProfitAssignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    res = i = best = 0
    for w in worker:
        while i < len(jobs) and jobs[i][0] <= w:
            best = max(best, jobs[i][1])
            i += 1
        res += best
    return res

# Example usage:
print(maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))  # Output: 100
