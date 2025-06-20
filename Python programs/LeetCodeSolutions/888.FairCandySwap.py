"""
888. Fair Candy Swap

Alice and Bob have candy bars of different sizes. Return a pair of values (one from Alice, one from Bob) to swap so that they both have the same total amount of candy.

Example 1:
Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]

Example 2:
Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]

Constraints:
- 1 <= aliceSizes.length, bobSizes.length <= 10^4
- 1 <= aliceSizes[i], bobSizes[i] <= 10^5
- Alice and Bob have different total amounts initially.
- There exists an answer.
"""
def fairCandySwap(aliceSizes, bobSizes):
    sumA, sumB = sum(aliceSizes), sum(bobSizes)
    setB = set(bobSizes)
    for a in aliceSizes:
        if a + (sumB - sumA) // 2 in setB:
            return [a, a + (sumB - sumA) // 2]

# Example usage:
print(fairCandySwap([1,1], [2,2]))  # Output: [1,2]
print(fairCandySwap([1,2], [2,3]))  # Output: [1,2]
