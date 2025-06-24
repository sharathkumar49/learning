"""
1144. Decrease Elements To Make Array Zigzag

Given an array nums, a zigzag array is one where every even-indexed element is greater than its adjacent elements, and every odd-indexed element is less than its adjacent elements. Return the minimum number of moves to make nums a zigzag array. (A move is incrementing or decrementing an element by 1.)

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000

Example:
Input: nums = [1,2,3]
Output: 2

"""
def movesToMakeZigzag(nums):
    n = len(nums)
    res = [0, 0]
    for parity in [0, 1]:
        moves = 0
        for i in range(n):
            if i % 2 == parity:
                left = nums[i-1] if i-1 >= 0 else float('inf')
                right = nums[i+1] if i+1 < n else float('inf')
                min_adj = min(left, right)
                if nums[i] >= min_adj:
                    moves += nums[i] - min_adj + 1
        res[parity] = moves
    return min(res)

# Example usage
if __name__ == "__main__":
    print(movesToMakeZigzag([1,2,3]))  # Output: 2
