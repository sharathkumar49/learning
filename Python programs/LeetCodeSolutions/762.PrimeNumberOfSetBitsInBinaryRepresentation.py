"""
LeetCode 762. Prime Number of Set Bits in Binary Representation

Given two integers left and right, return the count of numbers in the range [left, right] (inclusive) having a prime number of set bits in their binary representation.

Example 1:
Input: left = 6, right = 10
Output: 4

Example 2:
Input: left = 10, right = 15
Output: 5

Constraints:
- 1 <= left <= right <= 10^6
- 0 <= right - left <= 10^4
"""
def countPrimeSetBits(left: int, right: int) -> int:
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    primes = set(i for i in range(2, 21) if is_prime(i))
    res = 0
    for n in range(left, right+1):
        if bin(n).count('1') in primes:
            res += 1
    return res

# Example usage
if __name__ == "__main__":
    print(countPrimeSetBits(6, 10))   # Output: 4
    print(countPrimeSetBits(10, 15))  # Output: 5
