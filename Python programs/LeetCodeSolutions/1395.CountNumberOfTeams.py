"""
LeetCode 1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value. A team is formed by choosing 3 soldiers such that their ratings are either strictly increasing or strictly decreasing. Return the number of teams that can be formed.

Constraints:
- n == rating.length
- 3 <= n <= 1000
- 1 <= rating[i] <= 10^5

Example:
Input: rating = [2,5,3,4,1]
Output: 3
"""
def numTeams(rating):
    n = len(rating)
    res = 0
    for j in range(1, n-1):
        left_less = left_more = right_less = right_more = 0
        for i in range(j):
            if rating[i] < rating[j]: left_less += 1
            if rating[i] > rating[j]: left_more += 1
        for k in range(j+1, n):
            if rating[k] > rating[j]: right_more += 1
            if rating[k] < rating[j]: right_less += 1
        res += left_less * right_more + left_more * right_less
    return res

# Example usage:
rating = [2,5,3,4,1]
print(numTeams(rating))  # Output: 3
