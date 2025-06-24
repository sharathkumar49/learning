"""
1224. Maximum Equal Frequency

Given an array nums, return the length of the longest prefix such that after removing at most one element, every number has the same frequency.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Example:
Input: nums = [2,2,1,1,5,3,3,5]
Output: 7

"""
def maxEqualFreq(nums):
    from collections import Counter
    count = Counter()
    freq = Counter()
    res = 0
    for i, x in enumerate(nums):
        if count[x]:
            freq[count[x]] -= 1
        count[x] += 1
        freq[count[x]] += 1
        if len(freq) == 2:
            f1, f2 = freq.keys()
            c1, c2 = freq[f1], freq[f2]
            if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
                res = i + 1
            elif abs(f1 - f2) == 1 and (freq[max(f1, f2)] == 1):
                res = i + 1
        elif len(freq) == 1:
            f = next(iter(freq))
            if f == 1 or freq[f] == 1:
                res = i + 1
    return res

# Example usage
if __name__ == "__main__":
    print(maxEqualFreq([2,2,1,1,5,3,3,5]))  # Output: 7
