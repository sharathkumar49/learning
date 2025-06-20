#  553. Optimal Division
#  Difficulty: Medium
# 
#  You are given an integer array nums. The numbers are arranged in a line (not necessarily sorted). You are to perform division operations to get the maximum result. You may add parentheses to change the order of operations.
# 
#  You should return a string representing the expression that gives the maximum result.
# 
#  Example 1:
#  Input: nums = [1000,200,3,4]
#  Output: "1000/(200/3/4)" or "1000/(200/3/4)"
#  Explanation: You need to divide 1000 by 200, then by 3, then by 4, but to maximize the result, you should group the last three numbers together.
# 
#  Example 2:
#  Input: nums = [2,3,4]
#  Output: "2/(3/4)"
# 
#  Constraints:
#  1 <= nums.length <= 10
#  2 <= nums[i] <= 1000

def optimalDivision(nums):
    if len(nums) == 1:
        return str(nums[0])
    if len(nums) == 2:
        return f"{nums[0]}/{nums[1]}"
    return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"

# Example usage
if __name__ == "__main__":
    print(optimalDivision([1000,200,3,4]))  # Output: "1000/(200/3/4)"
    print(optimalDivision([2,3,4]))         # Output: "2/(3/4)"
