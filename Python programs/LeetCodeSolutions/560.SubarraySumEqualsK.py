'''
 560. Subarray Sum Equals K
 Difficulty: Medium

 Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 Example 1:
 Input: nums = [1,1,1], k = 2
 Output: 2

 Example 2:
 Input: nums = [1,2,3], k = 3
 Output: 2

 Constraints:
 1 <= nums.length <= 2 * 10^4
 -1000 <= nums[i] <= 1000
 -10^7 <= k <= 10^7
'''

def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    prefix = {0: 1}
    for num in nums:
        curr_sum += num
        count += prefix.get(curr_sum - k, 0)
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
    return count

# Example usage
if __name__ == "__main__":
    print(subarraySum([1,1,1], 2))  # Output: 2
    print(subarraySum([1,2,3], 3))  # Output: 2
