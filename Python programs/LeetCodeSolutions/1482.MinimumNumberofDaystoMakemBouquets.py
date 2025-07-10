"""
LeetCode 1482. Minimum Number of Days to Make m Bouquets

Given an integer array bloomDay, an integer m and an integer k, return the minimum number of days to make m bouquets each with k adjacent flowers. If it is impossible, return -1.

Constraints:
- 1 <= bloomDay.length <= 10^5
- 1 <= bloomDay[i] <= 10^9
- 1 <= m <= 10^6
- 1 <= k <= bloomDay.length

Example:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
"""
def minDays(bloomDay, m, k):
    def canMake(days):
        bouquets = flowers = 0
        for b in bloomDay:
            if b <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m
    if m * k > len(bloomDay):
        return -1
    left, right = 1, max(bloomDay)
    while left < right:
        mid = (left + right) // 2
        if canMake(mid):
            right = mid
        else:
            left = mid + 1
    return left if canMake(left) else -1

# Example usage:
bloomDay = [1,10,3,10,2]
m, k = 3, 1
print(minDays(bloomDay, m, k))  # Output: 3
