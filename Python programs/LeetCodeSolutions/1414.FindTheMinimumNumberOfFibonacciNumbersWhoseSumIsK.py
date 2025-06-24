"""
LeetCode 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. Each Fibonacci number can be used any number of times.

Constraints:
- 1 <= k <= 10^9

Example:
Input: k = 7
Output: 2
"""
def findMinFibonacciNumbers(k):
    fibs = [1, 1]
    while fibs[-1] < k:
        fibs.append(fibs[-1] + fibs[-2])
    count = 0
    for f in reversed(fibs):
        while k >= f:
            k -= f
            count += 1
    return count

# Example usage:
k = 7
print(findMinFibonacciNumbers(k))  # Output: 2
