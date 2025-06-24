"""
1231. Divide Chocolate

Given an array sweetness and an integer K, divide the chocolate into K+1 pieces to maximize the minimum total sweetness of any piece.

Constraints:
- 1 <= sweetness.length <= 10^4
- 1 <= sweetness[i] <= 10^9
- 1 <= K <= sweetness.length - 1

Example:
Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6

"""
def maximizeSweetness(sweetness, K):
    left, right = 1, sum(sweetness)
    while left < right:
        mid = (left + right + 1) // 2
        total, cuts = 0, 0
        for s in sweetness:
            total += s
            if total >= mid:
                cuts += 1
                total = 0
        if cuts >= K + 1:
            left = mid
        else:
            right = mid - 1
    return left

# Example usage
if __name__ == "__main__":
    print(maximizeSweetness([1,2,3,4,5,6,7,8,9], 5))  # Output: 6
