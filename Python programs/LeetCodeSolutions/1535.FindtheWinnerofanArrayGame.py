"""
LeetCode 1535. Find the Winner of an Array Game

Given an integer array arr of distinct integers and an integer k, return the winner of the game described in the problem statement.

Constraints:
- 2 <= arr.length <= 10^5
- 1 <= k <= 10^9
- arr[i] are distinct

Example:
Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
"""
def getWinner(arr, k):
    curr = arr[0]
    win = 0
    for i in range(1, len(arr)):
        if arr[i] > curr:
            curr = arr[i]
            win = 1
        else:
            win += 1
        if win == k:
            return curr
    return curr

# Example usage:
arr = [2,1,3,5,4,6,7]
k = 2
print(getWinner(arr, k))  # Output: 5
