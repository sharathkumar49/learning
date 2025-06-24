"""
1187. Make Array Strictly Increasing

Given two integer arrays arr1 and arr2, return the minimum number of operations to make arr1 strictly increasing by replacing elements with those from arr2. If impossible, return -1.

Constraints:
- 1 <= arr1.length, arr2.length <= 2000
- 0 <= arr1[i], arr2[i] <= 10^9

Example:
Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1

"""
def makeArrayIncreasing(arr1, arr2):
    from bisect import bisect_right
    arr2 = sorted(set(arr2))
    dp = {-1: 0}
    for a in arr1:
        tmp = {}
        for key in dp:
            if a > key:
                tmp[a] = min(tmp.get(a, float('inf')), dp[key])
            idx = bisect_right(arr2, key)
            if idx < len(arr2):
                tmp[arr2[idx]] = min(tmp.get(arr2[idx], float('inf')), dp[key] + 1)
        dp = tmp
    return min(dp.values()) if dp else -1

# Example usage
if __name__ == "__main__":
    print(makeArrayIncreasing([1,5,3,6,7], [1,3,2,4]))  # Output: 1
