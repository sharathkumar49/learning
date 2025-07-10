def integer_partitions(n):
    result = []

    def backtrack(remaining, path, max_value):
        print(f"remaining: {remaining}, path: {path}, max_value: {max_value}")
        if remaining == 0:
            print("remaining is zero and append path", path)
            result.append(path[:])
            print("result", result)
            print("after appending the final path, returning to the main call\n\n\n\n\n")
            return

        print(f"range_list: {list(range(min(remaining, max_value)))[::-1]}")
        for i in range(min(remaining, max_value), 0, -1):
            print("\n",f"i: {i}  the range selected between {remaining} and {max_value} and the resultant: {min(remaining, max_value)}")
            path.append(i)
            print(f"appending i: {i} to the path:{path}")
            print(f"calling backtracking function with (remaining - i) is {remaining - i} where remaining is {remaining} and i is {i}, path:{path}, max_value:{max_value}")
            print(f"So, ({remaining - i}, {path}), {i})")
            backtrack(remaining - i, path, i)  # Only use values ≤ i to maintain order
            print(f"poping the single value from path:{path}, which is {path[-1]}")
            path.pop()
            print("returning")

    backtrack(n, [], n)
    return result


print(integer_partitions(5))
# Output:
# [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
