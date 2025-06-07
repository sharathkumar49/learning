# Route Optimization for Delivery Trucks

# You have multiple delivery locations. 
# The goal is to find the shortest possible route that 
# covers all locations while minimizing fuel consumption.

# Approach
# Use the Traveling Salesman Problem (TSP) with a 
# greedy nearest-neighbor algorithm.

# Assume distances are given in a 2D matrix.

from itertools import permutations

def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    return total_distance

def find_optimal_route(distance_matrix):
    num_locations = len(distance_matrix)
    locations = list(range(num_locations))
    min_distance = float('inf')
    best_route = None

    for route in permutations(locations):
        distance = calculate_distance(route, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],  # Distances from location 0
    [10, 0, 35, 25],  # Distances from location 1
    [15, 35, 0, 30],  # Distances from location 2
    [20, 25, 30, 0]   # Distances from location 3
]

optimal_route, min_distance = find_optimal_route(distance_matrix)
print("Optimal Delivery Route:", optimal_route)
print("Minimum Distance:", min_distance)