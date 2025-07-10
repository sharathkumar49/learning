"""
LeetCode 1854. Maximum Population Year

You are given a 2D integer array logs where each logs[i] = [birth_i, death_i], representing the birth and death years of people. The population of a year y is the number of people alive during that year (including birth year, but not death year). Return the earliest year with the maximum population.

Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993

Constraints:
- 1 <= logs.length <= 100
- 1950 <= birth_i < death_i <= 2050
"""

def maximumPopulation(logs):
    years = [0]*101
    for b, d in logs:
        years[b-1950] += 1
        years[d-1950] -= 1
    max_pop = years[0]
    year = 1950
    for i in range(1, 101):
        years[i] += years[i-1]
        if years[i] > max_pop:
            max_pop = years[i]
            year = 1950 + i
    return year

# Example usage:
# logs = [[1993,1999],[2000,2010]]
# print(maximumPopulation(logs))  # Output: 1993
