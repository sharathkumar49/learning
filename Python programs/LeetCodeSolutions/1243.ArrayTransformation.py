"""
1243. Array Transformation

Given an integer array arr, repeatedly transform the array by replacing each element (except the first and last) with the sum of its neighbors. Return the array after k transformations.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 100
- 1 <= k <= 100

Example:
Input: arr = [1,2,3,4], k = 1
Output: [1,4,6,4]

"""
def transformArray(arr, k):
    for _ in range(k):
        arr = [arr[0]] + [arr[i-1] + arr[i+1] for i in range(1, len(arr)-1)] + [arr[-1]]
    return arr

# Example usage
if __name__ == "__main__":
    print(transformArray([1,2,3,4], 1))  # Output: [1,4,6,4]
