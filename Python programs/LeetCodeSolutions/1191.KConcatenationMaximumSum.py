"""
1191. K-Concatenation Maximum Sum

Given an integer array arr and an integer k, return the maximum subarray sum in the array formed by concatenating arr k times. The answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= 10^5
- -10^4 <= arr[i] <= 10^4

Example:
Input: arr = [1,2], k = 3
Output: 9

"""
def kConcatenationMaxSum(arr, k):
    MOD = 10**9 + 7
    def kadane(a):
        max_sum = curr = 0
        for x in a:
            curr = max(x, curr + x)
            max_sum = max(max_sum, curr)
        return max_sum
    max1 = kadane(arr)
    if k == 1:
        return max1 % MOD
    max2 = kadane(arr * 2)
    total = sum(arr)
    if total > 0:
        return (max2 + (k-2)*total) % MOD
    else:
        return max2 % MOD

# Example usage
if __name__ == "__main__":
    print(kConcatenationMaxSum([1,2], 3))  # Output: 9
