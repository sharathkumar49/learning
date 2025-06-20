"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

Constraints:
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

Note: The guess API is not implemented here. In LeetCode, it is provided for you.
"""
# The guess API is not implemented in this code.
# def guess(num: int) -> int:
#     ...

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            # res = guess(mid)
            res = 0  # Placeholder for LeetCode's guess API
            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# Example usage:
# n = 10
# pick = 6
# print(Solution().guessNumber(n))
