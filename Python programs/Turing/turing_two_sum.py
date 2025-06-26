# Turing: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))  # Output: [0,1]
    print(two_sum([3,2,4], 6))      # Output: [1,2]
