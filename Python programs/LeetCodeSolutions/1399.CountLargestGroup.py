"""
LeetCode 1399. Count Largest Group

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. Return how many groups have the largest size.

Constraints:
- 1 <= n <= 10^4

Example:
Input: n = 13
Output: 4
"""
def countLargestGroup(n):
    from collections import Counter
    def digit_sum(x):
        return sum(int(d) for d in str(x))
    count = Counter(digit_sum(i) for i in range(1, n+1))
    max_size = max(count.values())
    return sum(1 for v in count.values() if v == max_size)

# Example usage:
n = 13
print(countLargestGroup(n))  # Output: 4
