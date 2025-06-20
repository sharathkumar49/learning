# 70. Climbing Stairs (DP)
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways: 1+1 steps, or 2 steps.
#
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: 1+1+1, 1+2, 2+1
#
# Constraints:
# 1 <= n <= 45

def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

# Example usage
n = 5
print("Ways to climb stairs:", climbStairs(n))  # Output: 8
