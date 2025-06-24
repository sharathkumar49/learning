"""
1200. Minimum Absolute Difference

Given an array arr, return all pairs of elements with the minimum absolute difference in ascending order.

Constraints:
- 2 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6

Example:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]

"""
def minimumAbsDifference(arr):
    arr.sort()
    min_diff = min(arr[i+1] - arr[i] for i in range(len(arr)-1))
    return [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1] - arr[i] == min_diff]

# Example usage
if __name__ == "__main__":
    print(minimumAbsDifference([4,2,1,3]))  # Output: [[1,2],[2,3],[3,4]]
