"""
LeetCode 1702. Maximum Binary String After Change

You are given a binary string binary. You can apply the following operation any number of times:
- Choose two consecutive characters and if they are "01", change them to "10".

Return the maximum binary string you can obtain after any number of operations.

Example 1:
Input: binary = "000110"
Output: "111011"

Constraints:
- 1 <= binary.length <= 10^5
- binary consists only of '0' and '1'.
"""

def maximumBinaryString(binary):
    n = len(binary)
    first_zero = binary.find('0')
    if first_zero == -1:
        return binary
    zeros = binary.count('0')
    return '1' * first_zero + '1' * (zeros - 1) + '0' + '1' * (n - first_zero - zeros)

# Example usage:
# binary = "000110"
# print(maximumBinaryString(binary))  # Output: "111011"
