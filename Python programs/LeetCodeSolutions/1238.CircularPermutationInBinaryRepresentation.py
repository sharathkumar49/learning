"""
1238. Circular Permutation in Binary Representation

Given n and a start, return an array representing the circular permutation in binary representation starting from start.

Constraints:
- 1 <= n <= 16
- 0 <= start < 2^n

Example:
Input: n = 2, start = 3
Output: [3,2,0,1]

"""
def circularPermutation(n, start):
    res = [start]
    for i in range(1, 1 << n):
        res.append(start ^ i ^ (i >> 1))
    return res

# Example usage
if __name__ == "__main__":
    print(circularPermutation(2, 3))  # Output: [3,2,0,1]
