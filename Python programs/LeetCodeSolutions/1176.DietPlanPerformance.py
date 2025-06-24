"""
1176. Diet Plan Performance

Given an array calories, an integer k, lower, and upper, return the total points. For each consecutive subarray of length k, add 1 point if the sum > upper, -1 if sum < lower, else 0.

Constraints:
- 1 <= k <= calories.length <= 10^5
- 0 <= calories[i] <= 20000
- 0 <= lower <= upper

Example:
Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
Output: 0

"""
def dietPlanPerformance(calories, k, lower, upper):
    points = 0
    s = sum(calories[:k])
    if s < lower:
        points -= 1
    elif s > upper:
        points += 1
    for i in range(k, len(calories)):
        s += calories[i] - calories[i-k]
        if s < lower:
            points -= 1
        elif s > upper:
            points += 1
    return points

# Example usage
if __name__ == "__main__":
    print(dietPlanPerformance([1,2,3,4,5], 1, 3, 3))  # Output: 0
