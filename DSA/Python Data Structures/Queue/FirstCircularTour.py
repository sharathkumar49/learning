# Program: Implement a Queue for First Circular Tour (Petrol Pump)
# Problem: Find the first petrol pump from which a truck can complete the circle (queue simulation).
from collections import deque

def first_circular_tour(petrol, distance):
    n = len(petrol)
    start = 0
    curr_petrol = 0
    prev_petrol = 0
    for i in range(n):
        curr_petrol += petrol[i] - distance[i]
        if curr_petrol < 0:
            start = i + 1
            prev_petrol += curr_petrol
            curr_petrol = 0
    if curr_petrol + prev_petrol >= 0:
        return start
    else:
        return -1

if __name__ == '__main__':
    petrol = [4, 6, 7, 4]
    distance = [6, 5, 3, 5]
    print(first_circular_tour(petrol, distance))
