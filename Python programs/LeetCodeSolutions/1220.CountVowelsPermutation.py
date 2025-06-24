"""
1220. Count Vowels Permutation

Given an integer n, return the number of strings of length n that consist only of vowels and are lexicographically sorted. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 2 * 10^4

Example:
Input: n = 1
Output: 5

"""
def countVowelStrings(n):
    dp = [1]*5
    for _ in range(n-1):
        for i in range(3, -1, -1):
            dp[i] += dp[i+1]
    return sum(dp)

# Example usage
if __name__ == "__main__":
    print(countVowelStrings(1))  # Output: 5
