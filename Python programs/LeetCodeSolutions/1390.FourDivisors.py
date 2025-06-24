"""
LeetCode 1390. Four Divisors

Given an integer array nums, return the sum of divisors of the integers in that have exactly four divisors. If there is no such integer in the array, return 0.

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^5

Example:
Input: nums = [21,4,7]
Output: 32
"""
def sumFourDivisors(nums):
    def four_divisors(n):
        divs = set()
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divs.add(i)
                divs.add(n//i)
            if len(divs) > 4:
                return 0
        return sum(divs) if len(divs) == 4 else 0
    return sum(four_divisors(x) for x in nums)

# Example usage:
nums = [21,4,7]
print(sumFourDivisors(nums))  # Output: 32
