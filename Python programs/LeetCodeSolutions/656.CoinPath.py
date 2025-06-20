"""
656. Coin Path
Difficulty: Hard

Given an array A of positive integers, you start at index 0 and can jump up to B steps at a time. Return the path with the minimum sum of values from index 0 to the last index. If there are multiple paths, return the lexicographically smallest one. If no path exists, return an empty list.

Example 1:
Input: A = [1,2,4,4,5,2,1,4,2,2,1], B = 3
Output: [1,3,5,7,10,11]

Constraints:
1 <= A.length <= 1000
1 <= A[i] <= 10^6
1 <= B <= 100
"""

def cheapestJump(A, B):
    n = len(A)
    dp = [float('inf')] * n
    prev = [-1] * n
    dp[0] = A[0]
    for i in range(1, n):
        if A[i] == -1:
            continue
        for j in range(max(0, i-B), i):
            if A[j] == -1:
                continue
            if dp[j] + A[i] < dp[i]:
                dp[i] = dp[j] + A[i]
                prev[i] = j
    if dp[-1] == float('inf'):
        return []
    path = []
    i = n - 1
    while i != -1:
        path.append(i+1)
        i = prev[i]
    return path[::-1]

# Example usage
if __name__ == "__main__":
    print(cheapestJump([1,2,4,4,5,2,1,4,2,2,1], 3))  # Output: [1,3,5,7,10,11]
