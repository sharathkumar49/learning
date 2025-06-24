"""
1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k, return the number of nice subarrays. A nice subarray is a subarray with exactly k odd numbers.

Constraints:
- 1 <= nums.length <= 50000
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length

Example:
Input: nums = [1,1,2,1,1], k = 3
Output: 2

"""
def numberOfSubarrays(nums, k):
    from collections import defaultdict
    count = defaultdict(int)
    count[0] = 1
    res = odd = 0
    for num in nums:
        odd += num % 2
        res += count[odd - k]
        count[odd] += 1
    return res

# Example usage
if __name__ == "__main__":
    print(numberOfSubarrays([1,1,2,1,1], 3))  # Output: 2
