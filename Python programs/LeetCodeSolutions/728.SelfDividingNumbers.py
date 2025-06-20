"""
LeetCode 728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Example 1:
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Constraints:
- 1 <= left <= right <= 10^4
"""
from typing import List

def selfDividingNumbers(left: int, right: int) -> List[int]:
    res = []
    for num in range(left, right+1):
        n = num
        ok = True
        while n:
            d = n % 10
            if d == 0 or num % d != 0:
                ok = False
                break
            n //= 10
        if ok:
            res.append(num)
    return res

# Example usage
if __name__ == "__main__":
    print(selfDividingNumbers(1, 22))  # Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
