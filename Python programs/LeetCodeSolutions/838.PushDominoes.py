"""
838. Push Dominoes

Given a string dominoes representing dominoes, return the final state after all dominoes have fallen.

Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Constraints:
- 1 <= dominoes.length <= 10^5
- dominoes[i] is 'L', 'R', or '.'
"""
def pushDominoes(dominoes):
    symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
    symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
    res = list(dominoes)
    for (i, x), (j, y) in zip(symbols, symbols[1:]):
        if x == y:
            for k in range(i+1, j):
                res[k] = x
        elif x == 'R' and y == 'L':
            for k in range(i+1, j):
                if k - i == j - k:
                    continue
                res[k] = 'R' if k - i < j - k else 'L'
    return ''.join(res)

# Example usage:
print(pushDominoes("RR.L"))  # Output: "RR.L"
print(pushDominoes(".L.R...LR..L.."))  # Output: "LL.RR.LLRRLL.."
