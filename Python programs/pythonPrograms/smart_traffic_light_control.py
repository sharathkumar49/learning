
# Smart Traffic Light Control
# You are designing a system for traffic light control.
# Given an array representing the arrival times of cars at an intersection
# and the max duration the light can stay green, determine the 
# minimum number of green light cycles required to allow all cars to pass.

# Input : # arrival_times = [1, 3, 6, 8, 12, 15], green_light_duration = 5
# Output: 3 (cycles: [1, 3, 6], [8, 12], [15])


def min_green_light_cycles(arrivals, green_light_duration):
    arrivals.sort()  # Sort the arrival times
    cycles = 0
    i = 0
    while i < len(arrivals):
        cycles += 1
        start_time = arrivals[i]

        # Count how many cars can pass in this cycle
        while i < len(arrivals) and arrival_times[i] - start_time < green_light_duration:
            i += 1

    return cycles

# Example usage
if __name__ == "__main__":
    arrival_times = [1, 3, 6, 8, 12, 15]
    green_light_duration = 5
    print("Minimum green light cycles:", min_green_light_cycles(arrival_times, green_light_duration))  # Output: 3





def min_green_cycles(arrival_times, green_duration):
    arrival_times.sort()  # Sort the arrival times
    cycles = 0
    i = 0

    while i < len(arrival_times):
        cycles += 1
        cycle_start = arrival_times[i]
        cycle_end = cycle_start + green_duration

        # Count how many cars can pass in this cycle
        while i < len(arrival_times) and arrival_times[i] < cycle_end:
            i += 1

    return cycles

# Example usage
if __name__ == "__main__":
    arrival_times = [1, 2, 3, 5, 6, 8, 10]
    green_duration = 3
    print("Minimum green light cycles required:", min_green_cycles(arrival_times, green_duration))  # Output: 3