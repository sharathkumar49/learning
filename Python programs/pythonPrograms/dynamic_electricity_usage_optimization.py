
# Dynamic Electric Usage Optimization
# A company wants to minimize electricity costs by scheduling tasks during 
# off-peak hours. Given a list of tasks with different power consumption
# levels, find the most efficient way to group tasks so that no group exceeds
# the max power limit.

# Input: power_usage = [30, 50, 20, 40, 60], max_power_limit = 80
# Output: 3 (groups: [30, 50], [20, 40], [60])

def min_power_groups(power_usage, max_power_limit):
    power_usage.sort(reverse=True)  # Sort tasks in descending order
    groups = []  # List to hold the current groups

    for task in power_usage:
        placed = False
        for i in range(len(groups)):
            if sum(groups[i]) + task <= max_power_limit:
                groups[i].append(task)
                placed = True
                break
        if not placed:
            groups.append([task])  # Create a new group for this task

    return len(groups)

# Example usage
if __name__ == "__main__":
    power_usage = [30, 50, 20, 40, 60]
    max_power_limit = 80
    print("Minimum power groups needed:", min_power_groups(power_usage, max_power_limit))  # Output: 3





def min_task_groups(power_usage, max_power_limit):
    power_usage.sort(reverse=True)
    groups = 0
    
    while power_usage:
        current = power_usage.pop(0)
        for i in range(len(power_usage)):
            if current + power_usage[i] <= max_power_limit:
                power_usage.pop(i)
                break
        groups += 1
    
    return groups

# Example usage
power_usage = [30, 50, 20, 40, 60]
max_power_limit = 80
print("Minimum task groups:", min_task_groups(power_usage, max_power_limit))