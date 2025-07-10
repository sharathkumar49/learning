def all_permuted_partitions(n):
    result = []

    def backtrack(remaining, path):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(1, remaining + 1):  # Try 1 to remaining
            path.append(i)
            backtrack(remaining - i, path)
            path.pop()

    backtrack(n, [])
    return result

print(all_permuted_partitions(5))
