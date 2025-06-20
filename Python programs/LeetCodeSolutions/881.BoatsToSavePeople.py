"""
881. Boats to Save People

Given an array people where people[i] is the weight of the i-th person, and an integer limit, return the minimum number of boats to carry every person. Each boat can carry at most two people at the same time, provided the sum of the weight is at most limit.

Example 1:
Input: people = [1,2], limit = 3
Output: 1

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3

Constraints:
- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4
"""
def numRescueBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    return boats

# Example usage:
print(numRescueBoats([1,2], 3))        # Output: 1
print(numRescueBoats([3,2,2,1], 3))    # Output: 3
