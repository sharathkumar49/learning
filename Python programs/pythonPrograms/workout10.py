def find_partitions(n):
    result = []

    def helper(remaining, current, max_num):
        print("calling helper function")
        print("Remaining:", remaining, "Current:", current, "Max Num:", max_num)
        if remaining == 0:
            result.append(current[:])  # Store valid partition
            print("result: ", result)
            return

        for i in range(min(remaining, max_num), 0, -1):  # Choose decreasing numbers
            print("\n\nfor loop i: ", i)
            current.append(i)
            print("current after append: ", current)
            print("calling helper function with:", remaining - i, current, i)
            helper(remaining - i, current, i)  # Reduce remaining sum
            current.pop()  # Undo last step (backtrack)

    helper(n, [], n)  # Start recursion
    return result

# Example Usage
num = 5
print(find_partitions(num))


    