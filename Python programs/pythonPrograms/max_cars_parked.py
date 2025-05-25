
# Efficient Parking Lot Management System

# A parking lot receives cars with different parking durations.
# Given a list of arrival times and durations,
# find the maximum number of cars parked at any time.


# Input: arrivals = [1, 2, 5, 6], durations = [4, 3, 2, 4]
# Output: 2


def max_cars_parked(arrivals, durations):
    events = []
    for i in range(len(arrivals)):
        events.append((arrivals[i], 1)) #Car enters
        events.append((arrivals[i] + durations[i], -1)) #cars exits
    events.sort()
    max_cars = 0
    current_cars = 0

    for _, event in events:
        current_cars += event
        max_cars = max(max_cars, current_cars)

    return max_cars

# Example usage      
if __name__ == "__main__":
	arrivals = [1, 2, 5, 6]
	durations = [4, 3, 2, 4]
	print("Maximum cars parked: ", max_cars_parked(arrivals, durations))  # Output: 2