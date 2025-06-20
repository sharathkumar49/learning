# 191. Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
# Example 1:
# Input: n = 11 (00000000000000000000000000001011)
# Output: 3
#
# Example 2:
# Input: n = 128 (00000000000000000000000010000000)
# Output: 1
#
# Constraints:
# The input must be a binary string of length 32.

def hammingWeight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# Example usage
n = 11
print("Number of 1 bits:", hammingWeight(n))  # Output: 3
