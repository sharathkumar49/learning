"""
LeetCode 1363. Largest Multiple of Three

Given an array of digits, return the largest multiple of three that can be formed by concatenating some of the digits in any order. If not possible, return an empty string.

Constraints:
- 1 <= digits.length <= 10^4
- 0 <= digits[i] <= 9

Example:
Input: digits = [8,1,9]
Output: "981"
"""
def largestMultipleOfThree(digits):
    digits.sort(reverse=True)
    total = sum(digits)
    mod = total % 3
    buckets = [[], [], []]
    for d in digits:
        buckets[d % 3].append(d)
    if mod:
        if buckets[mod]:
            buckets[mod].sort()
            buckets[mod].pop()
        else:
            buckets[3-mod].sort()
            buckets[3-mod] = buckets[3-mod][2:]
    res = buckets[0] + buckets[1] + buckets[2]
    res.sort(reverse=True)
    if not res:
        return ""
    if res[0] == 0:
        return "0"
    return ''.join(map(str, res))

# Example usage:
digits = [8,1,9]
print(largestMultipleOfThree(digits))  # Output: "981"
