"""
LeetCode 2383. Minimum Hours of Training to Win a Competition

Given initial energy and experience, return the minimum hours of training needed to win.

Constraints:
- 1 <= initialEnergy, initialExperience <= 100
- 1 <= energy.length == experience.length <= 100
"""

def minTrainingHours(initialEnergy, initialExperience, energy, experience):
    hours = 0
    for e in energy:
        if initialEnergy <= e:
            hours += e - initialEnergy + 1
            initialEnergy = e + 1
        initialEnergy -= e
    for exp in experience:
        if initialExperience <= exp:
            hours += exp - initialExperience + 1
            initialExperience = exp + 1
        initialExperience += exp
    return hours

# Example usage:
# print(minTrainingHours(5,3,[1,4],[2,5]))  # Output: 2
