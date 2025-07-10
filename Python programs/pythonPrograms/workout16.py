def strictly_increasing_partitions(n):
    result = []

    def backtrack(remaining, path, min_value):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(min_value + 1, remaining + 1):  # Strictly increasing
            path.append(i)
            backtrack(remaining - i, path, i)
            path.pop()

    backtrack(n, [], 0)
    return result


print(strictly_increasing_partitions(5))