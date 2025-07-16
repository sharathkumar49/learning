"""
LeetCode 2491. Divide Players Into Teams of Equal Skill

Given an array, divide players into teams of equal skill and return the total chemistry.

Constraints:
- 2 <= skill.length <= 10^5
"""

def dividePlayers(skill):
    skill.sort()
    total = 0
    n = len(skill)
    target = skill[0]+skill[-1]
    for i in range(n//2):
        if skill[i]+skill[n-1-i] != target:
            return -1
        total += skill[i]*skill[n-1-i]
    return total

# Example usage:
# print(dividePlayers([3,2,5,1,3,4]))  # Output: 22
