"""
1228. Missing Number In Arithmetic Progression

Given an array arr that is a part of an arithmetic progression with one number missing, return the missing number.

Constraints:
- 3 <= arr.length <= 1000
- 0 <= arr[i] <= 10^6

Example:
Input: arr = [5,7,11,13]
Output: 9

"""
def missingNumber(arr):
    n = len(arr) + 1
    total = (arr[0] + arr[-1]) * n // 2
    return total - sum(arr)

# Example usage
if __name__ == "__main__":
    print(missingNumber([5,7,11,13]))  # Output: 9
