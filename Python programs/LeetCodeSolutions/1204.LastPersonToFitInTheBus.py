"""
1204. Last Person to Fit in the Bus

Given a list of groups and the bus capacity, return the number of people in the last group that can fit in the bus.

Constraints:
- 1 <= groups.length <= 1000
- 1 <= groups[i] <= 1000
- 1 <= busCapacity <= 1000

Example:
Input: groups = [1,4,2,1], busCapacity = 5
Output: 1

"""
def lastPersonToFit(groups, busCapacity):
    total = 0
    for g in groups:
        if total + g > busCapacity:
            break
        total += g
        last = g
    return last

# Example usage
if __name__ == "__main__":
    print(lastPersonToFit([1,4,2,1], 5))  # Output: 1
