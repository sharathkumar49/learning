def find_partitions(n):
    result = []
    
    def helper(remaining, current, max_num):
        if remaining == 0:
            result.append(current[:])  # Store the valid partition
            return

        for i in range(min(remaining, max_num), 1, -1):
            current.append(i)
            helper(remaining - i, current, i)  # Reduce remaining sum
            current.pop()  # Undo last step (backtrack)

    helper(n, [], n)  # Start recursion
    return result

# Example Usage
num = 5
print(find_partitions(num))
