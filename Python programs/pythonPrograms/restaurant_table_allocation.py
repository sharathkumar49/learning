

# Problem: Restaurant Table Allocation
# A restaurant has tables that seat exactly table_size people. 
# Customers arrive in groups, and you must minimize the number of
# used
# 
# Example:
# Input: groups = [4, 2, 1, 3, 5], table_size = 6
#  Output: 3 (tables used: [4, 2], [1, 3, 2], [5])


def min_tables(groups, table_size):
    groups.sort(reverse=True)  # Sort groups in descending order
    tables = []  # List to hold the current tables

    for group in groups:
        placed = False
        for i in range(len(tables)):
            if sum(tables[i]) + group <= table_size:
                tables[i].append(group)
                placed = True
                break
        if not placed:
            tables.append([group])  # Create a new table for this group

    return len(tables)


# Example usage
if __name__ == "__main__":
    groups = [4, 2, 1, 3, 5]
    table_size = 6
    print("Minimum tables used:", min_tables(groups, table_size))  # Output: 3






# Method 2: Using a greedy approach
def min_tables_greedy(groups, table_size):
    groups.sort(reverse=True)  # Sort groups in descending order
    tables = []  # List to hold the current tables

    for group in groups:
        placed = False
        for i in range(len(tables)):
            if sum(tables[i]) + group <= table_size:
                tables[i].append(group)
                placed = True
                break
        if not placed:
            tables.append([group])  # Create a new table for this group
    return len(tables)

# Example usage     
if __name__ == "__main__":
    groups = [4, 2, 1, 3, 5]
    table_size = 6
    print("Minimum tables used (greedy):", min_tables_greedy(groups, table_size))  # Output: 3





# Method 3: Using a dynamic programming approach with partitioning
def min_tables_dp(groups, table_size):
    n = len(groups)
    dp = [float('inf')] * (1 << n)  # DP table to track minimum tables used for subsets
    dp[0] = 0  # No groups, no tables

    # Precompute valid subsets that fit within table_size
    subset_sum = [0] * (1 << n)
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                subset_sum[mask] += groups[i]

    # Compute DP
    for mask in range(1 << n):
        for submask in range(mask, 0, -1):  # Iterate through subsets
            submask &= mask  # Ensure valid submasks
            if subset_sum[submask] <= table_size:  # Can fit in one table
                dp[mask] = min(dp[mask], dp[mask ^ submask] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1

# Example usage     
if __name__ == "__main__":
    groups = [4, 2, 1, 3, 5]
    table_size = 6
    print("Minimum tables used (DP):", min_tables_dp(groups, table_size))  # Output: 3





# Method 4: Using a backtracking approach
def min_tables_backtrack(groups, table_size, index=0, current_table=None, table_count=0):
    if current_table is None:
        current_table = []

    if index == len(groups):
        return table_count + (1 if current_table else 0)  # Count the last table if non-empty

    # Option 1: Place the current group in the current table
    with_current = float('inf')
    if sum(current_table) + groups[index] <= table_size:
        current_table.append(groups[index])
        with_current = min_tables_backtrack(groups, table_size, index + 1, current_table, table_count)
        current_table.pop()  # Backtrack

    # Option 2: Start a new table with the current group
    without_current = min_tables_backtrack(groups, table_size, index + 1, [groups[index]], table_count + 1)

    return min(with_current, without_current)

# Example usage
if __name__ == "__main__":
    groups = [4, 2, 1, 3, 5]
    table_size = 6
    result = min_tables_backtrack(groups, table_size)
    print("Minimum tables used (backtracking):", result)







# Method 5: Using a binary search approach
def can_allocate(groups, table_size, num_tables):
    current_table = 0
    current_sum = 0

    for group in groups:
        if current_sum + group > table_size:
            current_table += 1
            current_sum = group  # Start a new table with the current group
            if current_table >= num_tables:  # If we exceed the number of tables, return False
                return False
        else:
            current_sum += group

    return True  # All groups can be allocated within the given number of tables

def min_tables_binary_search(groups, table_size):   
    left, right = 1, len(groups)  # Minimum 1 table, maximum number of groups
    result = len(groups)

    while left <= right:
        mid = (left + right) // 2
        if can_allocate(groups, table_size, mid):
            result = mid
            right = mid - 1  # Try to find fewer tables
        else:
            left = mid + 1  # Need more tables

    return result

# Example usage
if __name__ == "__main__":
    groups = [4, 2, 1, 3, 5]
    table_size = 6
    print("Minimum tables used (binary search):", min_tables_binary_search(groups, table_size))  # Output: 3    






# Method 6: 
def min_tables_needed(groups, table_size):
    groups.sort(reverse=True)  # Sort groups in descending order
    tables = 0

    while groups:
        current = groups.pop(0)
        for i in range(len(groups)):
            if current + groups[i] <= table_size:
                current += groups[i]
                groups.pop(i)
                break
        tables += 1
    
    return tables

# Example usage
if __name__ == "__main__":
    groups = [4, 2, 1, 3, 5]
    table_size = 6
    print("Minimum tables needed:", min_tables_needed(groups, table_size))  # Output: 3