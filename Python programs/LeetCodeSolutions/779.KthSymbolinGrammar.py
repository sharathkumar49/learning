"""
779. K-th Symbol in Grammar

On the first row, we write a 0. Now in every subsequent row, we replace each 0 with 01 and each 1 with 10. Given row n and index k, return the k-th symbol in the n-th row of this sequence.

Example 1:
Input: n = 1, k = 1
Output: 0

Example 2:
Input: n = 2, k = 1
Output: 0

Example 3:
Input: n = 2, k = 2
Output: 1

Constraints:
- 1 <= n <= 30
- 1 <= k <= 2^(n - 1)
"""
def kthGrammar(n, k):
    if n == 1:
        return 0
    parent = kthGrammar(n-1, (k+1)//2)
    if k % 2 == 1:
        return parent
    else:
        return 1 - parent

# Example usage:
print(kthGrammar(1, 1))  # Output: 0
print(kthGrammar(2, 1))  # Output: 0
print(kthGrammar(2, 2))  # Output: 1
