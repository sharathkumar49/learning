# Amazon: Find the Maximum Length of Pair Chain
# You are given n pairs of numbers. In every pair, the first number is always less than the second number.
# A pair (c, d) can follow another pair (a, b) if and only if b < c.
# Find the length longest chain which can be formed.

def find_longest_chain(pairs):
    pairs.sort(key=lambda x: x[1])
    curr, res = float('-inf'), 0
    for pair in pairs:
        if pair[0] > curr:
            curr = pair[1]
            res += 1
    return res

if __name__ == "__main__":
    print(find_longest_chain([[1,2],[2,3],[3,4]]))  # Output: 2
    print(find_longest_chain([[1,2],[7,8],[4,5]]))  # Output: 3
