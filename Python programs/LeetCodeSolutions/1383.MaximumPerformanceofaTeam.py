"""
LeetCode 1383. Maximum Performance of a Team

You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the i-th engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 10^5
- speed.length == n
- efficiency.length == n
- 1 <= k <= n
- 1 <= speed[i] <= 10^5
- 1 <= efficiency[i] <= 10^8

Example:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
"""
import heapq

def maxPerformance(n, speed, efficiency, k):
    MOD = 10**9 + 7
    engineers = sorted(zip(efficiency, speed), reverse=True)
    speed_heap = []
    speed_sum = 0
    result = 0
    for eff, spd in engineers:
        heapq.heappush(speed_heap, spd)
        speed_sum += spd
        if len(speed_heap) > k:
            speed_sum -= heapq.heappop(speed_heap)
        result = max(result, speed_sum * eff)
    return result % MOD

# Example usage:
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(maxPerformance(n, speed, efficiency, k))  # Output: 60
