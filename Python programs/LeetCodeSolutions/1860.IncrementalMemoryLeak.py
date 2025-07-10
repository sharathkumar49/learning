"""
LeetCode 1860. Incremental Memory Leak

You are given two integers memory1 and memory2 representing the available memory in two memory sticks. A program will be run in an infinite loop in which it will do the following:

1. Allocate memory to the stick with more available memory (or to memory1 if both have the same).
2. If there is not enough memory to allocate, the program crashes.

Return an array of length 3, [crashTime, memory1, memory2], where crashTime is the time (the number of times memory was allocated) the program crashes, and memory1 and memory2 are the available memory in each stick at the time of the crash.

Example:
Input: memory1 = 2, memory2 = 2
Output: [3, 0, 1]

Constraints:
- 0 <= memory1, memory2 <= 2*10^9
"""

def memLeak(memory1, memory2):
    t = 1
    while True:
        if memory1 >= memory2:
            if memory1 < t:
                return [t, memory1, memory2]
            memory1 -= t
        else:
            if memory2 < t:
                return [t, memory1, memory2]
            memory2 -= t
        t += 1

# Example usage:
print(memLeak(2, 2))  # Output: [3, 0, 1]
