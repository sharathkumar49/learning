"""
1240. Tiling a Rectangle with the Fewest Squares

Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.

Constraints:
- 1 <= n, m <= 13

Example:
Input: n = 2, m = 3
Output: 3

"""
def tilingRectangle(n, m):
    if n > m:
        n, m = m, n
    res = n * m
    def dfs(h, cnt):
        nonlocal res
        if cnt >= res:
            return
        i = 0
        while i < n and h[i] == m:
            i += 1
        if i == n:
            res = min(res, cnt)
            return
        max_len = 1
        while i + max_len <= n and all(h[j] == h[i] for j in range(i, i+max_len)) and h[i] + max_len <= m:
            max_len += 1
        for l in range(max_len-1, 0, -1):
            for j in range(i, i+l):
                h[j] += l
            dfs(h, cnt+1)
            for j in range(i, i+l):
                h[j] -= l
    dfs([0]*n, 0)
    return res

# Example usage
if __name__ == "__main__":
    print(tilingRectangle(2, 3))  # Output: 3
