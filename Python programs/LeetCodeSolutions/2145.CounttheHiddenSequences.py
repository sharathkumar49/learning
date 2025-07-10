"""
LeetCode 2145. Count the Hidden Sequences

You are given an integer n and an integer array differences of length n-1. The array differences represents the difference between consecutive elements of a hidden sequence. Return the number of possible hidden sequences that satisfy the constraints that all elements are in the range [lower, upper].

Example:
Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2

Constraints:
- 1 <= n <= 10^5
- -10^5 <= differences[i] <= 10^5
- -10^5 <= lower <= upper <= 10^5
"""

def numberOfArrays(differences, lower, upper):
    min_sum = max_sum = curr = 0
    for d in differences:
        curr += d
        min_sum = min(min_sum, curr)
        max_sum = max(max_sum, curr)
    return max(0, (upper - lower) - (max_sum - min_sum) + 1)

# Example usage:
# print(numberOfArrays([1,-3,4], 1, 6))  # Output: 2
