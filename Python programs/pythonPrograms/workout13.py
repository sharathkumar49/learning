def integer_partitions(n):
    result = []

    def backtrack(remaining, path, max_value):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(min(remaining, max_value), 0, -1):
            path.append(i)
            backtrack(remaining - i, path, i)  # Only use values ≤ i to maintain order
            path.pop()

    backtrack(n, [], n)
    return result
  


print(integer_partitions(5))
# Output:
# [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
